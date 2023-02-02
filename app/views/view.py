
from app.views.main_window_view import (
    MainWindowView
)


from app.views.progress_window_view import (
    ProgressWindowView
)

from app.views.data_receiver_window_view import (
    DataReceiverWindowView
)


from app.models.playlist_model import PlaylistModel



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


    def get_main_view(self):
        self.MainWindowView.setupUi()
        self.MainWindowView.setWindowTitle('VZPlayer')
            
        self.Controller.main_window_restore()
            
        self.MainWindowView.pushButtonClose.clicked.connect(qApp.quit)
        self.MainWindowView.pushButtonMinimize.clicked.connect(self.MainWindowView.showMinimized)
        self.MainWindowView.pushButtonRestore.clicked.connect(lambda : self.Controller.main_window_status_restore())

        self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetLibrary)
            




        self.player = QMediaPlayer()

        self.player.error.connect(self.Controller.exceptions)
        self.player.play()

        # Setup the playlist.
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)



        self.MainWindowView.horizontalSliderVolume.setValue(50)
        self.MainWindowView.horizontalSliderVolume.valueChanged.connect(self.player.setVolume)
        self.MainWindowView.pushButtonVolume.clicked.connect(self.Controller.handle_volume_state)



        self.MainWindowView.pushButtonPlay.pressed.connect(self.Controller.play_song)
        self.MainWindowView.pushButtonPrevious.pressed.connect(self.Controller.previous_song)
        self.MainWindowView.pushButtonNext.pressed.connect(self.Controller.next_song)

        self.PlaylistModel = PlaylistModel(self.playlist)
        self.MainWindowView.listViewPlaylist.setModel(self.PlaylistModel)
        #self.MainWindowView.listViewPlaylist.doubleClicked.connect(self.player.play)
        self.MainWindowView.listViewPlaylist.doubleClicked.connect(self.Controller.play_song)

        #self.MainWindowView.listViewPlaylist.setDragEnabled(True)

        #self.MainWindowView.listViewPlaylist.setAcceptDrops(True)
        #self.MainWindowView.listViewPlaylist.setDropIndicatorShown(True)
        

        self.MainWindowView.listViewPlaylist.setDragDropMode(QAbstractItemView.InternalMove)
        self.MainWindowView.listViewPlaylist.setDefaultDropAction(Qt.MoveAction)
        self.MainWindowView.listViewPlaylist.setAcceptDrops(True)

        self.playlist.currentIndexChanged.connect(self.Controller.playlist_position_changed)

        selection_model = self.MainWindowView.listViewPlaylist.selectionModel()
        selection_model.selectionChanged.connect(self.Controller.playlist_selection_changed)

        self.player.durationChanged.connect(self.Controller.update_duration)
        self.player.positionChanged.connect(self.Controller.update_position)


        self.MainWindowView.horizontalSliderTime.valueChanged.connect(self.player.setPosition)

        self.MainWindowView.pushButtonAddFile.clicked.connect(self.Controller.open_file)
        self.MainWindowView.pushButtonAddDirectory.clicked.connect(self.Controller.open_directory)

        self.MainWindowView.pushButton.clicked.connect(self.Controller.save_playlist)

        self.player.stateChanged.connect(self.Controller.handle_reproduction_state)
        self.player.metaDataChanged.connect(self.Controller.meta_data_changed)

        self.MainWindowView.pushButtonFavorites.clicked.connect(lambda : self.MainWindowView.stackedWidgetContainer.setCurrentWidget(self.MainWindowView.widgetInterest))
        self.MainWindowView.pushButtonPlaylists.clicked.connect(self.Controller.get_playlists)
        self.Controller.get_playlist()

        self.MainWindowView.listViewPlaylists.doubleClicked.connect(self.Controller.open_playlist)
        self.MainWindowView.listViewPlaylists.setEditTriggers(QAbstractItemView.NoEditTriggers)
        return self.MainWindowView.show()


    def get_progress_view(self):
        self.ProgressWindowView.setupUi()
        self.ProgressWindowView.setWindowTitle('VZPlayer')


        return self.ProgressWindowView.show()

    def get_data_receiver_window_view(self, title : str):
        self.DataReceiverWindowView.setupUi()
        self.DataReceiverWindowView.setWindowTitle('VZPlayer')
        self.DataReceiverWindowView.set_title(title)


        self.DataReceiverWindowView.pushButtonConfirm.clicked.connect(self.Controller.confirm_data)


        return self.DataReceiverWindowView.show()