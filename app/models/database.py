import sqlite3


class DatabaseModel(object):
    def __init__(self, Controller):

        super(DatabaseModel, self).__init__()

        self.Controller = Controller

    def set_local_database(self, path: str):

        try:

            self.connection = sqlite3.connect(path)
            self.cursor = self.connection.cursor()

            return self.connection, self.cursor

        except Exception as exception:

            self.Controller.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def insert_data(self, query: str, parameters: tuple):

        try:
            self.Controller.Logger.debug(msg=f'Ejecutando query -> {query}')
            self.Controller.Logger.debug(
                msg=f'Insertando parametros -> {parameters}')

            self.cursor.execute(query, parameters)
            self.connection.commit()

        except Exception as exception:

            self.Controller.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def get_id(self):
        try:
            self.cursor.execute('SELECT max(id) FROM playlist')

            for parameter in self.cursor.fetchall():
                self.Controller.Logger.debug(
                    msg=f'Parametro {parameter} obtenido.')

                id_ = int(parameter[0])
                id_ += 1

                return id_

        except Exception as exception:

            self.Controller.Logger.warning(
                msg=f'Exception\t{exception}'
            )
