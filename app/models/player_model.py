# -*- coding: utf-8 -*-


from PyQt5 import (
    QtCore
)



class PlayerModel(QtCore.QAbstractListModel):

    def __init__(self, QMediaPlaylist, *args, **kwargs):

        super(PlayerModel, self).__init__(*args, **kwargs)

        self.QMediaPlaylist = QMediaPlaylist


        # self.Controller = Controller
        # self.__DatabaseModel = DatabaseModel(self.Controller)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            media = self.QMediaPlaylist.media(index.row())
            
            #print(media.canonicalUrl().path())


            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.QMediaPlaylist.mediaCount()
