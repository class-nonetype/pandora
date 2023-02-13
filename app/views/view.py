from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets,
    QtMultimedia
)
    
from app.views.modules import (
    MainView,
    ProgressView,
    DataReceiverView
)

from app.models.modules import PlayerModel

scrollbar_stylesheet = '''
    QScrollArea {
        border: none;
    }

    QScrollBar {
        background: transparent;
    }

    QScrollBar:horizontal {
        height: 13px;
    }

    QScrollBar:vertical {
        width: 13px;
    }

    QScrollBar::handle {
        background: #61364F;
    }

    QScrollBar::handle:horizontal {
        height: 25px;
        min-width: 10px;
    }

    QScrollBar::handle:vertical {
        width: 25px;
        min-height: 10px;
    }

    QScrollBar::add-line {
        border: none;
        background: none;
    }

    QScrollBar::sub-line {
        border: none;
        background: none;
    }
'''


class View(object):

    def __init__(self, Controller):

        super(View, self).__init__()

        self.Controller = Controller

        self.MainView = MainView(self.Controller)
        self.ProgressView = ProgressView()
        self.DataReceiverView = DataReceiverView()

    def get_main_view(self):

        self.MainView.setupUi()
        
        # Window titlebar
        self.Controller.window_title_bar_restore(self.MainView)


        self.MainView.pushButtonCloseWindow.clicked.connect(
                QtWidgets.qApp.quit)

        self.MainView.pushButtonMinimizeWindow.clicked.connect(
                self.MainView.showMinimized)

        self.MainView.pushButtonRestoreWindow.clicked.connect(
                lambda: self.Controller.window_status_restore(self.MainView))



        # Get library module
        self.get_library_module()
        
        # Library functions
        self.MainView.pushButtonPlaylists.clicked.connect(self.get_playlists_module)
        self.MainView.pushButtonAddFile.clicked.connect(self.Controller.open_file)
        self.MainView.pushButtonAddDirectory.clicked.connect(self.Controller.open_directory)
        self.MainView.pushButtonFavorites.clicked.connect(self.get_favorites_module)
        
        
        # Setup the media player
        self.QMediaPlayer = QtMultimedia.QMediaPlayer()
        self.QMediaPlayer.error.connect(self.Controller.exceptions)
        self.QMediaPlayer.play()
        
        
        # Setup the media playlist.
        self.QMediaPlaylist = QtMultimedia.QMediaPlaylist()
        
        self.QMediaPlayer.setPlaylist(self.QMediaPlaylist)
        self.QMediaPlayer.volumeChanged.connect(self.MainView.horizontalSliderVolume.setValue)
        
        self.MainView.horizontalSliderVolume.setValue(100)

        self.MainView.horizontalSliderVolume.valueChanged.connect(self.QMediaPlayer.setVolume)
        self.MainView.pushButtonVolume.clicked.connect(self.Controller.set_volume_state)


        # Player module
        self.MainView.pushButtonPlay.pressed.connect(self.Controller.play_song)
        self.MainView.pushButtonPrevious.pressed.connect(self.Controller.previous_song)
        self.MainView.pushButtonNext.pressed.connect(self.Controller.next_song)


        self.PlayerModel = PlayerModel(self.QMediaPlaylist)
        self.MainView.listViewPlayer.setModel(self.PlayerModel)
        self.MainView.listViewPlayer.doubleClicked.connect(self.Controller.play_song)
        self.MainView.listViewPlayer.verticalScrollBar().setStyleSheet(scrollbar_stylesheet)
        self.MainView.listViewPlayer.horizontalScrollBar().setStyleSheet(scrollbar_stylesheet)


        self.MainView.listViewPlayer.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.MainView.listViewPlayer.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.MainView.listViewPlayer.setAcceptDrops(True)

        self.QMediaPlaylist.currentIndexChanged.connect(self.Controller.set_playlist_position)

        selection_model = self.MainView.listViewPlayer.selectionModel()
        selection_model.selectionChanged.connect(self.Controller.set_playlist_selection)

        self.QMediaPlayer.durationChanged.connect(self.Controller.set_duration_update)
        self.QMediaPlayer.positionChanged.connect(self.Controller.set_position_update)

        self.MainView.horizontalSliderTime.valueChanged.connect(self.QMediaPlayer.setPosition)



        self.MainView.pushButtonSaveActualPlaylist.clicked.connect(self.Controller.save_playlist)

        self.QMediaPlayer.stateChanged.connect(self.Controller.set_reproduction_state)
        self.QMediaPlayer.metaDataChanged.connect(self.Controller.get_metadata)
        

        
        self.MainView.listViewPlaylists.doubleClicked.connect(self.Controller.open_playlist)
        self.MainView.listViewPlaylists.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.MainView.listViewPlaylists.setItemAlignment(QtCore.Qt.AlignLeft)
        
        
















        
        self.MainView.radioButtonDarkMode.toggled.connect(self.mode)
        self.MainView.radioButtonDarkMode.setChecked(True)
        
        self.MainView.radioButtonLightMode.toggled.connect(self.mode)
        
        
        
        self.MainView.pushButtonBack.clicked.connect(self.get_library_module)
        self.MainView.pushButtonSettings.clicked.connect(self.get_settings_module)
        self.MainView.pushButtonPlayer.clicked.connect(self.get_player_module)
        self.MainView.pushButtonPlaylistPlayer.clicked.connect(self.get_playlists_module)
        

        return self.MainView.show()
    
    
    def get_progress_view(self):
        
        self.ProgressView.setupUi()
        
        return self.ProgressView.show()


    def get_data_receiver_view(self, title: str):

        try:

            self.DataReceiverView.setupUi()

            self.DataReceiverView.setWindowTitle('Pandora : Data receiver')
            self.DataReceiverView.set_title(title)

            self.DataReceiverView.pushButtonConfirm.clicked.connect(self.Controller.set_confirmation)

            return self.DataReceiverView.show()

        except Exception as exception:
            print(exception)














    
    
    def get_library_module(self):
        
        self.MainView.pushButtonBack.setHidden(True)
        self.MainView.pushButtonSettings.setHidden(False)
        self.MainView.pushButtonPlayer.setHidden(False)
        self.MainView.pushButtonPlaylistPlayer.setHidden(True)
        
        self.MainView.stackedWidgetContent.setCurrentWidget(self.MainView.libraryWidget)

    
    def get_player_module(self):

        self.MainView.pushButtonBack.setHidden(False)
        self.MainView.pushButtonSettings.setHidden(True)
        self.MainView.pushButtonPlayer.setHidden(True)
        self.MainView.pushButtonPlaylistPlayer.setHidden(False)
        
        return self.MainView.stackedWidgetContent.setCurrentWidget(self.MainView.playerWidget)
    
    
    def get_settings_module(self):
        self.MainView.pushButtonBack.setHidden(False)
        self.MainView.pushButtonSettings.setHidden(True)
        self.MainView.pushButtonPlayer.setHidden(True)
        self.MainView.pushButtonPlaylistPlayer.setHidden(True)
        
        return self.MainView.stackedWidgetContent.setCurrentWidget(self.MainView.settingsWidget)
    

    def get_playlists_module(self):
        try:
            self.Controller.get_playlist()
        except Exception as exception:
            print(exception)

        self.MainView.pushButtonBack.setHidden(False)
        self.MainView.pushButtonSettings.setHidden(True)
        self.MainView.pushButtonPlayer.setHidden(False)
        self.MainView.pushButtonPlaylistPlayer.setHidden(True)
        
        return self.MainView.stackedWidgetContent.setCurrentWidget(self.MainView.playlistsWidget)


    def get_favorites_module(self):
        self.MainView.pushButtonBack.setHidden(False)
        self.MainView.pushButtonSettings.setHidden(True)
        self.MainView.pushButtonPlayer.setHidden(False)
        self.MainView.pushButtonPlaylistPlayer.setHidden(True)
        
        return self.MainView.stackedWidgetContent.setCurrentWidget(self.MainView.favoritesWidget)



    def mode(self):
        if self.MainView.radioButtonLightMode.isChecked():
            
            self.MainView.frameContainer.setStyleSheet('QFrame { background-color: #FFFFFF;}')


            self.MainView.labelWindowTitleBar.setStyleSheet("QLabel {\n"
                                                "    font : 77 15pt \"Microsoft JhengHei UI\";\n"
                                                "    color : #46355e;\n"
                                                "    border-radius : 0px;\n"
                                                "    text-align : left;\n"
                                                "    padding-left: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "QLabel::hover {\n"
                                                "    color : #4F6FA0;\n"
                                                "}\n"
                                                "")



            
            self.MainView.pushButtonBack.setStyleSheet("QPushButton{\n"
                                          "    background-color: #46355e;\n"
                                          "    border-radius : 14px;\n"
                                          "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding : 10px;\n"
                                          "\n"
                                          "    text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #252525;\n"
                                          "}")

            self.MainView.pushButtonSettings.setStyleSheet("QPushButton{\n"
                                          "    background-color: #46355e;\n"
                                          "    border-radius : 14px;\n"
                                          "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding : 10px;\n"
                                          "\n"
                                          "    text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #252525;\n"
                                          "}")

            self.MainView.pushButtonPlayer.setStyleSheet("QPushButton{\n"
                                          "    background-color: #46355e;\n"
                                          "    border-radius : 14px;\n"
                                          "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding : 10px;\n"
                                          "\n"
                                          "    text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #252525;\n"
                                          "}")

            self.MainView.pushButtonPlaylistPlayer.setStyleSheet("QPushButton{\n"
                                          "    background-color: #46355e;\n"
                                          "    border-radius : 14px;\n"
                                          "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding : 10px;\n"
                                          "\n"
                                          "    text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #252525;\n"
                                          "}")



            # Library
            self.MainView.labelLibraryWidgetTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #46355e;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #4F6FA0;\n"
                                                  "}\n"
                                                  "")
            
            self.MainView.labelLibraryFileTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #46355e;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #4F6FA0;\n"
                                                  "}\n"
                                                  "")

            self.MainView.labelLibraryMusicTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #46355e;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #4F6FA0;\n"
                                                  "}\n"
                                                  "")
            
            
            self.MainView.pushButtonAddDirectory.setStyleSheet("QPushButton{\n"
                                               "    background-color: #5F3E77;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #46355e;\n"
                                               "}")
            
            self.MainView.pushButtonAddFile.setStyleSheet("QPushButton{\n"
                                               "    background-color: #5F3E77;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #46355e;\n"
                                               "}")
            
            self.MainView.pushButtonAddPath.setStyleSheet("QPushButton{\n"
                                               "    background-color: #5F3E77;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #46355e;\n"
                                               "}")
            
            self.MainView.pushButtonPlaylists.setStyleSheet("QPushButton{\n"
                                               "    background-color: #5F3E77;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #46355e;\n"
                                               "}")

            self.MainView.pushButtonFavorites.setStyleSheet("QPushButton{\n"
                                               "    background-color: #5F3E77;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #46355e;\n"
                                               "}")
            
            
            # Favorites
            self.MainView.labelFavoriteWidgetTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #46355e;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #4F6FA0;\n"
                                                  "}\n"
                                                  "")
            
            
            # Playlists
            self.MainView.labelPlaylistWidgetTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #46355e;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #4F6FA0;\n"
                                                  "}\n"
                                                  "")


            # Settings
            self.MainView.labelSettingsWidgetTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #46355e;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #4F6FA0;\n"
                                                  "}\n"
                                                  "")

            self.MainView.labelSettingsModeTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #46355e;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #4F6FA0;\n"
                                                  "}\n"
                                                  "")

            self.MainView.radioButtonDarkMode.setStyleSheet("QRadioButton {\n"
                                                                "    font : 75 11pt \"Microsoft JhengHei UI\"  bold;\n"
                                                                "    color : #FFFFFF;\n"
                                                                "    border-radius : 0px;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton:hover {\n"
                                                                "    color : #909090;\n"
                                                                "    border-radius : 0px;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton::checked {\n"
                                                                "    color : #909090;\n"
                                                                "    border-radius : 0px;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton::indicator {\n"
                                                                "    color : #909090;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton::indicator:checked:pressed {\n"
                                                                "    color : #909090;\n"
                                                                "}")

            self.MainView.radioButtonLightMode.setStyleSheet("QRadioButton {\n"
                                                                 "    font : 75 11pt \"Microsoft JhengHei UI\"  bold;\n"
                                                                 "    color : #FFFFFF;\n"
                                                                 "    border-radius : 0px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QRadioButton:hover {\n"
                                                                 "    color : #909090;\n"
                                                                 "    border-radius : 0px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QRadioButton::checked {\n"
                                                                 "    color : #909090;\n"
                                                                 "    border-radius : 0px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QRadioButton::indicator {\n"
                                                                 "    color : #909090;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QRadioButton::indicator:checked:pressed {\n"
                                                                 "    color : #909090;\n"
                                                                 "}")


            self.MainView.frameMode.setStyleSheet("QFrame {\n"
                                            "    background-color: #46355e;\n"
                                            "    border-radius : 40px;\n"
                                            "}\n"
                                            "\n"
                                            "")
            self.MainView.labelSettingsModeTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #FFFFFF;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #909090;\n"
                                                  "}\n"
                                                  "")


            # Player
            self.MainView.labelAlbum.setStyleSheet("QLabel {\n"
                                      "    font : 80 16pt \"Microsoft JhengHei UI\" bold;\n"
                                      "    color : #46355e;\n"
                                      "    border-radius : 0px;\n"
                                      "    text-align : left;\n"
                                      "    padding-left: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QLabel::hover {\n"
                                      "    color : #4F6FA0;\n"
                                      "}\n"
                                      "")
            
            #color : #46355e
            
            self.MainView.labelArtist.setStyleSheet("QLabel {\n"
                                       "    font : 80 13pt \"Microsoft JhengHei UI\" bold;\n"
                                       "    color : #46355e;\n"
                                       "    border-radius : 0px;\n"
                                       "    text-align : left;\n"
                                       "    padding-left: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QLabel::hover {\n"
                                       "    color : #4F6FA0;\n"
                                       "}\n"
                                       "")

            self.MainView.labelTitle.setStyleSheet("QLabel {\n"
                                      "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                      "    color : #46355e;\n"
                                      "    border-radius : 0px;\n"
                                      "    text-align : left;\n"
                                      "    padding-left: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QLabel::hover {\n"
                                      "    color : #4F6FA0;\n"
                                      "}\n"
                                      "")
            
            self.MainView.labelCodec.setStyleSheet("QLabel {\n"
                                      "    font : 22 9pt \"Microsoft JhengHei UI\" bold;\n"
                                      "    color : #46355e;\n"
                                      "    border-radius : 0px;\n"
                                      "    text-align : left;\n"
                                      "    padding-left: 5px;\n"
                                      "}")
        

            self.MainView.labelBitrate.setStyleSheet("QLabel {\n"
                                        "    font : 22 11pt \"Microsoft JhengHei UI\" bold;\n"
                                        "    color : #46355e;\n"
                                        "    border-radius : 0px;\n"
                                        "    text-align : left;\n"
                                        "    padding-left: 5px;\n"
                                        "}")
            
            self.MainView.labelDurationTime.setStyleSheet("QLabel {\n"
                                             "    font : 80 8pt \"Microsoft JhengHei UI\" bold;\n"
                                             "    color : #46355e;\n"
                                             "    border-radius : 0px;\n"
                                             "    text-align : left;\n"
                                             "    padding-left: 5px;\n"
                                             "}")
            
            self.MainView.labelCurrentTime.setStyleSheet("QLabel {\n"
                                            "    font : 80 8pt \"Microsoft JhengHei UI\" bold;\n"
                                            "    color : #46355e;\n"
                                            "    border-radius : 0px;\n"
                                            "    text-align : left;\n"
                                            "    padding-left: 5px;\n"
                                            "}")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            self.MainView.pushButtonPlay.setStyleSheet("QPushButton {\n"
                                          "    background: #202020;\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #202020;\n"
                                          "    border-radius: 20px;\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #505050;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: #808080;\n"
                                          "}")
            
            
            
            self.MainView.pushButtonPrevious.setStyleSheet("QPushButton {\n"
                                          "    background: #202020;\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #202020;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #505050;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: #808080;\n"
                                          "}")
            
            self.MainView.pushButtonNext.setStyleSheet("QPushButton {\n"
                                          "    background: #202020;\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #202020;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #505050;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: #808080;\n"
                                          "}")
            
            self.MainView.pushButtonVolume.setStyleSheet("QPushButton {\n"
                                          "    background: #202020;\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #202020;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #505050;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: #808080;\n"
                                          "}")


            self.MainView.pushButtonAddFavorite.setStyleSheet("QPushButton {\n"
                                                 "    background: #202020;\n"
                                                 "    color: #333333;\n"
                                                 "    border: 2px solid #202020;\n"
                                                 "    border-radius: 20px;\n"
                                                 "\n"
                                                 "    padding: 5px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background: #505050;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "    border-style: inset;\n"
                                                 "    background: #AD3F3F;;\n"
                                                 "}")


        
        elif self.MainView.radioButtonDarkMode.isChecked():
            
            self.MainView.frameContainer.setStyleSheet('QFrame { background-color: #121212;}')
            

            self.MainView.labelWindowTitleBar.setStyleSheet("QLabel {\n"
                                                "    font : 77 15pt \"Microsoft JhengHei UI\";\n"
                                                "    color : #FFFFFF;\n"
                                                "    border-radius : 0px;\n"
                                                "    text-align : left;\n"
                                                "    padding-left: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "QLabel::hover {\n"
                                                "    color : #4F6FA0;\n"
                                                "}\n"
                                                "")









            self.MainView.pushButtonBack.setStyleSheet("QPushButton{\n"
                                          "    background-color: transparent;\n"
                                          "    border-radius : 14px;\n"
                                          "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding : 10px;\n"
                                          "\n"
                                          "    text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #252525;\n"
                                          "}")

            self.MainView.pushButtonSettings.setStyleSheet("QPushButton{\n"
                                          "    background-color: transparent;\n"
                                          "    border-radius : 14px;\n"
                                          "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding : 10px;\n"
                                          "\n"
                                          "    text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #252525;\n"
                                          "}")

            self.MainView.pushButtonPlayer.setStyleSheet("QPushButton{\n"
                                          "    background-color: transparent;\n"
                                          "    border-radius : 14px;\n"
                                          "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding : 10px;\n"
                                          "\n"
                                          "    text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #252525;\n"
                                          "}")

            self.MainView.pushButtonPlaylistPlayer.setStyleSheet("QPushButton{\n"
                                          "    background-color: transparent;\n"
                                          "    border-radius : 14px;\n"
                                          "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding : 10px;\n"
                                          "\n"
                                          "    text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: #252525;\n"
                                          "}")




            # Library
            self.MainView.labelLibraryWidgetTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #FFFFFF;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #46355e;\n"
                                                  "}\n"
                                                  "")

            self.MainView.labelLibraryFileTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #FFFFFF;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #46355e;\n"
                                                  "}\n"
                                                  "")
            
            self.MainView.labelLibraryMusicTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #FFFFFF;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #46355e;\n"
                                                  "}\n"
                                                  "")


            self.MainView.pushButtonAddDirectory.setStyleSheet("QPushButton{\n"
                                               "    background-color: transparent;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #202020;\n"
                                               "}")
            
            self.MainView.pushButtonAddFile.setStyleSheet("QPushButton{\n"
                                               "    background-color: transparent;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #202020;\n"
                                               "}")
            
            self.MainView.pushButtonAddPath.setStyleSheet("QPushButton{\n"
                                               "    background-color: transparent;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #202020;\n"
                                               "}")
            
            self.MainView.pushButtonPlaylists.setStyleSheet("QPushButton{\n"
                                               "    background-color: transparent;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #202020;\n"
                                               "}")

            self.MainView.pushButtonFavorites.setStyleSheet("QPushButton{\n"
                                               "    background-color: transparent;\n"
                                               "    border-radius : 14px;\n"
                                               "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "    color: #FFFFFF;\n"
                                               "    padding : 10px;\n"
                                               "\n"
                                               "    text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #202020;\n"
                                               "}")
            
            
            # Favorites
            self.MainView.labelFavoriteWidgetTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #FFFFFF;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #46355e;\n"
                                                  "}\n"
                                                  "")
            
            
            # Playlists
            self.MainView.labelPlaylistWidgetTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #FFFFFF;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #46355e;\n"
                                                  "}\n"
                                                  "")

            
            # Settings
            self.MainView.labelSettingsWidgetTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #FFFFFF;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #46355e;\n"
                                                  "}\n"
                                                  "")



            self.MainView.frameMode.setStyleSheet("QFrame {\n"
                                            "    background-color: #212121;\n"
                                            "    border-radius : 40px;\n"
                                            "}\n"
                                            "\n"
                                            "")
            
            self.MainView.labelSettingsModeTitle.setStyleSheet("QLabel {\n"
                                                  "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                                  "    color : #FFFFFF;\n"
                                                  "    border-radius : 0px;\n"
                                                  "    text-align : left;\n"
                                                  "    padding-left: 5px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLabel::hover {\n"
                                                  "    color : #46355e;\n"
                                                  "}\n"
                                                  "")



            self.MainView.radioButtonDarkMode.setStyleSheet("QRadioButton {\n"
                                                                "    font : 75 11pt \"Microsoft JhengHei UI\"  bold;\n"
                                                                "    color : #FFFFFF;\n"
                                                                "    border-radius : 0px;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton:hover {\n"
                                                                "    color : #909090;\n"
                                                                "    border-radius : 0px;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton::checked {\n"
                                                                "    color : #909090;\n"
                                                                "    border-radius : 0px;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton::indicator {\n"
                                                                "    color : #909090;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QRadioButton::indicator:checked:pressed {\n"
                                                                "    color : #909090;\n"
                                                                "}")

            self.MainView.radioButtonLightMode.setStyleSheet("QRadioButton {\n"
                                                                 "    font : 75 11pt \"Microsoft JhengHei UI\"  bold;\n"
                                                                 "    color : #FFFFFF;\n"
                                                                 "    border-radius : 0px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QRadioButton:hover {\n"
                                                                 "    color : #909090;\n"
                                                                 "    border-radius : 0px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QRadioButton::checked {\n"
                                                                 "    color : #909090;\n"
                                                                 "    border-radius : 0px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QRadioButton::indicator {\n"
                                                                 "    color : #909090;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QRadioButton::indicator:checked:pressed {\n"
                                                                 "    color : #909090;\n"
                                                                 "}")




            # Player
            self.MainView.labelAlbum.setStyleSheet("QLabel {\n"
                                      "    font : 80 16pt \"Microsoft JhengHei UI\" bold;\n"
                                      "    color : #FFFFFF;\n"
                                      "    border-radius : 0px;\n"
                                      "    text-align : left;\n"
                                      "    padding-left: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QLabel::hover {\n"
                                      "    color : #4F6FA0;\n"
                                      "}\n"
                                      "")

            self.MainView.labelArtist.setStyleSheet("QLabel {\n"
                                       "    font : 80 13pt \"Microsoft JhengHei UI\" bold;\n"
                                       "    color : #FFFFFF;\n"
                                       "    border-radius : 0px;\n"
                                       "    text-align : left;\n"
                                       "    padding-left: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QLabel::hover {\n"
                                       "    color : #4F6FA0;\n"
                                       "}\n"
                                       "")

            self.MainView.labelTitle.setStyleSheet("QLabel {\n"
                                      "    font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                      "    color : #FFFFFF;\n"
                                      "    border-radius : 0px;\n"
                                      "    text-align : left;\n"
                                      "    padding-left: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QLabel::hover {\n"
                                      "    color : #4F6FA0;\n"
                                      "}\n"
                                      "")
            
            self.MainView.labelCodec.setStyleSheet("QLabel {\n"
                                      "    font : 22 9pt \"Microsoft JhengHei UI\" bold;\n"
                                      "    color : #FFFFFF;\n"
                                      "    border-radius : 0px;\n"
                                      "    text-align : left;\n"
                                      "    padding-left: 5px;\n"
                                      "}")
        

            self.MainView.labelBitrate.setStyleSheet("QLabel {\n"
                                        "    font : 22 11pt \"Microsoft JhengHei UI\" bold;\n"
                                        "    color : #FFFFFF;\n"
                                        "    border-radius : 0px;\n"
                                        "    text-align : left;\n"
                                        "    padding-left: 5px;\n"
                                        "}")
            
            self.MainView.labelDurationTime.setStyleSheet("QLabel {\n"
                                             "    font : 80 8pt \"Microsoft JhengHei UI\" bold;\n"
                                             "    color : #FFFFFF;\n"
                                             "    border-radius : 0px;\n"
                                             "    text-align : left;\n"
                                             "    padding-left: 5px;\n"
                                             "}")
            
            self.MainView.labelCurrentTime.setStyleSheet("QLabel {\n"
                                            "    font : 80 8pt \"Microsoft JhengHei UI\" bold;\n"
                                            "    color : #FFFFFF;\n"
                                            "    border-radius : 0px;\n"
                                            "    text-align : left;\n"
                                            "    padding-left: 5px;\n"
                                            "}")










            self.MainView.pushButtonAddFavorite.setStyleSheet("QPushButton {\n"
                                                 "    color: #333333;\n"
                                                 "    border: 2px solid #202020;\n"
                                                 "    border-radius: 20px;\n"
                                                 "\n"
                                                 "    padding: 5px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background: #202020;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "    border-style: inset;\n"
                                                 "    background: #AD3F3F;\n"
                                                 "}")


            self.MainView.pushButtonPlay.setStyleSheet("QPushButton {\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #202020;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #202020;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
                                          "}")
            self.MainView.pushButtonPrevious.setStyleSheet("QPushButton {\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #202020;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #202020;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
                                          "}")
            
            self.MainView.pushButtonNext.setStyleSheet("QPushButton {\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #202020;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #202020;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
                                          "}")
            
            self.MainView.pushButtonVolume.setStyleSheet("QPushButton {\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #202020;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #202020;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
                                          "}")
