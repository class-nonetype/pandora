


import os


from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets,
    QtMultimedia
)

from app.views.view import View
from app.models.model import Model






class Controller(object):
    
    
    def __init__(self):
        
        super(Controller, self).__init__()

        self.View = View(self)
        self.Model = Model(self)


    
    def get_main_window(self):
        return self.View.get_main_view()



    def main_window_restore(self):
        def dobleClickMaximizeRestore(event):
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(8, lambda: self.main_window_status_restore())
                
        self.View.MainWindowView.frameWindowTitleBar.mouseDoubleClickEvent = dobleClickMaximizeRestore



    def main_window_status_restore(self):
        def main_window_maximize():
            return self.View.MainWindowView.showMaximized()

        def main_window_minimize():
            return self.View.MainWindowView.showNormal()
        
        if self.View.MainWindowView.windowState() == QtCore.Qt.WindowState.WindowNoState:
            
            main_window_maximize()
            
            self.View.MainWindowView.pushButtonRestore.setToolTip('Restore')
            
            _icon = QtGui.QIcon()
            _icon.addPixmap(
                QtGui.QPixmap('app/resources/img/icons/24x24/cil-window-restore.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            self.View.MainWindowView.pushButtonRestore.setIcon(_icon)
            self.View.MainWindowView.pushButtonRestore.setIconSize(QtCore.QSize(20, 20))
        
        else:
            
            main_window_minimize()
            
            self.View.MainWindowView.pushButtonRestore.setToolTip('Maximize')
            
            _icon = QtGui.QIcon()
            _icon.addPixmap(
                QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-window-maximize.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            self.View.MainWindowView.pushButtonRestore.setIcon(_icon)
            self.View.MainWindowView.pushButtonRestore.setIconSize(QtCore.QSize(20, 20))



    def hhmmss(self, ms):
        # s = 1000
        # m = 60000
        # h = 360000
        s = round(ms / 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))



    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()



    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.View.playlist.addMedia(QtMultimedia.QMediaContent(url))

        self.View.PlaylistModel.layoutChanged.emit()

        # If not playing, seeking to first of newly added + play.
        if self.View.player.state() != QtMultimedia.QMediaPlayer.PlayingState:
            i = self.View.playlist.mediaCount() - len(e.mimeData().urls())
            self.View.playlist.setCurrentIndex(i)
            self.View.player.play()



    def open_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.View.MainWindowView,
            "Open file",
            "",
            "mp3 Audio (*.mp3);;flac Audio (*.flac);;wav Audio (*.wav);;All files (*.*)",
        )

        if path:
            self.View.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))

        self.View.PlaylistModel.layoutChanged.emit()



    def open_directory(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self.View.MainWindowView
        )

        if path:
            self.View.get_progress_view()
            for root, directories, files in os.walk(path):

                root = str(root).replace('/', '\\')

                for file in files:
                    if file[-4:] == 'flac' or file[-3:] == 'mp3' or file[-3:] == 'm4a':

                        

                        path = f'{root}\\{file}'

                        if os.path.exists(path):
                            
                            max_length = 60
                            path_length = len(path)

                            if path_length > max_length:

                                result_length = path_length - max_length
                                _path = path[:-result_length] + '...'

                                self.View.ProgressWindowView.labelProgress.setText(_path)
                            
                            else:
                                self.View.ProgressWindowView.labelProgress.setText(path)

                            self.View.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))
                            self.Model.EnvironmentModel.attr['path']['file'].append(path)

                            for index in range(len(files)):
                                
                                self.View.ProgressWindowView.progressBar.setValue(int(index))

                                if index > len(files):
                                    self.View.ProgressWindowView.progressBar.setValue(100)

                                self.View.ProgressWindowView.progressBar.setFormat('%.02f%%' % (float(index)))
                            QtWidgets.QApplication.processEvents()

                            self.View.ProgressWindowView.progressBar.setValue(100)
                        
                        else:
                            pass
                    self.View.ProgressWindowView.progressBar.setValue(100)

            self.View.ProgressWindowView.destroy()

        self.View.PlaylistModel.layoutChanged.emit()


        
    def update_duration(self, duration):
        self.View.MainWindowView.horizontalSliderTime.setMaximum(duration)

        if duration >= 0:
            self.View.MainWindowView.labelDuration.setText(self.hhmmss(duration))



    def update_position(self, position):
        if position >= 0:
            self.View.MainWindowView.labelTime.setText(self.hhmmss(position))


        # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
        self.View.MainWindowView.horizontalSliderTime.blockSignals(True)
        self.View.MainWindowView.horizontalSliderTime.setValue(position)
        self.View.MainWindowView.horizontalSliderTime.blockSignals(False)



    def playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i = ix.indexes()[0].row()
        self.View.playlist.setCurrentIndex(i)



    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.View.PlaylistModel.index(i)
            self.View.MainWindowView.listViewPlaylist.setCurrentIndex(ix)



    def exceptions(self, *args):
        print(args)

        pass



    def play_song(self):

        if self.View.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.View.player.pause()

 
        else:
            self.View.player.play()
        
        self.meta_data_changed()



    def next_song(self):

        self.meta_data_changed()
        self.View.playlist.next()
    


    def previous_song(self):
        self.meta_data_changed()
        self.View.playlist.previous()



    def meta_data_changed(self):


        if self.View.player.isMetaDataAvailable():
            self.View.MainWindowView.labelAlbumSong.setText(self.View.player.metaData(QtMultimedia.QMediaMetaData.AlbumTitle))
            self.View.MainWindowView.labelArtistSong.setText(self.View.player.metaData(QtMultimedia.QMediaMetaData.AlbumArtist))
            self.View.MainWindowView.labelTitleSong.setText(self.View.player.metaData(QtMultimedia.QMediaMetaData.Title))

            try:
                self.View.MainWindowView.labelCoverArt.setPixmap(
                    QtGui.QPixmap(self.View.player.metaData(QtMultimedia.QMediaMetaData.ThumbnailImage.encode('utf-8').decode('utf-8'))))

            except Exception as exception:
                print(exception)
                self.View.MainWindowView.labelCoverArt.setPixmap(QtGui.QPixmap(u'app/resources/img/default/cover-art.png'))

            self.View.MainWindowView.labelCodec.setText(self.View.player.metaData(QtMultimedia.QMediaMetaData.AudioCodec))
            self.View.MainWindowView.labelBitrate.setText(
                f'{int(self.View.player.metaData(QtMultimedia.QMediaMetaData.AudioBitRate) * 0.001)}kbps'
            )
        

    def handle_reproduction_state(self, state):
        if self.View.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            _icon = QtGui.QIcon()
            _icon.addPixmap(
                QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-media-pause.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                
            self.View.MainWindowView.pushButtonPlay.setIcon(_icon)
            self.View.MainWindowView.pushButtonPlay.setIconSize(QtCore.QSize(20, 20))

 
        else:
            _icon = QtGui.QIcon()
            _icon.addPixmap(
                QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-media-play.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                
            self.View.MainWindowView.pushButtonPlay.setIcon(_icon)
            self.View.MainWindowView.pushButtonPlay.setIconSize(QtCore.QSize(20, 20))

        self.meta_data_changed()

        

    def handle_volume_state(self):
        self.View.player.setMuted(not self.View.player.isMuted())

        if self.View.player.isMuted():
            _icon = QtGui.QIcon()
            _icon.addPixmap(
                QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-volume-off.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            self.View.MainWindowView.pushButtonVolume.setIcon(_icon)
            self.View.MainWindowView.pushButtonVolume.setIconSize(QtCore.QSize(20, 20))
        
        else:
            _icon = QtGui.QIcon()
            _icon.addPixmap(
                QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-volume-high.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            self.View.MainWindowView.pushButtonVolume.setIcon(_icon)
            self.View.MainWindowView.pushButtonVolume.setIconSize(QtCore.QSize(20, 20))

    def save_playlist(self):

        self.View.get_data_receiver_window_view(
            'Ingresa el nombre de la playlist'
        )


    def playlist_data(self):

        model = self.View.MainWindowView.listViewPlaylist.model()
        row_count = model.rowCount(QtCore.QModelIndex())
        count = 0

        for file in self.Model.EnvironmentModel.attr['path']['file']:

            if self.Model.EnvironmentModel.attr['system']['os'] == 'Windows':
                __file = str(file).split('\\')

            elif self.Model.EnvironmentModel.attr['system']['os'] == 'Linux':
                __file = str(file).split('/')
                
            __file = __file.pop()



            for row in range(row_count):
                index = model.index(row, 0)
                item = model.data(index, QtCore.Qt.DisplayRole)

                if str(item) == str(__file):
                    print(file)
                    count+=1

                    self.Model.DatabaseModel.insert_data(
                        'INSERT INTO playlist (id, name, file_path) VALUES (?, ?, ?)',
                        (
                            self.Model.DatabaseModel.get_id(),
                            self.Model.EnvironmentModel.attr['data'],
                            file,
                        )
                    )
        
        if count == row_count:
            print(True)

            #print(self.View.playlist.currentMedia().canonicalUrl().toString().encode('utf-8').decode('utf-8'))

                        
        #print(self.View.playlist.currentMedia().canonicalUrl().toString().encode('utf-8').decode('utf-8'))
    
    def confirm_data(self):

        data = self.View.DataReceiverWindowView.lineEditData.text()
        print(data)

        self.Model.EnvironmentModel.attr['data'] = str(data)

        self.View.DataReceiverWindowView.destroy()

        return self.playlist_data()
    
    def get_playlist(self):

        self.Model.DatabaseModel.cursor.execute(
            'SELECT name FROM playlist GROUP BY name ORDER BY name ASC' 
        )
        model = QtGui.QStandardItemModel()
        self.View.MainWindowView.listViewPlaylists.setModel(model)


        for parameter in self.Model.DatabaseModel.cursor.fetchall():
            item = QtGui.QStandardItem(parameter[0])
            model.appendRow(item)
            #self.View.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))
        
    def get_playlists(self):
        self.View.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.View.MainWindowView.widgetPlaylist)
        self.get_playlist()
    
    def open_playlist(self):

        self.View.playlist.clear()



        for index in self.View.MainWindowView.listViewPlaylists.selectedIndexes():
            item = self.View.MainWindowView.listViewPlaylists.model().itemFromIndex(index)
            
            self.Model.DatabaseModel.cursor.execute(
                'SELECT file_path FROM playlist WHERE name = ?',
                (item.text(),) 
            )

            self.View.MainWindowView.labelPlaylist.setText(
                f'Playlist {item.text()}'
            )

            for parameter in self.Model.DatabaseModel.cursor.fetchall():
                self.View.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(parameter[0])))
        self.View.PlaylistModel.layoutChanged.emit()

            

