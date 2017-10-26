import logging, os, psycopg2
from contextlib import contextmanager


from argparse import ArgumentParser, Namespace

def common_arguments(parser: ArgumentParser):
    parser.add_argument('config', help='Path to .ini file')
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--db-name')
    parser.add_argument('--db-user')
    parser.add_argument('--db-password')

def parse_args(parser: ArgumentParser) -> Namespace:
    return parser.parse_args()


import yaml


def load_config(path):
    with open(path) as source:
        return yaml.load(source)


def adjust_config(args: Namespace, config):
    for name in 'name', 'user', 'password':
        environ_value = os.environ.get('DB_'+name.upper())
        arg_value = getattr(args, 'db_'+name)
        value = arg_value or environ_value
        if value:
            config['db'][name] = value


import sys
from subprocess import list2cmdline

logger = logging.getLogger()

def setup_logging(log_path, quiet=False, verbose=False):
    handler = logging.FileHandler(log_path)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    if not quiet:
        handler = logging.StreamHandler(sys.stderr)
        handler.setLevel(logging.DEBUG if verbose else logging.INFO)
        logger.addHandler(handler)

@contextmanager
def log_details():
    logger.info('Called as: %s', list2cmdline(sys.argv))
    try:
        yield
    except KeyboardInterrupt:
        logger.warning('keyboard interrupt')
        raise
    except SystemExit:
        logger.error('system exit')
        raise
    except:
        logger.exception('unhandled exception')


logger = logging.getLogger(__name__)

@contextmanager
def handle_database(name, user, password):
    conn = psycopg2.connect(dbname=name, user=user, password=password)
    try:
        yield conn
        conn.commit()
    except:
        logger.exception('commit failed')
        conn.rollback()
        raise
