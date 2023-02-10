
from app.views.menu import (
    MainWindowView
)

from app.views.progress import (
    ProgressWindowView
)

from app.views.data_receiver import (
    DataReceiverWindowView
)

from app.views.message import (
    MessageWindowView
)


from app.models.playlist import PlayerModel


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


class View(object):

    def __init__(self, Controller):

        super(View, self).__init__()

        self.Controller = Controller

        self.MainWindowView = MainWindowView(self.Controller)
        self.ProgressWindowView = ProgressWindowView(self.Controller)
        self.DataReceiverWindowView = DataReceiverWindowView(self.Controller)
        self.MessageWindowView = MessageWindowView()

    def get_main_view(self):
        try:
            self.Controller.Logger.debug(
                msg='Iniciando los componentes graficos de la ventana principal...')

            self.MainWindowView.setupUi()

            self.Controller.Logger.info(
                msg='Los componentes graficos han sido instanciados correctamente.')

            self.Controller.Logger.debug(
                msg='Iniciando las propiedades de la ventana principal...')

            self.MainWindowView.setWindowTitle('VZPlayer')

            self.MainWindowView.stackedWidgetContainer.setCurrentWidget(
                self.MainWindowView.widgetMenu)

            self.MainWindowView.lineEditSearcher.setPlaceholderText(
                'Busca algo')
            '''self.MainWindowView.lineEditSearcher.textChanged.connect(
                self.Controller.search)'''

            self.MainWindowView.pushButtonSearch.clicked.connect(
                self.Controller.search)

            self.MainWindowView.pushButtonAddFavorite.clicked.connect(
                self.Controller.add_favorite)

            self.player = QMediaPlayer()

            self.player.error.connect(self.Controller.exceptions)
            self.player.play()

            # Setup the playlist.
            self.playlist = QMediaPlaylist()
            self.player.setPlaylist(self.playlist)

            self.player.volumeChanged.connect(
                self.MainWindowView.horizontalSliderVolume.setValue)
            self.MainWindowView.horizontalSliderVolume.setValue(5)
            self.MainWindowView.horizontalSliderVolume.valueChanged.connect(
                self.player.setVolume)
            self.MainWindowView.pushButtonVolume.clicked.connect(
                self.Controller.handle_volume_state)

            self.MainWindowView.pushButtonScanner.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetMenu))

            self.MainWindowView.pushButtonMenu.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetMenu))
            self.MainWindowView.pushButtonMenu_2.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetMenu))
            self.MainWindowView.pushButtonMenu_3.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetMenu))
            self.MainWindowView.pushButtonMenu_4.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetMenu))
            self.MainWindowView.pushButtonMenu_5.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetMenu))

            self.MainWindowView.pushButtonSong.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetPlayer))
            self.MainWindowView.pushButtonSettings.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetSettings))

            self.MainWindowView.pushButtonPlay.pressed.connect(
                self.Controller.play_song)
            self.MainWindowView.pushButtonPrevious.pressed.connect(
                self.Controller.previous_song)
            self.MainWindowView.pushButtonNext.pressed.connect(
                self.Controller.next_song)

            self.PlayerModel = PlayerModel(self.playlist)
            self.MainWindowView.listViewPlaylist.setModel(self.PlayerModel)
            self.MainWindowView.listViewPlaylist.doubleClicked.connect(
                self.Controller.play_song)

            self.MainWindowView.listViewPlaylist.setDragDropMode(
                QAbstractItemView.InternalMove)
            self.MainWindowView.listViewPlaylist.setDefaultDropAction(
                Qt.MoveAction)
            self.MainWindowView.listViewPlaylist.setAcceptDrops(True)

            self.playlist.currentIndexChanged.connect(
                self.Controller.playlist_position_changed)

            selection_model = self.MainWindowView.listViewPlaylist.selectionModel()
            selection_model.selectionChanged.connect(
                self.Controller.playlist_selection_changed)

            self.player.durationChanged.connect(
                self.Controller.update_duration)
            self.player.positionChanged.connect(
                self.Controller.update_position)

            self.MainWindowView.horizontalSliderTime.valueChanged.connect(
                self.player.setPosition)

            self.MainWindowView.pushButtonAddFile.clicked.connect(
                self.Controller.open_file)
            self.MainWindowView.pushButtonAddDirectory.clicked.connect(
                self.Controller.open_directory)

            self.MainWindowView.pushButtonSaveActualPlaylist.clicked.connect(
                self.Controller.save_playlist)

            self.player.stateChanged.connect(
                self.Controller.handle_reproduction_state)
            self.player.metaDataChanged.connect(
                self.Controller.meta_data_changed)

            self.MainWindowView.pushButtonFavorites.clicked.connect(
                lambda: self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetInterest))
            self.MainWindowView.pushButtonPlaylists.clicked.connect(
                self.Controller.get_playlists)
            self.Controller.get_playlist()

            self.MainWindowView.listViewPlaylists.doubleClicked.connect(
                self.Controller.open_playlist)
            self.MainWindowView.listViewPlaylists.setEditTriggers(
                QAbstractItemView.NoEditTriggers)

            self.Controller.Logger.info(
                msg='Las propiedades han sido instanciadas en la ventana principal.')

            self.Controller.Logger.debug(msg='Iniciando interfaz grafica...')

            return self.MainWindowView.show()

        except Exception as exception:
            self.Controller.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def get_progress_view(self):

        try:

            self.Controller.Logger.debug(
                msg='Iniciando los componentes graficos de la ventana de progreso...')
            self.ProgressWindowView.setupUi()

            self.Controller.Logger.info(
                msg='Los componentes graficos han sido instanciados correctamente.')

            self.Controller.Logger.debug(
                msg='Iniciando las propiedades de la ventana de progreso...')
            self.ProgressWindowView.setWindowTitle('VZPlayer')
            self.ProgressWindowView.setMaximumSize(800, 150)
            self.ProgressWindowView.setMinimumSize(800, 150)
            self.Controller.Logger.info(
                msg='Las propiedades han sido instanciadas en la ventana de progreso.')

            self.Controller.Logger.debug(msg='Iniciando interfaz grafica...')

            return self.ProgressWindowView.show()

        except Exception as exception:
            self.Controller.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def get_message_view(self, title: str, message: str, status: str):
        try:
            '''
            STATUS >
                        Question
                        Information
                        Warning
                        Critical
            '''

            self.Controller.Logger.debug(
                msg='Iniciando las propiedades de la ventana de mensaje...')
            self.MessageWindowView.set_title(title)
            self.MessageWindowView.set_status(status)
            self.MessageWindowView.set_message(message)
            self.Controller.Logger.info(
                msg='Las propiedades han sido instanciadas en la ventana de mensaje.')

            self.Controller.Logger.debug(
                msg='Iniciando los componentes graficos de la ventana de mensaje...')
            self.MessageWindowView.setupUi()
            self.Controller.Logger.info(
                msg='Los componentes graficos han sido instanciados correctamente.')

            self.Controller.Logger.debug(msg='Iniciando interfaz grafica...')

            return self.MessageWindowView.show()

        except Exception as exception:
            self.Controller.Logger.warning(
                msg=f'Exception\t{exception}'
            )

    def get_data_receiver_window_view(self, title: str):

        try:

            self.Controller.Logger.debug(
                msg='Iniciando los componentes graficos de la ventana de solicitud...')
            self.DataReceiverWindowView.setupUi()
            self.Controller.Logger.info(
                msg='Los componentes graficos han sido instanciados correctamente.')

            self.Controller.Logger.debug(
                msg='Iniciando las propiedades de la ventana de solicitud...')
            self.DataReceiverWindowView.setWindowTitle('VZPlayer')
            self.DataReceiverWindowView.set_title(title)
            self.Controller.Logger.info(
                msg='Las propiedades han sido instanciadas en la ventana de solicitud.')

            self.DataReceiverWindowView.pushButtonConfirm.clicked.connect(
                self.Controller.confirm_data)

            self.Controller.Logger.debug(msg='Iniciando interfaz grafica...')

            return self.DataReceiverWindowView.show()

        except Exception as exception:
            self.Controller.Logger.warning(
                msg=f'Exception\t{exception}'
            )
