

import platform
import getpass
import socket
import sqlite3
import os


class EnvironmentModel(object):

    def __init__(self, Controller):

        super(EnvironmentModel, self).__init__()

        self.Controller = Controller

        self.attr = {
            'session': socket.gethostname() + '@' + getpass.getuser(),
            'system': {
                'user': getpass.getuser(),
                'os': platform.system(),
                'system': platform.system(),
                'version': platform.version(),
                'processor': platform.processor(),
                'node': platform.node(),
                'machine': platform.machine(),
                'architecture': platform.architecture(),
                'platform': platform.platform()
            },
            'path': {
                'execution': os.getcwd(),
                'storage': {
                    'storage': None,
                    'database': None,
                    'local': None,
                    'data': None,
                    'scripts': None,
                },
                'file': [],
                'log': None,
                'temp': []
            },
            'data': None,
        }

    def create_storage_directory(self):

        if self.attr['system']['os'] == 'Windows':
            self.attr['path']['storage']['storage'] = self.attr['path']['execution'] + \
                '\\' + 'app' + '\\' + 'storage'
            self.attr['path']['storage']['database'] = self.attr['path']['storage']['storage'] + '\\' + 'database'
            self.attr['path']['storage']['data'] = self.attr['path']['storage']['storage'] + '\\' + 'data'
            self.attr['path']['storage']['scripts'] = self.attr['path']['storage']['database'] + '\\' + 'scripts'
            self.attr['path']['log'] = self.attr['path']['execution'] + \
                '\\' + 'app' + '\\' + 'log'

        elif self.attr['system']['os'] == 'Linux':
            self.attr['path']['storage']['storage'] = self.attr['path']['execution'] + \
                '/' + 'app' + '/' + 'storage'
            self.attr['path']['storage']['database'] = self.attr['path']['storage']['storage'] + '/' + 'database'
            self.attr['path']['storage']['data'] = self.attr['path']['storage']['storage'] + '/' + 'data'
            self.attr['path']['storage']['scripts'] = self.attr['path']['storage']['database'] + '/' + 'scripts'
            self.attr['path']['log'] = self.attr['path']['execution'] + \
                '/' + 'app' + '/' + 'log'

        if not os.path.exists(self.attr['path']['storage']['storage']):
            os.mkdir(self.attr['path']['storage']['storage'])

        if not os.path.exists(self.attr['path']['storage']['database']):
            os.makedirs(self.attr['path']['storage']['scripts'])

        if not os.path.exists(self.attr['path']['log']):
            os.mkdir(self.attr['path']['log'])

    def create_scripts_directory(self):

        CREATE_TABLE_PLAYLIST = '''
        
        CREATE TABLE IF NOT EXISTS playlist (
            id                  INTEGER PRIMARY KEY,
            name                VARCHAR2(100),
            file_path           VARCHAR2(250)
        )
        
        '''

        if self.attr['system']['os'] == 'Windows':
            script_file_path = self.attr['path']['storage']['scripts'] + \
                '\\' + 'CREATE_TABLE_PLAYLIST.sql'

        elif self.attr['system']['os'] == 'Linux':
            script_file_path = self.attr['path']['storage']['scripts'] + \
                '/' + 'CREATE_TABLE_PLAYLIST.sql'

        with open(script_file_path, '+w') as script_file:
            script_file.write(CREATE_TABLE_PLAYLIST)
        script_file.close()

        CREATE_TABLE_INTEREST = '''
        
        CREATE TABLE IF NOT EXISTS interest(
            id                  INTEGER PRIMARY KEY,
            file_path           VARCHAR2(250)
        )
        
        '''
        if self.attr['system']['os'] == 'Windows':
            script_file_path = self.attr['path']['storage']['scripts'] + \
                '\\' + 'CREATE_TABLE_INTEREST.sql'

        elif self.attr['system']['os'] == 'Linux':
            script_file_path = self.attr['path']['storage']['scripts'] + \
                '/' + 'CREATE_TABLE_INTEREST.sql'

        with open(script_file_path, '+w') as script_file:
            script_file.write(CREATE_TABLE_INTEREST)
        script_file.close()

        CREATE_TABLE_SESSION = '''
        
        CREATE TABLE IF NOT EXISTS session(
            id                  INTEGER PRIMARY KEY,
            time                VARCHAR2(50),
            file_path           VARCHAR2(250)
        )
        
        '''
        if self.attr['system']['os'] == 'Windows':
            script_file_path = self.attr['path']['storage']['scripts'] + \
                '\\' + 'CREATE_TABLE_SESSION.sql'

        elif self.attr['system']['os'] == 'Linux':
            script_file_path = self.attr['path']['storage']['scripts'] + \
                '/' + 'CREATE_TABLE_SESSION.sql'

        with open(script_file_path, '+w') as script_file:
            script_file.write(CREATE_TABLE_SESSION)
        script_file.close()

    def create_local_database(self):

        try:
            if self.attr['system']['os'] == 'Windows':
                database_file_path = self.attr['path']['storage']['database'] + \
                    '\\' + 'storage.db'

            elif self.attr['system']['os'] == 'Linux':
                database_file_path = self.attr['path']['storage']['database'] + \
                    '/' + 'storage.db'

            if os.path.exists(self.attr['path']['storage']['database']):
                connection = sqlite3.connect(database_file_path)
                cursor = connection.cursor()

                self.attr['path']['storage']['local'] = database_file_path

                for script in os.scandir(self.attr['path']['storage']['scripts']):
                    with open(script.path, 'r') as script_file:

                        sql_script = script_file.read()
                        cursor.executescript(sql_script)
                        connection.commit()
                    script_file.close()

            connection.close()

        except Exception as exception:
            self.Controller.Logger.warning(
                msg=f'Exception\t{exception}'
            )
