from argparse import ArgumentParser
from configparser import RawConfigParser
import logging, os, psycopg2, sys


class BaseScript(object):

    def load_args(self):
        parser = ArgumentParser()
        parser.add_argument('config', help='Path to .ini file')
        parser.add_argument('-q', '--quiet', action='store_true')
        parser.add_argument('-v', '--verbose', action='store_true')
        self.add_args(parser)
        self.args = parser.parse_args()

    def add_args(self):
        pass

    def load_config(self):
        self.config = RawConfigParser()
        self.config.read(self.args.config)

    def setup_logging(self):
        handler = logging.FileHandler(self.config.get('main', 'log'))
        handler.setLevel(logging.DEBUG)
        self.log = logging.getLogger()
        self.log.addHandler(handler)
        self.log.setLevel(logging.DEBUG)
        if not self.args.quiet:
            handler = logging.StreamHandler(sys.stderr)
            handler.setLevel(logging.DEBUG if self.args.verbose else logging.INFO)
            self.log.addHandler(handler)

    _conn = None
    @property
    def conn(self):
        if self._conn is None:
            db = self.config.get('db', 'name')
            user = self.config.get('db', 'user')
            password = self.config.get('db', 'password')
            self.log.debug('connecting to %s as %s', db, user)
            conn = psycopg2.connect(dbname=db, user=user, password=password)
            self._conn = conn
        return self._conn

    def run(self):
        self.load_args()
        self.load_config()
        self.setup_logging()
        try:
            self.script(self)
            self.conn.commit()
        except:
            self.conn.rollback()
            self.log.exception('script failed')
        else:
            self.log.info('completed successfully')

    def script(self, parser):
        pass


class MyScript(BaseScript):

    def add_args(self):
        self.parser.add_argument('path', help='Path to the file to process')

    def script(self):
        filename = os.path.basename(self.args.path)
        with open(self.args.path) as source:
            self.log.debug('opened %s to insert as %s', self.args.path, filename)
            cursor = self.conn.cursor()
            cursor.execute('insert into notes values (%s, %s)',
                           (filename, source.read()))
        self.log.info('successfully inserted %s', filename)


if __name__ == '__main__':
    MyScript().run()
