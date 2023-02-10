

import os


from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets,
    QtMultimedia
)


from app.views.view import View
from app.models.model import Model

import logging
import sys



class Controller(object):

    def __init__(self, Logger: logging.Logger):

        super(Controller, self).__init__()
        
        self.QApplication = QtWidgets.QApplication(sys.argv)

        self.Logger = Logger
        self.View = View(self)
        self.Model = Model(self)
    
    def execute(self):
        
        self.get_main_window_view()
        
        self.QApplication.exec_()
    
    

    def get_main_window_view(self):
        try:

            self.Logger.info(
                msg='Obteniendo la vista de la ventana principal...'
            )

            return self.View.get_main_view()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
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
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def dropEvent(self, e):
        try:
            for url in e.mimeData().urls():
                self.View.playlist.addMedia(QtMultimedia.QMediaContent(url))

            self.View.PlayerModel.layoutChanged.emit()

            # If not playing, seeking to first of newly added + play.
            if self.View.player.state() != QtMultimedia.QMediaPlayer.PlayingState:
                i = self.View.playlist.mediaCount() - len(e.mimeData().urls())
                self.View.playlist.setCurrentIndex(i)
                self.View.player.play()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def open_file(self):
        try:
            path, _ = QtWidgets.QFileDialog.getOpenFileName(
                self.View.MainWindowView,
                "Open file",
                "",
                "mp3 Audio (*.mp3);;flac Audio (*.flac);;wav Audio (*.wav);;All files (*.*)",
            )

            if path:
                self.View.playlist.addMedia(
                    QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))

            self.View.PlayerModel.layoutChanged.emit()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def open_directory(self):
        try:
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

                                    self.View.ProgressWindowView.labelProgress.setText(
                                        _path)

                                else:
                                    self.View.ProgressWindowView.labelProgress.setText(
                                        path)

                                self.View.playlist.addMedia(
                                    QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))
                                self.Model.EnvironmentModel.attr['path']['file'].append(
                                    path)

                                for index in range(len(files)):

                                    self.View.ProgressWindowView.progressBar.setValue(
                                        int(index))

                                    if index > len(files):
                                        self.View.ProgressWindowView.progressBar.setValue(
                                            100)

                                    self.View.ProgressWindowView.progressBar.setFormat(
                                        '%.02f%%' % (float(index)))
                                QtWidgets.QApplication.processEvents()

                                self.View.ProgressWindowView.progressBar.setValue(
                                    100)

                            else:
                                pass
                        self.View.ProgressWindowView.progressBar.setValue(100)

                self.View.ProgressWindowView.destroy()

            self.View.PlayerModel.layoutChanged.emit()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def update_duration(self, duration):

        try:
            self.View.MainWindowView.horizontalSliderTime.setMaximum(duration)

            if duration >= 0:
                self.View.MainWindowView.labelDuration.setText(
                    self.hhmmss(duration))

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def update_position(self, position):

        try:
            if position >= 0:
                self.View.MainWindowView.labelTime.setText(
                    self.hhmmss(position))

            # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
            self.View.MainWindowView.horizontalSliderTime.blockSignals(True)
            self.View.MainWindowView.horizontalSliderTime.setValue(position)
            self.View.MainWindowView.horizontalSliderTime.blockSignals(False)

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def playlist_selection_changed(self, ix):

        try:
            # We receive a QItemSelection from selectionChanged.
            i = ix.indexes()[0].row()
            self.View.playlist.setCurrentIndex(i)

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def playlist_position_changed(self, i):
        try:
            if i > -1:
                ix = self.View.PlayerModel.index(i)
                self.View.MainWindowView.listViewPlaylist.setCurrentIndex(ix)

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def exceptions(self, *args):
        self.Logger.warning(
            msg=f'Exception\t{args}'
        )

    def play_song(self):

        try:

            if self.View.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
                self.View.player.pause()

            else:
                self.View.player.play()

            self.meta_data_changed()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def next_song(self):

        try:

            self.meta_data_changed()
            self.View.playlist.next()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def previous_song(self):

        try:
            self.meta_data_changed()
            self.View.playlist.previous()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def meta_data_changed(self):

        try:

            if self.View.player.isMetaDataAvailable():

                try:
                    album_title = self.View.player.metaData(
                        QtMultimedia.QMediaMetaData.AlbumTitle)

                    self.Model.FileModel.attr['file']['metadata']['album'] = album_title

                    self.View.MainWindowView.labelAlbumSong.setText(
                        album_title)

                except Exception as exception:
                    self.Logger.warning(
                        msg=f'Exception\t{exception}'
                    )

                    self.View.MainWindowView.labelAlbumSong.setText('')

                try:

                    contributing_artist = self.View.player.metaData(
                        QtMultimedia.QMediaMetaData.ContributingArtist)[0]
                    album_artist = self.View.player.metaData(
                        QtMultimedia.QMediaMetaData.AlbumArtist)

                    self.View.MainWindowView.labelArtistSong.setText(
                        album_artist)

                    self.Model.FileModel.attr['file']['metadata']['contributing'] = contributing_artist
                    self.Model.FileModel.attr['file']['metadata']['artist'] = album_artist

                except Exception as exception:
                    self.Logger.warning(
                        msg=f'Exception\t{exception}'
                    )

                    self.View.MainWindowView.labelArtistSong.setText('')

                try:

                    title = self.View.player.metaData(
                        QtMultimedia.QMediaMetaData.Title)

                    self.Model.FileModel.attr['file']['metadata']['title'] = title

                    self.View.MainWindowView.labelTitleSong.setText(title)

                except Exception as exception:
                    self.Logger.warning(
                        msg=f'Exception\t{exception}'
                    )

                    self.View.MainWindowView.labelTitleSong.setText('')

                try:

                    album_cover_art = self.View.player.metaData(
                        QtMultimedia.QMediaMetaData.ThumbnailImage.encode('utf-8').decode('utf-8'))

                    if album_cover_art is not None:
                        self.View.MainWindowView.labelCoverArt.setPixmap(
                            QtGui.QPixmap(album_cover_art)
                        )

                        self.Model.FileModel.attr['file']['metadata']['cover'] = album_cover_art

                    else:
                        self.View.MainWindowView.labelCoverArt.setPixmap(
                            QtGui.QPixmap(u'app/resources/img/default/cover-art.png'))

                except Exception as exception:
                    self.Logger.warning(
                        msg=f'Exception\t{exception}'
                    )

                    self.View.MainWindowView.labelCoverArt.setPixmap(
                        QtGui.QPixmap(u'app/resources/img/default/cover-art.png'))

                try:
                    codec = self.View.player.metaData(
                        QtMultimedia.QMediaMetaData.AudioCodec)

                    self.Model.FileModel.attr['file']['metadata']['codec'] = codec
                    self.View.MainWindowView.labelCodec.setText(codec)

                except Exception as exception:
                    self.Logger.warning(
                        msg=f'Exception\t{exception}'
                    )

                    self.View.MainWindowView.labelCodec.setText('')

                try:

                    bitrate = f'{int(self.View.player.metaData(QtMultimedia.QMediaMetaData.AudioBitRate) * 0.001)}kbps'

                    self.Model.FileModel.attr['file']['metadata']['bitrate'] = bitrate

                    self.View.MainWindowView.labelBitrate.setText(
                        bitrate
                    )

                except Exception as exception:
                    self.Logger.warning(
                        msg=f'Exception\t{exception}'
                    )

                    self.View.MainWindowView.labelBitrate.setText('')

                # self.View.player.metaData(QtMultimedia.QMediaMetaData.Lyrics)

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def handle_reproduction_state(self, state):
        try:
            if self.View.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
                _icon = QtGui.QIcon()
                _icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-media-pause.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.View.MainWindowView.pushButtonPlay.setIcon(_icon)
                self.View.MainWindowView.pushButtonPlay.setIconSize(
                    QtCore.QSize(20, 20))

            else:
                _icon = QtGui.QIcon()
                _icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-media-play.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.View.MainWindowView.pushButtonPlay.setIcon(_icon)
                self.View.MainWindowView.pushButtonPlay.setIconSize(
                    QtCore.QSize(20, 20))

            self.meta_data_changed()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def handle_volume_state(self):

        try:
            self.View.player.setMuted(not self.View.player.isMuted())

            if self.View.player.isMuted():
                _icon = QtGui.QIcon()
                _icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-volume-off.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.View.MainWindowView.pushButtonVolume.setIcon(_icon)
                self.View.MainWindowView.pushButtonVolume.setIconSize(
                    QtCore.QSize(20, 20))

            else:
                _icon = QtGui.QIcon()
                _icon.addPixmap(
                    QtGui.QPixmap(u'app/resources/img/icons/24x24/cil-volume-high.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.View.MainWindowView.pushButtonVolume.setIcon(_icon)
                self.View.MainWindowView.pushButtonVolume.setIconSize(
                    QtCore.QSize(20, 20))

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def save_playlist(self):

        try:

            self.View.get_data_receiver_window_view(
                'Ingresa el nombre de la playlist'
            )

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def playlist_data(self):

        try:

            model = self.View.MainWindowView.listViewPlaylist.model()
            row_count = model.rowCount(QtCore.QModelIndex())

            self.Logger.debug(
                msg=f'Total de filas contadas : {row_count}'
            )

            count = 0

            self.Logger.debug(
                msg=f'Total contador : {count}'
            )

            self.Logger.debug(msg='Iniciando iteracion...')

            self.View.get_progress_view()

            for file in self.Model.EnvironmentModel.attr['path']['file']:

                self.Logger.debug(msg=f'{file}')

                if self.Model.EnvironmentModel.attr['system']['os'] == 'Windows':

                    self.Logger.debug(
                        msg='Iniciando separacion de caracteres...')

                    __file = str(file).split('\\')
                    self.Logger.debug(msg=f'{__file}')

                elif self.Model.EnvironmentModel.attr['system']['os'] == 'Linux':

                    self.Logger.debug(
                        msg='Iniciando separacion de caracteres...')

                    __file = str(file).split('/')
                    self.Logger.debug(msg=f'{__file}')

                __file = __file.pop()

                self.Logger.debug(msg=f'Resultado obtenido : {__file}')

                self.Logger.debug(
                    msg='Iniciando iteracion al total de filas...')

                for row in range(row_count):
                    index = model.index(row, 0)
                    item = model.data(index, QtCore.Qt.DisplayRole)

                    if str(item) == str(__file):

                        self.Logger.debug(msg=f'Archivo encontrado : {file}')

                        self.Logger.debug(
                            msg=f'Total de archivos contados : {count}')

                        self.Logger.debug(
                            msg='Iniciando la insercion de datos...')

                        self.Model.DatabaseModel.insert_data(
                            'INSERT INTO playlist (id, name, file_path) VALUES (?, ?, ?)',
                            (
                                self.Model.DatabaseModel.get_id(),
                                self.Model.EnvironmentModel.attr['data'],
                                file,
                            )
                        )

                        count += 1
                        process = (row_count - count)

                        max_length = 60
                        path_length = len(file)

                        if path_length > max_length:
                            result_length = path_length - max_length
                            _file = file[:-result_length] + '...'

                            self.View.ProgressWindowView.labelProgress.setText(
                                _file)

                        self.View.ProgressWindowView.progressBar.setValue(
                            int(count))
                        self.View.ProgressWindowView.progressBar.setFormat(
                            f'{count} Archivos insertados')

                        QtWidgets.QApplication.processEvents()

                        self.Logger.debug(msg='Insercion finalizada.')

            print(f'count       : {count}')
            print(f'row_count   : {row_count}')

            if count == row_count:
                self.View.ProgressWindowView.progressBar.setValue(100)

                self.Logger.info(
                    msg='La insercion se ha ejecutado correctamente.')
                self.View.ProgressWindowView.destroy()

                # print(self.View.playlist.currentMedia().canonicalUrl().toString().encode('utf-8').decode('utf-8'))

            # print(self.View.playlist.currentMedia().canonicalUrl().toString().encode('utf-8').decode('utf-8'))

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def confirm_data(self):

        try:

            self.Logger.debug(msg='Obteniendo dato solicitado...')

            data = self.View.DataReceiverWindowView.lineEditData.text()
            self.Logger.debug(msg=f'Dato recibido : {data}')

            self.Model.EnvironmentModel.attr['data'] = str(data)

            self.Logger.debug(msg='Destruyendo la ventana de solicitud...')

            self.View.DataReceiverWindowView.destroy()
            self.Logger.debug(msg='Ventana destruida.')

            return self.playlist_data()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def get_playlist(self):

        try:

            self.Logger.debug(msg='Obteniendo nombres de playlists...')

            self.Model.DatabaseModel.cursor.execute(
                'SELECT name FROM playlist GROUP BY name ORDER BY name ASC'
            )
            model = QtGui.QStandardItemModel()
            self.View.MainWindowView.listViewPlaylists.setModel(model)

            for parameter in self.Model.DatabaseModel.cursor.fetchall():
                item = QtGui.QStandardItem(parameter[0])

                self.Logger.debug(msg=f'Nombres encontrados : {item.text()}')
                model.appendRow(item)
                # self.View.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def get_playlists(self):

        try:
            self.View.MainWindowView.stackedWidgetContainer.setCurrentWidget(
                self.View.MainWindowView.widgetPlaylist)
            self.get_playlist()

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def open_playlist(self):

        try:

            self.View.playlist.clear()

            self.Logger.debug(msg='Iniciando iteracion de playlist...')

            for index in self.View.MainWindowView.listViewPlaylists.selectedIndexes():
                item = self.View.MainWindowView.listViewPlaylists.model().itemFromIndex(index)

                self.Model.DatabaseModel.cursor.execute(
                    'SELECT file_path FROM playlist WHERE name = ?',
                    (item.text(),)
                )
                self.Logger.debug(
                    msg=f'Seleccionando las rutas de los archivos donde el nombre sea : {item.text()}')

                self.View.MainWindowView.labelPlaylist.setText(
                    f'Playlist {item.text()}'
                )

                for parameter in self.Model.DatabaseModel.cursor.fetchall():
                    self.Logger.debug(
                        msg=f'Insertando los parametros : {parameter[0]}')

                    self.View.playlist.addMedia(QtMultimedia.QMediaContent(
                        QtCore.QUrl.fromLocalFile(parameter[0])))

            self.View.PlayerModel.layoutChanged.emit()

            self.View.get_message_view(
                title='Operacion finalizada',
                message='Playlist cargada',
                status=QtWidgets.QMessageBox.Information
            )

        except Exception as exception:
            self.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def search(self):
        data = str(None)
        data = self.View.MainWindowView.lineEdit.text()

        model = self.View.MainWindowView.listViewPlaylist.model()
        match = model.match(
            model.index(
                0, self.View.MainWindowView.listViewPlaylist.modelColumn()),
            QtCore.Qt.DisplayRole,
            data,
            hits=1,
            flags=QtCore.Qt.MatchStartsWith)

        if match:
            self.View.MainWindowView.listViewPlaylist.setCurrentIndex(match[0])
            self.View.MainWindowView.listViewPlaylist.setFocus()
            print(match[0].data())

    def add_favorite(self):
        
        title = self.View.player.metaData(QtMultimedia.QMediaMetaData.PosterUrl.encode('utf-8').decode('utf-8'))
        print(title)

        artist = self.View.player.metaData(
            QtMultimedia.QMediaMetaData.AlbumArtist)
        album = self.View.player.metaData(
            QtMultimedia.QMediaMetaData.AlbumTitle)

        self.Model.DatabaseModel.insert_data(
            query='INSERT INTO favorite (title, artist, album) VALUES (?,?,?)', parameters=(title, artist, album,))

        self.View.MainWindowView.pushButtonAddFavorite.setStyleSheet(u"QPushButton {\n"
                                                                     "    background-color: #AD3F3F;\n"
                                                                     "    border: 2px solid #222222;\n"
                                                                     "    border-radius: 20px;\n"
                                                                     "    /*border-style: outset;*/\n"
                                                                     "    padding: 5px;\n"
                                                                     "}\n")
