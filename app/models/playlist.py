from app.models.database import DatabaseModel

from PyQt5 import QtCore


class PlayerModel(QtCore.QAbstractListModel):

    # def __init__(self, Controller, playlist, *args, **kwargs):
    def __init__(self, playlist, *args, **kwargs):

        super(PlayerModel, self).__init__(*args, **kwargs)

        self.playlist = playlist
        self.attr = {
            'path': []
        }

        # self.Controller = Controller
        # self.__DatabaseModel = DatabaseModel(self.Controller)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            media = self.playlist.media(index.row())

            self.attr['path'].append(media.canonicalUrl().path())

            # self.__DatabaseModel.insert_data(
            #    query = 'INSERT INTO session (time, file_path) VALUES (CURRENT_TIMESTAMP, ?)',
            #    parameters = (media.canonicalUrl().path(),)
            # )
            # self.__DatabaseModel.connection.close()

            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()
