import sqlite3


class Database(object):
    def __init__(self, Controller):

        super(Database, self).__init__()

        self.Controller = Controller

    def set_local_database(self, path: str):

        try:

            self.connection = sqlite3.connect(path)
            self.cursor = self.connection.cursor()
            
            self.__create_tables()

            return self.connection, self.cursor

        except Exception as exception:
            print(exception)
    
    
    
    def __create_tables(self):
        CREATE_TABLE_PLAYLIST = '''
        
            CREATE TABLE IF NOT EXISTS playlist (
                    playlist_id                  INTEGER PRIMARY KEY,
                    playlist_name                VARCHAR2(100),
                    playlist_file_path           VARCHAR2(250),
                    playlist_file_name           VARCHAR2(250)

            )
                
        '''
        self.cursor.execute(CREATE_TABLE_PLAYLIST)
        self.connection.commit()

        
    def insert_data(self, query: str, parameters: tuple):

        self.cursor.execute(query, parameters)
        self.connection.commit()



    def get_id(self):
        self.cursor.execute('SELECT max(playlist_id) FROM playlist')

        for parameter in self.cursor.fetchall():
            
            if parameter[0] is not None:
            
                playlist_id = int(parameter[0])
                playlist_id += 1
            
            else:
                playlist_id = int(0)
                playlist_id += 1

            return playlist_id


