from PyQt5 import (
    QtWidgets,
    QtCore,
    QtGui,
    QtMultimedia
)
from app.models.modules import (
    get_path,
    get_logger,
    clear_project
    
)

from app.views.view import View
from app.models.model import Model

import logging
import os
import sys



class Controller(object):
    
    
    def __init__(self, logger : logging.Logger, **struct):
        super(Controller, self).__init__()
        
        self.logger = logger


        self.QApplication = QtWidgets.QApplication(sys.argv)

        
        self.Model = Model(self, **struct)

        self.View = View(self)

    
    
    def get_main_view(self):
        
        try:
        
            self.View.get_main_view()
            
            return sys.exit(self.QApplication.exec_())

        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )




    def window_title_bar_restore(self, component):
        try:
            def dobleClickMaximizeRestore(event):
                if event.type() == QtCore.QEvent.MouseButtonDblClick:
                    QtCore.QTimer.singleShot(8, lambda: self.window_status_restore(component))
                    
            component.frameWindowTitleBar.mouseDoubleClickEvent = dobleClickMaximizeRestore

        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )




    def window_status_restore(self, component):
        try:
        
            def window_maximize():
                return component.showMaximized()

            def window_minimize():
                return component.showNormal()
            
            if component.windowState() == QtCore.Qt.WindowState.WindowNoState:
                
                window_maximize()
                
                component.pushButtonRestoreWindow.setToolTip('Restore')
                
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap('app/resources/img/icons/24x24/cil-window-restore.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                
                component.pushButtonRestoreWindow.setIcon(icon)
                component.pushButtonRestoreWindow.setIconSize(QtCore.QSize(20, 20))
            
            else:
                
                window_minimize()
                
                component.pushButtonRestoreWindow.setToolTip('Maximize')
                
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-window-maximize.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                
                component.pushButtonRestoreWindow.setIcon(icon)
                component.pushButtonRestoreWindow.setIconSize(QtCore.QSize(20, 20))



        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )






    def hhmmss(self, ms):
        # s = 1000
        # m = 60000
        # h = 360000

        s = round(ms / 1000)

        m, s = divmod(s, 60)
        h, m = divmod(m, 60)

        return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


    def dragEnterEvent(self, e):

        try:
            if e.mimeData().hasUrls():
                e.acceptProposedAction()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )


    def dropEvent(self, e):
        try:
            for url in e.mimeData().urls():
                self.View.QMediaPlaylist.addMedia(QtMultimedia.QMediaContent(url))

            self.View.PlayerModel.layoutChanged.emit()

            # If not playing, seeking to first of newly added + play.
            if self.View.QMediaPlayer.state() != QtMultimedia.QMediaPlayer.PlayingState:
                i = self.View.QMediaPlaylist.mediaCount() - len(e.mimeData().urls())
                self.View.QMediaPlaylist.setCurrentIndex(i)
                self.View.QMediaPlayer.play()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )


    def set_volume_state(self):

        try:
            self.View.QMediaPlayer.setMuted(not self.View.QMediaPlayer.isMuted())

            if self.View.QMediaPlayer.isMuted():
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-volume-off.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.View.MainView.pushButtonVolume.setIcon(icon)
                self.View.MainView.pushButtonVolume.setIconSize(
                    QtCore.QSize(20, 20))

            else:
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-volume-high.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.View.MainView.pushButtonVolume.setIcon(icon)
                self.View.MainView.pushButtonVolume.setIconSize(
                    QtCore.QSize(20, 20))


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )


    def play_song(self):

        try:

            if self.View.QMediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
                self.View.QMediaPlayer.pause()

            else:
                self.View.QMediaPlayer.play()

            self.get_metadata()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def next_song(self):

        try:

            self.get_metadata()
            self.View.QMediaPlaylist.next()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def previous_song(self):

        try:
            self.get_metadata()
            self.View.QMediaPlaylist.previous()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def get_metadata(self):

        try:

            if self.View.QMediaPlayer.isMetaDataAvailable():

                try:
                    album_title = self.View.QMediaPlayer.metaData(QtMultimedia.QMediaMetaData.AlbumTitle)
                    self.View.MainView.labelAlbum.setText(album_title)

                except Exception as exception:

                    self.View.MainView.labelAlbum.setText('')

                try:

                    contributing_artist = self.View.QMediaPlayer.metaData(QtMultimedia.QMediaMetaData.ContributingArtist)[0]
                    album_artist = self.View.QMediaPlayer.metaData(QtMultimedia.QMediaMetaData.AlbumArtist)

                    self.View.MainView.labelArtist.setText(album_artist)

                except Exception as exception:

                    self.View.MainView.labelArtist.setText('')

                try:

                    title = self.View.QMediaPlayer.metaData(QtMultimedia.QMediaMetaData.Title)

                    self.View.MainView.labelTitle.setText(title)

                except Exception as exception:
                    self.View.MainView.labelTitle.setText('')

                try:

                    album_cover_art = self.View.QMediaPlayer.metaData(QtMultimedia.QMediaMetaData.ThumbnailImage.encode('utf-8').decode('utf-8'))

                    if album_cover_art is not None:
                        self.View.MainView.labelCoverArt.setPixmap(QtGui.QPixmap(album_cover_art))

                    else:
                        self.View.MainView.labelCoverArt.setPixmap(QtGui.QPixmap(u'app/resources/img/default/cover-art-1.png'))

                except Exception as exception:
                    self.View.MainView.labelCoverArt.setPixmap(QtGui.QPixmap(u'app/resources/img/default/cover-art-1.png'))

                try:
                    codec = self.View.QMediaPlayer.metaData(QtMultimedia.QMediaMetaData.AudioCodec)

                    self.View.MainView.labelCodec.setText(codec)

                except Exception as exception:

                    self.View.MainView.labelCodec.setText('')

                try:

                    bitrate = f'{int(self.View.QMediaPlayer.metaData(QtMultimedia.QMediaMetaData.AudioBitRate) * 0.001)}kbps'

                    self.View.MainView.labelBitrate.setText(bitrate)

                except Exception as exception:
                    self.View.MainView.labelBitrate.setText('')

                # self.View.QMediaPlayer.metaData(QtMultimedia.QMediaMetaData.Lyrics)


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )


    def open_file(self):
        try:
            path, _ = QtWidgets.QFileDialog.getOpenFileName(
                self.View.MainView,
                "Open file",
                "",
                "mp3 Audio (*.mp3);;FLAC Audio (*.flac);;WAV Audio (*.wav);;All files (*.*)",
            )
            path = get_path(path)
            
            if path:
                self.View.QMediaPlaylist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))

            self.View.PlayerModel.layoutChanged.emit()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def open_directory(self):
        
        
        data = {
            'object' : {
                
                'name' : [],
                'path' : {
                    'directory' : [],
                    'file' : []
                }
            },
            'playlist' : []
        }
        
        try:
            self.View.QMediaPlaylist.clear()

            path = QtWidgets.QFileDialog.getExistingDirectory(self.View.MainView)

            if path:
                self.View.get_progress_view()
                
                for root, directories, files in os.walk(path):

                    root = get_path(root)

                    for file in files:
                        if file[-4:] == 'flac' or file[-3:] == 'mp3' or file[-3:] == 'm4a' or file[-3:] == 'wav':

                            path = get_path(os.path.join(root, file))

                            if os.path.exists(path):
                                
                                # Aqui
                                
                                data['object']['name'].append(os.path.dirname(path))

                                data['object']['path']['directory'].append(path)
                                data['object']['path']['file'].append(file)



                                max_length = 60
                                path_length = len(path)

                                if path_length > max_length:

                                    result_length = path_length - max_length
                                    path_display = path[:-result_length] + '...'

                                    self.View.ProgressView.labelProgress.setText(path_display)

                                else:
                                    self.View.ProgressView.labelProgress.setText(path)

                                self.View.QMediaPlaylist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))


                                for index in range(len(files)):

                                    self.View.ProgressView.progressBar.setValue(int(index))

                                    if index > len(files):
                                        self.View.ProgressView.progressBar.setValue(100)

                                    self.View.ProgressView.progressBar.setFormat('%.02f%%' % (float(index)))
                                    
                                QtWidgets.QApplication.processEvents()

                                self.View.ProgressView.progressBar.setValue(100)

                            else:
                                pass
                        self.View.ProgressView.progressBar.setValue(100)

                self.View.ProgressView.destroy()
                
            data['object']['name'] = list(dict.fromkeys(data['object']['name']))
            data['object']['path']['directory'] = list(dict.fromkeys(data['object']['path']['directory']))
            data['object']['path']['file'] = list(dict.fromkeys(data['object']['path']['file']))
            
            
            self.Model.struct.update(data)
            
            print(self.Model.struct)

            self.View.PlayerModel.layoutChanged.emit()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def set_duration_update(self, duration):

        try:
            self.View.MainView.horizontalSliderTime.setMaximum(duration)

            if duration >= 0:
                self.View.MainView.labelDurationTime.setText(self.hhmmss(duration))


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def set_position_update(self, position):

        try:
            if position >= 0:
                self.View.MainView.labelCurrentTime.setText(self.hhmmss(position))

            # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
            self.View.MainView.horizontalSliderTime.blockSignals(True)
            self.View.MainView.horizontalSliderTime.setValue(position)
            self.View.MainView.horizontalSliderTime.blockSignals(False)


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def set_playlist_selection(self, ix):

        try:
            # We receive a QItemSelection from selectionChanged.
            i = ix.indexes()[0].row()
            self.View.QMediaPlaylist.setCurrentIndex(i)


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def set_playlist_position(self, i):
        try:
            if i > -1:
                ix = self.View.PlayerModel.index(i)
                self.View.MainView.listViewPlayer.setCurrentIndex(ix)


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def exceptions(self, *args):
        print(args)


    def set_reproduction_state(self, state):
        try:
            if self.View.QMediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-media-pause.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.View.MainView.pushButtonPlay.setIcon(icon)
                self.View.MainView.pushButtonPlay.setIconSize(
                    QtCore.QSize(20, 20))

            else:
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-media-play.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.View.MainView.pushButtonPlay.setIcon(icon)
                self.View.MainView.pushButtonPlay.setIconSize(
                    QtCore.QSize(20, 20))

            self.get_metadata()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )



    def save_playlist(self):

        try:

            self.View.get_data_receiver_view(
                title = 'Ingresa el nombre de la playlist'
            )


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )



    def get_playlist_data(self, playlist_name : str):

        try:

            model = self.View.MainView.listViewPlayer.model()
            row_count = model.rowCount(QtCore.QModelIndex())


            count = 0

            self.View.get_progress_view()

            for file in self.Model.struct['object']['path']['directory']:

                file_name = os.path.basename(file)

                for row in range(row_count):
                    index = model.index(row, 0)
                    item = model.data(index, QtCore.Qt.DisplayRole)

                    if str(item) == str(file_name):
                        
                        playlist_id = self.Model.Database.get_id()
                        playlist_file_path = file
                        playlist_file_name = file_name

                        
                        self.Model.Database.insert_data(
                            query = 'INSERT INTO playlist (playlist_id, playlist_name, playlist_file_path, playlist_file_name) VALUES (?, ?, ?, ?)',
                            parameters = (
                                playlist_id,
                                playlist_name,
                                playlist_file_path,
                                playlist_file_name
                            )
                        )

                        count += 1
                        process = (row_count - count)

                        max_length = 60
                        path_length = len(file)

                        if path_length > max_length:
                            result_length = path_length - max_length
                            self.View.ProgressView.labelProgress.setText(file[:-result_length] + '...')

                        self.View.ProgressView.progressBar.setMaximum(row_count)
                        self.View.ProgressView.progressBar.setValue(int(count))
                        self.View.ProgressView.progressBar.setFormat(f'{count} Archivos insertados')

                        QtWidgets.QApplication.processEvents()


            print(f'count       : {count}')
            print(f'row_count   : {row_count}')

            if count == row_count:
                self.View.ProgressView.progressBar.setValue(100)
                self.View.ProgressView.destroy()

                # print(self.View.playlist.currentMedia().canonicalUrl().toString().encode('utf-8').decode('utf-8'))

            # print(self.View.playlist.currentMedia().canonicalUrl().toString().encode('utf-8').decode('utf-8'))


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )


    def set_confirmation(self):

        try:

            playlist = self.View.DataReceiverView.lineEditData.text()
            
            self.get_playlist_data(playlist)
            self.get_playlist()

            

            return self.View.DataReceiverView.destroy()


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )




    def get_playlist(self):

        try:

            self.Model.Database.cursor.execute(
                'SELECT playlist_name FROM playlist GROUP BY playlist_name ORDER BY playlist_name ASC'
            )
            model = QtGui.QStandardItemModel()
            self.View.MainView.listViewPlaylists.setModel(model)

            for parameter in self.Model.Database.cursor.fetchall():
                item = QtGui.QStandardItem(parameter[0])
                model.appendRow(item)


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )



    def open_playlist(self):

        try:

            self.View.QMediaPlaylist.clear()


            for index in self.View.MainView.listViewPlaylists.selectedIndexes():
                item = self.View.MainView.listViewPlaylists.model().itemFromIndex(index)

                self.Model.Database.cursor.execute(
                    'SELECT playlist_file_path FROM playlist WHERE playlist_name = ?',
                    (item.text(),)
                )

                #self.View.MainView.labelPl.setText(f'Playlist {item.text()}')
                

                for parameter in self.Model.Database.cursor.fetchall():

                    self.View.QMediaPlaylist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(parameter[0])))

            self.View.PlayerModel.layoutChanged.emit()

            print(True)


        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def search(self):
        try:
            data = str(None)
            data = self.View.MainView.lineEdit.text()

            model = self.View.MainView.listViewPlaylist.model()
            match = model.match(
                model.index(
                    0, self.View.MainView.listViewPlaylist.modelColumn()),
                QtCore.Qt.DisplayRole,
                data,
                hits=1,
                flags=QtCore.Qt.MatchStartsWith)

            if match:
                self.View.MainView.listViewPlaylist.setCurrentIndex(match[0])
                self.View.MainView.listViewPlaylist.setFocus()
                print(match[0].data())

        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

    def add_favorite(self):
        try:
            title = self.View.player.metaData(QtMultimedia.QMediaMetaData.PosterUrl.encode('utf-8').decode('utf-8'))
            print(title)

            artist = self.View.player.metaData(
                QtMultimedia.QMediaMetaData.AlbumArtist)
            album = self.View.player.metaData(
                QtMultimedia.QMediaMetaData.AlbumTitle)

            self.Model.Database.insert_data(
                query='INSERT INTO favorite (title, artist, album) VALUES (?,?,?)', parameters=(title, artist, album,))

            self.View.MainView.pushButtonAddFavorite.setStyleSheet(u"QPushButton {\n"
                                                                        "    background-color: #AD3F3F;\n"
                                                                        "    border: 2px solid #222222;\n"
                                                                        "    border-radius: 20px;\n"
                                                                        "    /*border-style: outset;*/\n"
                                                                        "    padding: 5px;\n"
                                                                        "}\n")
        except Exception as exception:
            
            self.logger.critical(
                msg = f'Exception : {exception}'
            )

