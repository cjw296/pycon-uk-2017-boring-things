
from .components import (
    common_arguments, parse_args, load_config, adjust_config, setup_logging,
    handle_database, log_details
)

from argparse import ArgumentParser, Namespace
from mush import Runner, attr, item, requires

script = Runner()
script.add(ArgumentParser)
script.add(common_arguments)

script.add_label('args')

script.add(parse_args)
script.add(load_config,
           requires=attr(Namespace, 'config'),
           returns='config')
script.add(adjust_config)

script.add_label('adjust_config')

script.add(setup_logging, requires(
    log_path=item('config', 'log_path'),
    quiet=attr(Namespace, 'quiet'),
    verbose=attr(Namespace, 'verbose'),
))
script.add(log_details)

script.add(handle_database, requires(
    name=item('config', 'db', 'name'),
    user=item('config', 'db', 'user'),
    password=item('config', 'db', 'password'),
))

script.add_label('body')


import logging
import os

from argparse import ArgumentParser, Namespace
from mush import attr
from psycopg2.extensions import connection as Psycopg2Connection

logger = logging.getLogger(__name__)


def args(parser: ArgumentParser):
    parser.add_argument('path', help='Path to the file to process')


def insert_note(path: attr(Namespace, 'path'), conn: Psycopg2Connection):
    filename = os.path.basename(path)
    with open(path) as source:
        logger.debug('opened %s to insert as %s', path, filename)
        cursor = conn.cursor()
        cursor.execute('insert into notes values (%s, %s)',
                       (filename, source.read()))
    logger.info('successfully inserted %s', filename)


main = script.clone()
main['args'].add(args)
main.add(insert_note)
if __name__ == '__main__':
    main()
