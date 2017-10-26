from argparse import ArgumentParser

from .components import (
    common_arguments, parse_args, load_config, adjust_config, setup_logging,
    handle_database, log_details
)


def script(func, add_args=None):

    parser = ArgumentParser()
    common_arguments(parser)
    if add_args:
        add_args(parser)
    args = parse_args(parser)

    config = load_config(args.config)
    adjust_config(args, config)

    setup_logging(config['log_path'], args.quiet, args.verbose)

    with log_details():

        with handle_database as conn:
            func(...)


import logging
import os

logger = logging.getLogger(__name__)

def insert_note(path, conn):
    filename = os.path.basename(path)
    with open(path) as source:
        logger.debug('opened %s to insert as %s', path, filename)
        cursor = conn.cursor()
        cursor.execute('insert into notes values (%s, %s)',
                       (filename, source.read()))
    logger.info('successfully inserted %s', filename)

def add_args(parser):
    parser.add_argument('path', help='Path to the file to process')

if __name__ == '__main__':
    script(insert_note, add_args)
