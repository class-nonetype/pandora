

from PyQt5 import QtCore


class PlaylistModel(QtCore.QAbstractListModel):

    def __init__(self, playlist, *args, **kwargs):

        super(PlaylistModel, self).__init__(*args, **kwargs)

        self.playlist = playlist



    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()