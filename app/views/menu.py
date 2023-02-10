# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindowView(QtWidgets.QMainWindow):

    def __init__(self, Controller):
        super().__init__()

        self.Controller = Controller

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            qApp.quit()

        elif event.key() == QtCore.Qt.Key_F1:
            return self.stackedWidgetContainer.setCurrentWidget(self.widgetMenu)

        elif event.key() == QtCore.Qt.Key_F2:
            return self.stackedWidgetContainer.setCurrentWidget(self.widgetPlayer)

        else:
            super().keyPressEvent(event)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(550, 800)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frameContainer = QFrame(self.centralwidget)
        self.frameContainer.setObjectName(u"frameContainer")
        self.frameContainer.setStyleSheet(u"QFrame {\n"
                                          "\n"
                                          "	background-color : #111111;\n"
                                          "\n"
                                          "}")
        self.frameContainer.setFrameShape(QFrame.NoFrame)
        self.frameContainer.setFrameShadow(QFrame.Plain)
        self.frameContainer.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frameContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetContainer = QStackedWidget(self.frameContainer)
        self.stackedWidgetContainer.setObjectName(u"stackedWidgetContainer")
        self.stackedWidgetContainer.setStyleSheet(u"")
        self.stackedWidgetContainer.setLineWidth(0)
        self.widgetPlayer = QWidget()
        self.widgetPlayer.setObjectName(u"widgetPlayer")
        self.widgetPlayer.setStyleSheet(u"QWidget {\n"
                                        "\n"
                                        "	background-color : #111111;\n"
                                        "\n"
                                        "}")
        self.gridLayout_4 = QGridLayout(self.widgetPlayer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(9)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.framePlayerContent = QFrame(self.widgetPlayer)
        self.framePlayerContent.setObjectName(u"framePlayerContent")
        self.framePlayerContent.setStyleSheet(u"QFrame {\n"
                                              "\n"
                                              "	background-color : #111111;\n"
                                              "\n"
                                              "}")
        self.framePlayerContent.setFrameShape(QFrame.Panel)
        self.framePlayerContent.setFrameShadow(QFrame.Plain)
        self.framePlayerContent.setLineWidth(0)
        self.gridLayout_5 = QGridLayout(self.framePlayerContent)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(9)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.framePlayer = QFrame(self.framePlayerContent)
        self.framePlayer.setObjectName(u"framePlayer")
        self.framePlayer.setFrameShape(QFrame.NoFrame)
        self.framePlayer.setFrameShadow(QFrame.Plain)
        self.framePlayer.setLineWidth(0)
        self.gridLayout_9 = QGridLayout(self.framePlayer)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(9)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frameSong = QFrame(self.framePlayer)
        self.frameSong.setObjectName(u"frameSong")
        self.frameSong.setStyleSheet(u"QFrame {\n"
                                     "\n"
                                     "	background-color : #000000;\n"
                                     "\n"
                                     "}")
        self.frameSong.setFrameShape(QFrame.NoFrame)
        self.frameSong.setFrameShadow(QFrame.Plain)
        self.frameSong.setLineWidth(0)
        self.gridLayout_10 = QGridLayout(self.frameSong)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.labelArtistSong = QLabel(self.frameSong)
        self.labelArtistSong.setObjectName(u"labelArtistSong")
        self.labelArtistSong.setStyleSheet(u"QLabel {\n"
                                           "	font : 80 13pt \"Microsoft JhengHei UI\" bold;\n"
                                           "	color : #FFFFFF;\n"
                                           "	border-radius : 0px;\n"
                                           "	text-align : left;\n"
                                           "	padding-left: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QLabel::hover {\n"
                                           "	color : #4F6FA0;\n"
                                           "}\n"
                                           "")

        self.gridLayout_10.addWidget(
            self.labelArtistSong, 3, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.labelTitleSong = QLabel(self.frameSong)
        self.labelTitleSong.setObjectName(u"labelTitleSong")
        self.labelTitleSong.setStyleSheet(u"QLabel {\n"
                                          "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                          "	color : #FFFFFF;\n"
                                          "	border-radius : 0px;\n"
                                          "	text-align : left;\n"
                                          "	padding-left: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QLabel::hover {\n"
                                          "	color : #4F6FA0;\n"
                                          "}\n"
                                          "")
        self.labelTitleSong.setFrameShape(QFrame.Panel)
        self.labelTitleSong.setFrameShadow(QFrame.Plain)
        self.labelTitleSong.setLineWidth(0)

        self.gridLayout_10.addWidget(
            self.labelTitleSong, 1, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.frameSongTime = QFrame(self.frameSong)
        self.frameSongTime.setObjectName(u"frameSongTime")
        self.frameSongTime.setFrameShape(QFrame.StyledPanel)
        self.frameSongTime.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frameSongTime)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.framePlayerFunction = QFrame(self.frameSongTime)
        self.framePlayerFunction.setObjectName(u"framePlayerFunction")
        self.framePlayerFunction.setMinimumSize(QSize(0, 50))
        self.framePlayerFunction.setMaximumSize(QSize(16777215, 50))
        self.framePlayerFunction.setFrameShape(QFrame.StyledPanel)
        self.framePlayerFunction.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.framePlayerFunction)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(9)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)

        self.pushButtonNext = QPushButton(self.framePlayerFunction)
        self.pushButtonNext.setObjectName(u"pushButtonNext")
        self.pushButtonNext.setMinimumSize(QSize(40, 40))
        self.pushButtonNext.setMaximumSize(QSize(40, 40))
        self.pushButtonNext.setStyleSheet(u"QPushButton {\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #333333;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #444444;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
                                          "}")
        icon = QIcon()
        icon.addFile(u"app/resources/img/icons/24x24/cil-media-step-forward.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNext.setIcon(icon)
        self.pushButtonNext.setIconSize(QSize(24, 24))
        self.pushButtonNext.setFlat(True)

        self.gridLayout_6.addWidget(self.pushButtonNext, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.pushButtonPrevious = QPushButton(self.framePlayerFunction)
        self.pushButtonPrevious.setObjectName(u"pushButtonPrevious")
        self.pushButtonPrevious.setMinimumSize(QSize(40, 40))
        self.pushButtonPrevious.setMaximumSize(QSize(40, 40))
        self.pushButtonPrevious.setStyleSheet(u"QPushButton {\n"
                                              "    color: #333333;\n"
                                              "    border: 2px solid #333333;\n"
                                              "    border-radius: 20px;\n"
                                              "    /*border-style: outset;*/\n"
                                              "    padding: 5px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background: #444444;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    border-style: inset;\n"
                                              "    background: qradialgradient(\n"
                                              "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                              "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
                                              "}")
        icon1 = QIcon()
        icon1.addFile(u"app/resources/img/icons/24x24/cil-media-step-backward.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPrevious.setIcon(icon1)
        self.pushButtonPrevious.setIconSize(QSize(24, 24))
        self.pushButtonPrevious.setFlat(True)

        self.gridLayout_6.addWidget(self.pushButtonPrevious, 0, 2, 1, 1)

        self.pushButtonPlay = QPushButton(self.framePlayerFunction)
        self.pushButtonPlay.setObjectName(u"pushButtonPlay")
        self.pushButtonPlay.setMinimumSize(QSize(40, 40))
        self.pushButtonPlay.setMaximumSize(QSize(40, 40))
        self.pushButtonPlay.setStyleSheet(u"QPushButton {\n"
                                          "    color: #333333;\n"
                                          "    border: 2px solid #333333;\n"
                                          "    border-radius: 20px;\n"
                                          "    /*border-style: outset;*/\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: #444444;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
                                          "}")
        icon2 = QIcon()
        icon2.addFile(u"app/resources/img/icons/24x24/cil-media-play.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPlay.setIcon(icon2)
        self.pushButtonPlay.setIconSize(QSize(24, 24))
        self.pushButtonPlay.setFlat(True)

        self.gridLayout_6.addWidget(self.pushButtonPlay, 0, 3, 1, 1)

        self.gridLayout_14.addWidget(self.framePlayerFunction, 2, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.horizontalSliderTime = QSlider(self.frameSongTime)
        self.horizontalSliderTime.setObjectName(u"horizontalSliderTime")
        self.horizontalSliderTime.setMinimumSize(QSize(300, 0))
        self.horizontalSliderTime.setStyleSheet(u"QSlider::groove:horizontal {\n"
                                                "	border: 1px solid #333333;\n"
                                                "	height: 6px;\n"
                                                "\n"
                                                "	border-radius: 4px;\n"
                                                "}\n"
                                                "\n"
                                                "QSlider::handle:horizontal {\n"
                                                "	width : 6px;\n"
                                                "	border-radius : 2px;\n"
                                                "\n"
                                                "	height : 10px;\n"
                                                "	background-color : #FFFFFF;\n"
                                                "}\n"
                                                "\n"
                                                "QSlider::add-page:qlineargradient {\n"
                                                "	background: #222222;\n"
                                                "	border-top-right-radius: 9px;\n"
                                                "	border-bottom-right-radius: 9px;\n"
                                                "	border-top-left-radius: 0px;\n"
                                                "	border-bottom-left-radius: 0px;\n"
                                                "}\n"
                                                "\n"
                                                "QSlider::sub-page:qlineargradient {\n"
                                                "	background: #5F3E77;\n"
                                                "	border-top-right-radius: 0px;\n"
                                                "	border-bottom-right-radius: 0px;\n"
                                                "	border-top-left-radius: 9px;\n"
                                                "	border-bottom-left-radius: 9px;\n"
                                                "}")
        self.horizontalSliderTime.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.horizontalSliderTime, 0, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 3, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_5, 0, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(
            20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_3, 1, 2, 1, 1)

        self.labelDuration = QLabel(self.frameSongTime)
        self.labelDuration.setObjectName(u"labelDuration")
        self.labelDuration.setStyleSheet(u"QLabel {\n"
                                         "	font : 80 8pt \"Microsoft JhengHei UI\" bold;\n"
                                         "	color : #FFFFFF;\n"
                                         "	border-radius : 0px;\n"
                                         "	text-align : left;\n"
                                         "	padding-left: 5px;\n"
                                         "}")

        self.gridLayout_14.addWidget(self.labelDuration, 0, 3, 1, 1)

        self.labelTime = QLabel(self.frameSongTime)
        self.labelTime.setObjectName(u"labelTime")
        self.labelTime.setStyleSheet(u"QLabel {\n"
                                     "	font : 80 8pt \"Microsoft JhengHei UI\" bold;\n"
                                     "	color : #FFFFFF;\n"
                                     "	border-radius : 0px;\n"
                                     "	text-align : left;\n"
                                     "	padding-left: 5px;\n"
                                     "}")

        self.gridLayout_14.addWidget(self.labelTime, 0, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_10, 7, 2, 1, 1)

        self.labelBitrate = QLabel(self.frameSongTime)
        self.labelBitrate.setObjectName(u"labelBitrate")
        self.labelBitrate.setStyleSheet(u"QLabel {\n"
                                        "	font : 22 11pt \"Microsoft JhengHei UI\" bold;\n"
                                        "	color : #FFFFFF;\n"
                                        "	border-radius : 0px;\n"
                                        "	text-align : left;\n"
                                        "	padding-left: 5px;\n"
                                        "}")

        self.gridLayout_14.addWidget(
            self.labelBitrate, 6, 2, 1, 1, Qt.AlignHCenter)

        self.frameVolume = QFrame(self.frameSongTime)
        self.frameVolume.setObjectName(u"frameVolume")
        self.frameVolume.setFrameShape(QFrame.StyledPanel)
        self.frameVolume.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frameVolume)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButtonVolume = QPushButton(self.frameVolume)
        self.pushButtonVolume.setObjectName(u"pushButtonVolume")
        self.pushButtonVolume.setMinimumSize(QSize(40, 40))
        self.pushButtonVolume.setMaximumSize(QSize(40, 40))
        self.pushButtonVolume.setStyleSheet(u"QPushButton {\n"
                                            "    color: #222222;\n"
                                            "    border: 2px solid #222222;\n"
                                            "    border-radius: 20px;\n"
                                            "    /*border-style: outset;*/\n"
                                            "    padding: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background: #222222;\n"
                                            "}\n"
                                            "")
        icon3 = QIcon()
        icon3.addFile(u"app/resources/img/icons/24x24/cil-volume-high.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonVolume.setIcon(icon3)
        self.pushButtonVolume.setIconSize(QSize(24, 24))

        self.gridLayout_12.addWidget(self.pushButtonVolume, 0, 0, 1, 1)

        self.horizontalSliderVolume = QSlider(self.frameVolume)
        self.horizontalSliderVolume.setObjectName(u"horizontalSliderVolume")
        self.horizontalSliderVolume.setStyleSheet(u"QSlider::groove:horizontal {\n"
                                                  "	border: 1px solid #333333;\n"
                                                  "	height: 6px;\n"
                                                  "\n"
                                                  "	border-radius: 4px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QSlider::handle:horizontal {\n"
                                                  "	width : 6px;\n"
                                                  "	border-radius : 2px;\n"
                                                  "\n"
                                                  "	height : 10px;\n"
                                                  "	background-color : #FFFFFF;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QSlider::add-page:qlineargradient {\n"
                                                  "	background: #222222;\n"
                                                  "	border-top-right-radius: 9px;\n"
                                                  "	border-bottom-right-radius: 9px;\n"
                                                  "	border-top-left-radius: 0px;\n"
                                                  "	border-bottom-left-radius: 0px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QSlider::sub-page:qlineargradient {\n"
                                                  "	background: #4F6FA0;\n"
                                                  "	border-top-right-radius: 0px;\n"
                                                  "	border-bottom-right-radius: 0px;\n"
                                                  "	border-top-left-radius: 9px;\n"
                                                  "	border-bottom-left-radius: 9px;\n"
                                                  "}")
        self.horizontalSliderVolume.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.horizontalSliderVolume, 0, 1, 1, 1)

        self.pushButtonAddFavorite = QPushButton(self.frameVolume)
        self.pushButtonAddFavorite.setObjectName(u"pushButtonAddFavorite")
        self.pushButtonAddFavorite.setMinimumSize(QSize(40, 40))
        self.pushButtonAddFavorite.setMaximumSize(QSize(40, 40))
        self.pushButtonAddFavorite.setStyleSheet(u"QPushButton {\n"
                                                 "    color: #222222;\n"
                                                 "    border: 2px solid #222222;\n"
                                                 "    border-radius: 20px;\n"
                                                 "    /*border-style: outset;*/\n"
                                                 "    padding: 5px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background: #222222;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "    border-style: inset;\n"
                                                 "    background: #AD3F3F;\n"
                                                 "}")
        icon4 = QIcon()
        icon4.addFile(u"app/resources/img/icons/24x24/cil-heart.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddFavorite.setIcon(icon4)
        self.pushButtonAddFavorite.setIconSize(QSize(24, 24))

        self.gridLayout_12.addWidget(self.pushButtonAddFavorite, 0, 2, 1, 1)

        self.gridLayout_14.addWidget(self.frameVolume, 4, 2, 1, 1)

        self.labelCodec = QLabel(self.frameSongTime)
        self.labelCodec.setObjectName(u"labelCodec")
        self.labelCodec.setStyleSheet(u"QLabel {\n"
                                      "	font : 22 9pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color : #FFFFFF;\n"
                                      "	border-radius : 0px;\n"
                                      "	text-align : left;\n"
                                      "	padding-left: 5px;\n"
                                      "}")

        self.gridLayout_14.addWidget(
            self.labelCodec, 5, 2, 1, 1, Qt.AlignHCenter)

        self.labelTime.raise_()
        self.framePlayerFunction.raise_()
        self.frameVolume.raise_()
        self.labelBitrate.raise_()
        self.horizontalSliderTime.raise_()
        self.labelDuration.raise_()
        self.labelCodec.raise_()

        self.gridLayout_10.addWidget(self.frameSongTime, 5, 0, 1, 1)

        self.labelAlbumSong = QLabel(self.frameSong)
        self.labelAlbumSong.setObjectName(u"labelAlbumSong")
        self.labelAlbumSong.setStyleSheet(u"QLabel {\n"
                                          "	font : 80 16pt \"Microsoft JhengHei UI\" bold;\n"
                                          "	color : #FFFFFF;\n"
                                          "	border-radius : 0px;\n"
                                          "	text-align : left;\n"
                                          "	padding-left: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QLabel::hover {\n"
                                          "	color : #4F6FA0;\n"
                                          "}\n"
                                          "")

        self.gridLayout_10.addWidget(
            self.labelAlbumSong, 2, 0, 1, 1, Qt.AlignHCenter)

        self.gridLayout_9.addWidget(self.frameSong, 1, 0, 1, 1)

        self.frameCoverArt = QFrame(self.framePlayer)
        self.frameCoverArt.setObjectName(u"frameCoverArt")
        self.frameCoverArt.setStyleSheet(u"QFrame {\n"
                                         "\n"
                                         "	background-color : #000000;\n"
                                         "\n"
                                         "}")
        self.frameCoverArt.setFrameShape(QFrame.Panel)
        self.frameCoverArt.setFrameShadow(QFrame.Plain)
        self.frameCoverArt.setLineWidth(0)
        self.gridLayout_11 = QGridLayout(self.frameCoverArt)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(9)
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setContentsMargins(9, 0, 9, 0)
        self.pushButtonMenu = QPushButton(self.frameCoverArt)
        self.pushButtonMenu.setObjectName(u"pushButtonMenu")
        self.pushButtonMenu.setMinimumSize(QSize(42, 42))
        self.pushButtonMenu.setMaximumSize(QSize(42, 42))
        self.pushButtonMenu.setStyleSheet(u"QPushButton{\n"
                                          "	background-color: #000000;\n"
                                          "\n"
                                          "	border-top-left-radius: 14px;\n"
                                          "	border-bottom-left-radius: 14px;\n"
                                          "	border-top-right-radius: 14px;\n"
                                          "	border-bottom-right-radius: 14px;\n"
                                          "\n"
                                          "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "	color: #FFFFFF;\n"
                                          "	padding : 10px;\n"
                                          "\n"
                                          "	text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "	background-color: #222222;\n"
                                          "	border-top-left-radius: 14px;	\n"
                                          "	border-bottom-left-radius: 14px;\n"
                                          "	border-top-right-radius: 14px;\n"
                                          "	border-bottom-right-radius: 14px;\n"
                                          "\n"
                                          "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "	color: #FFFFFF;\n"
                                          "	text-align : left;\n"
                                          "\n"
                                          "}")
        icon5 = QIcon()
        icon5.addFile(u"app/resources/img/icons/24x24/cil-list.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMenu.setIcon(icon5)
        self.pushButtonMenu.setIconSize(QSize(24, 24))

        self.gridLayout_11.addWidget(
            self.pushButtonMenu, 1, 1, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_11, 3, 4, 1, 1)

        self.labelCoverArt = QLabel(self.frameCoverArt)
        self.labelCoverArt.setObjectName(u"labelCoverArt")
        self.labelCoverArt.setMinimumSize(QSize(300, 300))
        self.labelCoverArt.setMaximumSize(QSize(300, 300))
        self.labelCoverArt.setSizeIncrement(QSize(0, 0))
        self.labelCoverArt.setBaseSize(QSize(100, 100))
        self.labelCoverArt.setAutoFillBackground(False)
        self.labelCoverArt.setLineWidth(0)
        self.labelCoverArt.setScaledContents(True)
        self.labelCoverArt.setWordWrap(False)

        self.gridLayout_11.addWidget(
            self.labelCoverArt, 3, 3, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 0, 1, 1, 5)

        self.verticalSpacer_32 = QSpacerItem(
            20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_32, 2, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_7, 3, 5, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_6, 3, 1, 1, 1)

        self.gridLayout_9.addWidget(self.frameCoverArt, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.framePlayer, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.framePlayerContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetPlayer)
        self.widgetMenu = QWidget()
        self.widgetMenu.setObjectName(u"widgetMenu")
        self.widgetMenu.setStyleSheet(u"QWidget {\n"
                                      "\n"
                                      "	background-color : #111111;\n"
                                      "\n"
                                      "}")
        self.gridLayout_7 = QGridLayout(self.widgetMenu)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frameMenuContent = QFrame(self.widgetMenu)
        self.frameMenuContent.setObjectName(u"frameMenuContent")
        self.frameMenuContent.setStyleSheet(u"QFrame {\n"
                                            "\n"
                                            "	background-color : #111111;\n"
                                            "}")
        self.frameMenuContent.setFrameShape(QFrame.NoFrame)
        self.frameMenuContent.setFrameShadow(QFrame.Plain)
        self.frameMenuContent.setLineWidth(0)
        self.gridLayout_13 = QGridLayout(self.frameMenuContent)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(9)
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setContentsMargins(9, 0, 9, 0)
        self.labelPlaylist = QLabel(self.frameMenuContent)
        self.labelPlaylist.setObjectName(u"labelPlaylist")
        self.labelPlaylist.setStyleSheet(u"QLabel {\n"
                                         "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                         "	color : #FFFFFF;\n"
                                         "	border-radius : 0px;\n"
                                         "	text-align : left;\n"
                                         "	padding-left: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel::hover {\n"
                                         "	color : #4F6FA0;\n"
                                         "}\n"
                                         "")

        self.gridLayout_13.addWidget(
            self.labelPlaylist, 3, 1, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_8 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_13.addItem(self.verticalSpacer_8, 0, 0, 1, 11)

        self.frameLibrary = QFrame(self.frameMenuContent)
        self.frameLibrary.setObjectName(u"frameLibrary")
        self.frameLibrary.setFrameShape(QFrame.NoFrame)
        self.frameLibrary.setFrameShadow(QFrame.Plain)
        self.frameLibrary.setLineWidth(0)
        self.gridLayout_15 = QGridLayout(self.frameLibrary)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButtonAddFile = QPushButton(self.frameLibrary)
        self.pushButtonAddFile.setObjectName(u"pushButtonAddFile")
        self.pushButtonAddFile.setStyleSheet(u"QPushButton{\n"
                                             "	background-color: #000000;\n"
                                             "\n"
                                             "	border-top-left-radius: 14px;\n"
                                             "	border-bottom-left-radius: 14px;\n"
                                             "	border-top-right-radius: 14px;\n"
                                             "	border-bottom-right-radius: 14px;\n"
                                             "\n"
                                             "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                             "	color: #FFFFFF;\n"
                                             "	padding : 10px;\n"
                                             "\n"
                                             "	text-align : left;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "	background-color: #222222;\n"
                                             "	border-top-left-radius: 14px;	\n"
                                             "	border-bottom-left-radius: 14px;\n"
                                             "	border-top-right-radius: 14px;\n"
                                             "	border-bottom-right-radius: 14px;\n"
                                             "\n"
                                             "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                             "	color: #FFFFFF;\n"
                                             "	text-align : left;\n"
                                             "\n"
                                             "}")
        icon6 = QIcon()
        icon6.addFile(u"app/resources/img/icons/24x24/cil-copy.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddFile.setIcon(icon6)
        self.pushButtonAddFile.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddFile, 3, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_9, 7, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(
            20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_6, 13, 0, 1, 1)

        self.labelFileOptions = QLabel(self.frameLibrary)
        self.labelFileOptions.setObjectName(u"labelFileOptions")
        self.labelFileOptions.setStyleSheet(u"QLabel {\n"
                                            "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                            "	color : #FFFFFF;\n"
                                            "	border-radius : 0px;\n"
                                            "	text-align : left;\n"
                                            "	padding-left: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QLabel::hover {\n"
                                            "	color : #4F6FA0;\n"
                                            "}\n"
                                            "")

        self.gridLayout_15.addWidget(
            self.labelFileOptions, 1, 0, 1, 1, Qt.AlignLeft)

        self.pushButtonFavorites = QPushButton(self.frameLibrary)
        self.pushButtonFavorites.setObjectName(u"pushButtonFavorites")
        self.pushButtonFavorites.setStyleSheet(u"QPushButton{\n"
                                               "	background-color: #000000;\n"
                                               "\n"
                                               "	border-top-left-radius: 14px;\n"
                                               "	border-bottom-left-radius: 14px;\n"
                                               "	border-top-right-radius: 14px;\n"
                                               "	border-bottom-right-radius: 14px;\n"
                                               "\n"
                                               "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "	color: #FFFFFF;\n"
                                               "	padding : 10px;\n"
                                               "\n"
                                               "	text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "	background-color: #222222;\n"
                                               "	border-top-left-radius: 14px;	\n"
                                               "	border-bottom-left-radius: 14px;\n"
                                               "	border-top-right-radius: 14px;\n"
                                               "	border-bottom-right-radius: 14px;\n"
                                               "\n"
                                               "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "	color: #FFFFFF;\n"
                                               "	text-align : left;\n"
                                               "\n"
                                               "}")
        self.pushButtonFavorites.setIcon(icon4)
        self.pushButtonFavorites.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonFavorites, 12, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(
            20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_18, 6, 0, 1, 1)

        self.pushButtonPlaylists = QPushButton(self.frameLibrary)
        self.pushButtonPlaylists.setObjectName(u"pushButtonPlaylists")
        self.pushButtonPlaylists.setStyleSheet(u"QPushButton{\n"
                                               "	background-color: #000000;\n"
                                               "\n"
                                               "	border-top-left-radius: 14px;\n"
                                               "	border-bottom-left-radius: 14px;\n"
                                               "	border-top-right-radius: 14px;\n"
                                               "	border-bottom-right-radius: 14px;\n"
                                               "\n"
                                               "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "	color: #FFFFFF;\n"
                                               "	padding : 10px;\n"
                                               "\n"
                                               "	text-align : left;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "	background-color: #222222;\n"
                                               "	border-top-left-radius: 14px;	\n"
                                               "	border-bottom-left-radius: 14px;\n"
                                               "	border-top-right-radius: 14px;\n"
                                               "	border-bottom-right-radius: 14px;\n"
                                               "\n"
                                               "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                               "	color: #FFFFFF;\n"
                                               "	text-align : left;\n"
                                               "\n"
                                               "}")
        self.pushButtonPlaylists.setIcon(icon5)
        self.pushButtonPlaylists.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonPlaylists, 11, 0, 1, 1)

        self.pushButtonRecentlyPlayed = QPushButton(self.frameLibrary)
        self.pushButtonRecentlyPlayed.setObjectName(
            u"pushButtonRecentlyPlayed")
        self.pushButtonRecentlyPlayed.setStyleSheet(u"QPushButton{\n"
                                                    "	background-color: #000000;\n"
                                                    "\n"
                                                    "	border-top-left-radius: 14px;\n"
                                                    "	border-bottom-left-radius: 14px;\n"
                                                    "	border-top-right-radius: 14px;\n"
                                                    "	border-bottom-right-radius: 14px;\n"
                                                    "\n"
                                                    "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                                    "	color: #FFFFFF;\n"
                                                    "	padding : 10px;\n"
                                                    "\n"
                                                    "	text-align : left;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover{\n"
                                                    "	background-color: #222222;\n"
                                                    "	border-top-left-radius: 14px;	\n"
                                                    "	border-bottom-left-radius: 14px;\n"
                                                    "	border-top-right-radius: 14px;\n"
                                                    "	border-bottom-right-radius: 14px;\n"
                                                    "\n"
                                                    "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                                    "	color: #FFFFFF;\n"
                                                    "	text-align : left;\n"
                                                    "\n"
                                                    "}")
        icon7 = QIcon()
        icon7.addFile(u"app/resources/img/icons/24x24/cil-library.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRecentlyPlayed.setIcon(icon7)
        self.pushButtonRecentlyPlayed.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(
            self.pushButtonRecentlyPlayed, 10, 0, 1, 1)

        self.pushButtonAddDirectory = QPushButton(self.frameLibrary)
        self.pushButtonAddDirectory.setObjectName(u"pushButtonAddDirectory")
        self.pushButtonAddDirectory.setStyleSheet(u"QPushButton{\n"
                                                  "	background-color: #000000;\n"
                                                  "\n"
                                                  "	border-top-left-radius: 14px;\n"
                                                  "	border-bottom-left-radius: 14px;\n"
                                                  "	border-top-right-radius: 14px;\n"
                                                  "	border-bottom-right-radius: 14px;\n"
                                                  "\n"
                                                  "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                                  "	color: #FFFFFF;\n"
                                                  "	padding : 10px;\n"
                                                  "\n"
                                                  "	text-align : left;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "	background-color: #222222;\n"
                                                  "	border-top-left-radius: 14px;	\n"
                                                  "	border-bottom-left-radius: 14px;\n"
                                                  "	border-top-right-radius: 14px;\n"
                                                  "	border-bottom-right-radius: 14px;\n"
                                                  "\n"
                                                  "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                                  "	color: #FFFFFF;\n"
                                                  "	text-align : left;\n"
                                                  "\n"
                                                  "}")
        icon8 = QIcon()
        icon8.addFile(u"app/resources/img/icons/24x24/cil-folder-open.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddDirectory.setIcon(icon8)
        self.pushButtonAddDirectory.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddDirectory, 4, 0, 1, 1)

        self.labelMusic = QLabel(self.frameLibrary)
        self.labelMusic.setObjectName(u"labelMusic")
        self.labelMusic.setStyleSheet(u"QLabel {\n"
                                      "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                      "	color : #FFFFFF;\n"
                                      "	border-radius : 0px;\n"
                                      "	text-align : left;\n"
                                      "	padding-left: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QLabel::hover {\n"
                                      "	color : #4F6FA0;\n"
                                      "}\n"
                                      "")

        self.gridLayout_15.addWidget(self.labelMusic, 8, 0, 1, 1, Qt.AlignLeft)

        self.pushButtonAddPath = QPushButton(self.frameLibrary)
        self.pushButtonAddPath.setObjectName(u"pushButtonAddPath")
        self.pushButtonAddPath.setStyleSheet(u"QPushButton{\n"
                                             "	background-color: #000000;\n"
                                             "\n"
                                             "	border-top-left-radius: 14px;\n"
                                             "	border-bottom-left-radius: 14px;\n"
                                             "	border-top-right-radius: 14px;\n"
                                             "	border-bottom-right-radius: 14px;\n"
                                             "\n"
                                             "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                             "	color: #FFFFFF;\n"
                                             "	padding : 10px;\n"
                                             "\n"
                                             "	text-align : left;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "	background-color: #222222;\n"
                                             "	border-top-left-radius: 14px;	\n"
                                             "	border-bottom-left-radius: 14px;\n"
                                             "	border-top-right-radius: 14px;\n"
                                             "	border-bottom-right-radius: 14px;\n"
                                             "\n"
                                             "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                             "	color: #FFFFFF;\n"
                                             "	text-align : left;\n"
                                             "\n"
                                             "}")
        icon9 = QIcon()
        icon9.addFile(u"app/resources/img/icons/24x24/cil-plus.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddPath.setIcon(icon9)
        self.pushButtonAddPath.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddPath, 5, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_16, 9, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_15, 2, 0, 1, 1)

        self.gridLayout_13.addWidget(self.frameLibrary, 2, 0, 1, 11)

        self.lineEditSearcher = QLineEdit(self.frameMenuContent)
        self.lineEditSearcher.setObjectName(u"lineEditSearcher")
        self.lineEditSearcher.setMinimumSize(QSize(260, 0))
        self.lineEditSearcher.setStyleSheet(u"QLineEdit{\n"
                                            "	background-color: #222222;\n"
                                            "\n"
                                            "	border-top-left-radius: 14px;\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	padding : 10px;\n"
                                            "\n"
                                            "	text-align : left;\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit:hover{\n"
                                            "	background-color: #444444;\n"
                                            "	border-top-left-radius: 14px;	\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	text-align : left;\n"
                                            "\n"
                                            "}")

        self.gridLayout_13.addWidget(self.lineEditSearcher, 5, 1, 1, 2)

        self.horizontalSpacer_9 = QSpacerItem(
            20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_9, 5, 3, 1, 1)

        self.pushButtonSaveActualPlaylist = QPushButton(self.frameMenuContent)
        self.pushButtonSaveActualPlaylist.setObjectName(
            u"pushButtonSaveActualPlaylist")
        self.pushButtonSaveActualPlaylist.setStyleSheet(u"QPushButton{\n"
                                                        "	background-color: #000000;\n"
                                                        "\n"
                                                        "	border-top-left-radius: 14px;\n"
                                                        "	border-bottom-left-radius: 14px;\n"
                                                        "	border-top-right-radius: 14px;\n"
                                                        "	border-bottom-right-radius: 14px;\n"
                                                        "\n"
                                                        "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                                        "	color: #FFFFFF;\n"
                                                        "	padding : 10px;\n"
                                                        "\n"
                                                        "	text-align : left;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:hover{\n"
                                                        "	background-color: #222222;\n"
                                                        "	border-top-left-radius: 14px;	\n"
                                                        "	border-bottom-left-radius: 14px;\n"
                                                        "	border-top-right-radius: 14px;\n"
                                                        "	border-bottom-right-radius: 14px;\n"
                                                        "\n"
                                                        "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                                        "	color: #FFFFFF;\n"
                                                        "	text-align : left;\n"
                                                        "\n"
                                                        "}")
        icon10 = QIcon()
        icon10.addFile(u"app/resources/img/icons/24x24/cil-library-add.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveActualPlaylist.setIcon(icon10)
        self.pushButtonSaveActualPlaylist.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(
            self.pushButtonSaveActualPlaylist, 3, 5, 1, 4)

        self.listViewPlaylist = QListView(self.frameMenuContent)
        self.listViewPlaylist.setObjectName(u"listViewPlaylist")
        self.listViewPlaylist.setMinimumSize(QSize(0, 150))
        self.listViewPlaylist.setStyleSheet(u"QListView {\n"
                                            "	font : 77 13pt \"Microsoft JhengHei UI\";\n"
                                            "	color : #FFFFFF;\n"
                                            "	border-radius : 0px;\n"
                                            "	text-align : left;\n"
                                            "	padding-left: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QListView::hover {\n"
                                            "	color : #4F6FA0;\n"
                                            "}")
        self.listViewPlaylist.setFrameShadow(QFrame.Plain)
        self.listViewPlaylist.setDragEnabled(True)
        self.listViewPlaylist.setDragDropMode(QAbstractItemView.DragDrop)
        self.listViewPlaylist.setDefaultDropAction(Qt.MoveAction)
        self.listViewPlaylist.setResizeMode(QListView.Fixed)
        self.listViewPlaylist.setLayoutMode(QListView.SinglePass)
        self.listViewPlaylist.setItemAlignment(Qt.AlignLeading)

        self.gridLayout_13.addWidget(self.listViewPlaylist, 8, 0, 1, 11)

        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_10, 4, 1, 1, 8)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 3, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_13, 6, 1, 1, 8)

        self.pushButtonSearch = QPushButton(self.frameMenuContent)
        self.pushButtonSearch.setObjectName(u"pushButtonSearch")
        self.pushButtonSearch.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: #5F3E77;\n"
                                            "\n"
                                            "	border-top-left-radius: 14px;\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	padding : 10px;\n"
                                            "\n"
                                            "	text-align : left;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "	background-color: #222222;\n"
                                            "	border-top-left-radius: 14px;	\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	text-align : left;\n"
                                            "\n"
                                            "}")
        icon11 = QIcon()
        icon11.addFile(u"app/resources/img/icons/24x24/cil-arrow-circle-right.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSearch.setIcon(icon11)
        self.pushButtonSearch.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.pushButtonSearch, 5, 5, 1, 4)

        self.pushButtonSettings = QPushButton(self.frameMenuContent)
        self.pushButtonSettings.setObjectName(u"pushButtonSettings")
        self.pushButtonSettings.setMinimumSize(QSize(42, 42))
        self.pushButtonSettings.setMaximumSize(QSize(42, 42))
        self.pushButtonSettings.setStyleSheet(u"QPushButton{\n"
                                              "	background-color: #000000;\n"
                                              "\n"
                                              "	border-top-left-radius: 14px;\n"
                                              "	border-bottom-left-radius: 14px;\n"
                                              "	border-top-right-radius: 14px;\n"
                                              "	border-bottom-right-radius: 14px;\n"
                                              "\n"
                                              "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                              "	color: #FFFFFF;\n"
                                              "	padding : 10px;\n"
                                              "\n"
                                              "	text-align : left;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "	background-color: #222222;\n"
                                              "	border-top-left-radius: 14px;	\n"
                                              "	border-bottom-left-radius: 14px;\n"
                                              "	border-top-right-radius: 14px;\n"
                                              "	border-bottom-right-radius: 14px;\n"
                                              "\n"
                                              "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                              "	color: #FFFFFF;\n"
                                              "	text-align : left;\n"
                                              "\n"
                                              "}")
        icon12 = QIcon()
        icon12.addFile(u"app/resources/img/icons/24x24/cil-settings.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSettings.setIcon(icon12)
        self.pushButtonSettings.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.pushButtonSettings, 1, 7, 1, 1)

        self.pushButtonSong = QPushButton(self.frameMenuContent)
        self.pushButtonSong.setObjectName(u"pushButtonSong")
        self.pushButtonSong.setMinimumSize(QSize(42, 42))
        self.pushButtonSong.setMaximumSize(QSize(42, 42))
        self.pushButtonSong.setStyleSheet(u"QPushButton{\n"
                                          "	background-color: #000000;\n"
                                          "\n"
                                          "	border-top-left-radius: 14px;\n"
                                          "	border-bottom-left-radius: 14px;\n"
                                          "	border-top-right-radius: 14px;\n"
                                          "	border-bottom-right-radius: 14px;\n"
                                          "\n"
                                          "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "	color: #FFFFFF;\n"
                                          "	padding : 10px;\n"
                                          "\n"
                                          "	text-align : left;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "	background-color: #222222;\n"
                                          "	border-top-left-radius: 14px;	\n"
                                          "	border-bottom-left-radius: 14px;\n"
                                          "	border-top-right-radius: 14px;\n"
                                          "	border-bottom-right-radius: 14px;\n"
                                          "\n"
                                          "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                          "	color: #FFFFFF;\n"
                                          "	text-align : left;\n"
                                          "\n"
                                          "}")
        icon13 = QIcon()
        icon13.addFile(u"app/resources/img/icons/24x24/cil-music-note.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSong.setIcon(icon13)
        self.pushButtonSong.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.pushButtonSong, 1, 8, 1, 1)

        self.gridLayout_7.addWidget(self.frameMenuContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetMenu)
        self.widgetPlaylist = QWidget()
        self.widgetPlaylist.setObjectName(u"widgetPlaylist")
        self.widgetPlaylist.setStyleSheet(u"QWidget {\n"
                                          "\n"
                                          "	background-color : #111111;\n"
                                          "\n"
                                          "}")
        self.gridLayout_16 = QGridLayout(self.widgetPlaylist)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.framePlaylistContent = QFrame(self.widgetPlaylist)
        self.framePlaylistContent.setObjectName(u"framePlaylistContent")
        self.framePlaylistContent.setStyleSheet(u"QFrame {\n"
                                                "\n"
                                                "	background-color : #111111;\n"
                                                "}")
        self.framePlaylistContent.setFrameShape(QFrame.NoFrame)
        self.framePlaylistContent.setFrameShadow(QFrame.Plain)
        self.framePlaylistContent.setLineWidth(0)
        self.gridLayout_17 = QGridLayout(self.framePlaylistContent)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(9)
        self.gridLayout_17.setVerticalSpacing(0)
        self.gridLayout_17.setContentsMargins(9, 0, 9, 0)
        self.listViewPlaylists = QListView(self.framePlaylistContent)
        self.listViewPlaylists.setObjectName(u"listViewPlaylists")
        self.listViewPlaylists.setStyleSheet(u"QListView {\n"
                                             "	font : 77 13pt \"Microsoft JhengHei UI\";\n"
                                             "	color : #FFFFFF;\n"
                                             "	border-radius : 0px;\n"
                                             "	text-align : left;\n"
                                             "	padding-left: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QListView::hover {\n"
                                             "	color : #4F6FA0;\n"
                                             "}")
        self.listViewPlaylists.setFrameShadow(QFrame.Plain)
        self.listViewPlaylists.setDragEnabled(True)
        self.listViewPlaylists.setDragDropMode(QAbstractItemView.DragDrop)
        self.listViewPlaylists.setDefaultDropAction(Qt.MoveAction)
        self.listViewPlaylists.setResizeMode(QListView.Fixed)
        self.listViewPlaylists.setLayoutMode(QListView.SinglePass)
        self.listViewPlaylists.setItemAlignment(Qt.AlignLeading)

        self.gridLayout_17.addWidget(self.listViewPlaylists, 5, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_11, 4, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_12, 1, 0, 1, 1)

        self.labelPlaylisr = QLabel(self.framePlaylistContent)
        self.labelPlaylisr.setObjectName(u"labelPlaylisr")
        self.labelPlaylisr.setStyleSheet(u"QLabel {\n"
                                         "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                         "	color : #FFFFFF;\n"
                                         "	border-radius : 0px;\n"
                                         "	text-align : left;\n"
                                         "	padding-right: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel::hover {\n"
                                         "	color : #4F6FA0;\n"
                                         "}\n"
                                         "")

        self.gridLayout_17.addWidget(
            self.labelPlaylisr, 3, 0, 1, 1, Qt.AlignRight)

        self.pushButtonMenu_2 = QPushButton(self.framePlaylistContent)
        self.pushButtonMenu_2.setObjectName(u"pushButtonMenu_2")
        self.pushButtonMenu_2.setMinimumSize(QSize(42, 42))
        self.pushButtonMenu_2.setMaximumSize(QSize(42, 42))
        self.pushButtonMenu_2.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: #000000;\n"
                                            "\n"
                                            "	border-top-left-radius: 14px;\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	padding : 10px;\n"
                                            "\n"
                                            "	text-align : left;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "	background-color: #222222;\n"
                                            "	border-top-left-radius: 14px;	\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	text-align : left;\n"
                                            "\n"
                                            "}")
        icon14 = QIcon()
        icon14.addFile(u"app/resources/img/icons/24x24/cil-arrow-circle-left.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMenu_2.setIcon(icon14)
        self.pushButtonMenu_2.setIconSize(QSize(24, 24))

        self.gridLayout_17.addWidget(self.pushButtonMenu_2, 2, 0, 1, 1)

        self.gridLayout_16.addWidget(self.framePlaylistContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetPlaylist)
        self.widgetInterest = QWidget()
        self.widgetInterest.setObjectName(u"widgetInterest")
        self.widgetInterest.setStyleSheet(u"QWidget {\n"
                                          "\n"
                                          "	background-color : #111111;\n"
                                          "\n"
                                          "}")
        self.gridLayout_18 = QGridLayout(self.widgetInterest)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frameInterestContent = QFrame(self.widgetInterest)
        self.frameInterestContent.setObjectName(u"frameInterestContent")
        self.frameInterestContent.setStyleSheet(u"QFrame {\n"
                                                "\n"
                                                "	background-color : #111111;\n"
                                                "}")
        self.frameInterestContent.setFrameShape(QFrame.NoFrame)
        self.frameInterestContent.setFrameShadow(QFrame.Plain)
        self.frameInterestContent.setLineWidth(0)
        self.gridLayout_19 = QGridLayout(self.frameInterestContent)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(9)
        self.gridLayout_19.setVerticalSpacing(0)
        self.gridLayout_19.setContentsMargins(9, 0, 9, 0)
        self.listViewInterest = QListView(self.frameInterestContent)
        self.listViewInterest.setObjectName(u"listViewInterest")
        self.listViewInterest.setStyleSheet(u"QListView {\n"
                                            "	font : 77 13pt \"Microsoft JhengHei UI\";\n"
                                            "	color : #FFFFFF;\n"
                                            "	border-radius : 0px;\n"
                                            "	text-align : left;\n"
                                            "	padding-left: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QListView::hover {\n"
                                            "	color : #4F6FA0;\n"
                                            "}")
        self.listViewInterest.setFrameShadow(QFrame.Plain)
        self.listViewInterest.setDragEnabled(True)
        self.listViewInterest.setDragDropMode(QAbstractItemView.DragDrop)
        self.listViewInterest.setDefaultDropAction(Qt.MoveAction)
        self.listViewInterest.setResizeMode(QListView.Fixed)
        self.listViewInterest.setLayoutMode(QListView.SinglePass)
        self.listViewInterest.setItemAlignment(Qt.AlignLeading)

        self.gridLayout_19.addWidget(self.listViewInterest, 6, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_13, 5, 0, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_31, 1, 0, 1, 1)

        self.labelInterest = QLabel(self.frameInterestContent)
        self.labelInterest.setObjectName(u"labelInterest")
        self.labelInterest.setStyleSheet(u"QLabel {\n"
                                         "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                         "	color : #FFFFFF;\n"
                                         "	border-radius : 0px;\n"
                                         "	text-align : left;\n"
                                         "	padding-right: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel::hover {\n"
                                         "	color : #4F6FA0;\n"
                                         "}\n"
                                         "")

        self.gridLayout_19.addWidget(
            self.labelInterest, 3, 0, 1, 1, Qt.AlignRight)

        self.pushButtonMenu_3 = QPushButton(self.frameInterestContent)
        self.pushButtonMenu_3.setObjectName(u"pushButtonMenu_3")
        self.pushButtonMenu_3.setMinimumSize(QSize(42, 42))
        self.pushButtonMenu_3.setMaximumSize(QSize(42, 42))
        self.pushButtonMenu_3.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: #000000;\n"
                                            "\n"
                                            "	border-top-left-radius: 14px;\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	padding : 10px;\n"
                                            "\n"
                                            "	text-align : left;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "	background-color: #222222;\n"
                                            "	border-top-left-radius: 14px;	\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	text-align : left;\n"
                                            "\n"
                                            "}")
        self.pushButtonMenu_3.setIcon(icon14)
        self.pushButtonMenu_3.setIconSize(QSize(24, 24))

        self.gridLayout_19.addWidget(self.pushButtonMenu_3, 2, 0, 1, 1)

        self.gridLayout_18.addWidget(self.frameInterestContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetInterest)
        self.widgetHistory = QWidget()
        self.widgetHistory.setObjectName(u"widgetHistory")
        self.widgetHistory.setStyleSheet(u"QWidget {\n"
                                         "\n"
                                         "	background-color : #111111;\n"
                                         "\n"
                                         "}")
        self.gridLayout_21 = QGridLayout(self.widgetHistory)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frameHistoryContent = QFrame(self.widgetHistory)
        self.frameHistoryContent.setObjectName(u"frameHistoryContent")
        self.frameHistoryContent.setStyleSheet(u"QFrame {\n"
                                               "\n"
                                               "	background-color : #111111;\n"
                                               "}")
        self.frameHistoryContent.setFrameShape(QFrame.NoFrame)
        self.frameHistoryContent.setFrameShadow(QFrame.Plain)
        self.frameHistoryContent.setLineWidth(0)
        self.gridLayout_20 = QGridLayout(self.frameHistoryContent)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(9)
        self.gridLayout_20.setVerticalSpacing(0)
        self.gridLayout_20.setContentsMargins(9, 0, 9, 0)
        self.verticalSpacer_20 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_20.addItem(self.verticalSpacer_20, 0, 0, 1, 1)

        self.listViewHistory = QListView(self.frameHistoryContent)
        self.listViewHistory.setObjectName(u"listViewHistory")
        self.listViewHistory.setStyleSheet(u"QListView {\n"
                                           "	font : 77 13pt \"Microsoft JhengHei UI\";\n"
                                           "	color : #FFFFFF;\n"
                                           "	border-radius : 0px;\n"
                                           "	text-align : left;\n"
                                           "	padding-left: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QListView::hover {\n"
                                           "	color : #4F6FA0;\n"
                                           "}")
        self.listViewHistory.setFrameShadow(QFrame.Plain)
        self.listViewHistory.setDragEnabled(True)
        self.listViewHistory.setDragDropMode(QAbstractItemView.DragDrop)
        self.listViewHistory.setDefaultDropAction(Qt.MoveAction)
        self.listViewHistory.setResizeMode(QListView.Fixed)
        self.listViewHistory.setLayoutMode(QListView.SinglePass)
        self.listViewHistory.setItemAlignment(Qt.AlignLeading)

        self.gridLayout_20.addWidget(self.listViewHistory, 4, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_20.addItem(self.verticalSpacer_21, 3, 0, 1, 1)

        self.labelHistory = QLabel(self.frameHistoryContent)
        self.labelHistory.setObjectName(u"labelHistory")
        self.labelHistory.setStyleSheet(u"QLabel {\n"
                                        "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                        "	color : #FFFFFF;\n"
                                        "	border-radius : 0px;\n"
                                        "	text-align : left;\n"
                                        "	padding-right: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QLabel::hover {\n"
                                        "	color : #4F6FA0;\n"
                                        "}\n"
                                        "")

        self.gridLayout_20.addWidget(
            self.labelHistory, 2, 0, 1, 1, Qt.AlignRight)

        self.pushButtonMenu_4 = QPushButton(self.frameHistoryContent)
        self.pushButtonMenu_4.setObjectName(u"pushButtonMenu_4")
        self.pushButtonMenu_4.setMinimumSize(QSize(42, 42))
        self.pushButtonMenu_4.setMaximumSize(QSize(42, 42))
        self.pushButtonMenu_4.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: #000000;\n"
                                            "\n"
                                            "	border-top-left-radius: 14px;\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	padding : 10px;\n"
                                            "\n"
                                            "	text-align : left;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "	background-color: #222222;\n"
                                            "	border-top-left-radius: 14px;	\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	text-align : left;\n"
                                            "\n"
                                            "}")
        self.pushButtonMenu_4.setIcon(icon14)
        self.pushButtonMenu_4.setIconSize(QSize(24, 24))

        self.gridLayout_20.addWidget(self.pushButtonMenu_4, 1, 0, 1, 1)

        self.gridLayout_21.addWidget(self.frameHistoryContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetHistory)
        self.widgetSettings = QWidget()
        self.widgetSettings.setObjectName(u"widgetSettings")
        self.widgetSettings.setStyleSheet(u"QWidget {\n"
                                          "\n"
                                          "	background-color : #111111;\n"
                                          "\n"
                                          "}")
        self.gridLayout_27 = QGridLayout(self.widgetSettings)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frameSettingsContent = QFrame(self.widgetSettings)
        self.frameSettingsContent.setObjectName(u"frameSettingsContent")
        self.frameSettingsContent.setStyleSheet(u"QFrame {\n"
                                                "\n"
                                                "	background-color : #111111;\n"
                                                "}")
        self.frameSettingsContent.setFrameShape(QFrame.NoFrame)
        self.frameSettingsContent.setFrameShadow(QFrame.Plain)
        self.frameSettingsContent.setLineWidth(0)
        self.gridLayout_26 = QGridLayout(self.frameSettingsContent)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setHorizontalSpacing(9)
        self.gridLayout_26.setVerticalSpacing(0)
        self.gridLayout_26.setContentsMargins(9, 0, 9, 0)
        self.pushButtonMenu_5 = QPushButton(self.frameSettingsContent)
        self.pushButtonMenu_5.setObjectName(u"pushButtonMenu_5")
        self.pushButtonMenu_5.setMinimumSize(QSize(42, 42))
        self.pushButtonMenu_5.setMaximumSize(QSize(42, 42))
        self.pushButtonMenu_5.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: #000000;\n"
                                            "\n"
                                            "	border-top-left-radius: 14px;\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	padding : 10px;\n"
                                            "\n"
                                            "	text-align : left;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "	background-color: #222222;\n"
                                            "	border-top-left-radius: 14px;	\n"
                                            "	border-bottom-left-radius: 14px;\n"
                                            "	border-top-right-radius: 14px;\n"
                                            "	border-bottom-right-radius: 14px;\n"
                                            "\n"
                                            "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                            "	color: #FFFFFF;\n"
                                            "	text-align : left;\n"
                                            "\n"
                                            "}")
        self.pushButtonMenu_5.setIcon(icon14)
        self.pushButtonMenu_5.setIconSize(QSize(24, 24))

        self.gridLayout_26.addWidget(self.pushButtonMenu_5, 1, 0, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_26.addItem(self.verticalSpacer_30, 3, 0, 1, 1)

        self.groupBoxScanner = QGroupBox(self.frameSettingsContent)
        self.groupBoxScanner.setObjectName(u"groupBoxScanner")
        self.groupBoxScanner.setStyleSheet(u"QGroupBox {\n"
                                           "	font : 77 15pt \"Microsoft JhengHei UI\";\n"
                                           "	color : #FFFFFF;\n"
                                           "	border-radius : 0px;\n"
                                           "	text-align : left;\n"
                                           "	padding-left: 5px;\n"
                                           "}")
        self.gridLayout_28 = QGridLayout(self.groupBoxScanner)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_10 = QLabel(self.groupBoxScanner)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
                                    "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                    "	color : #FFFFFF;\n"
                                    "	border-radius : 0px;\n"
                                    "	text-align : left;\n"
                                    "	padding-left: 5px;\n"
                                    "}\n"
                                    "")

        self.gridLayout_28.addWidget(self.label_10, 4, 0, 1, 1)

        self.labelUser = QLabel(self.groupBoxScanner)
        self.labelUser.setObjectName(u"labelUser")
        self.labelUser.setStyleSheet(u"QLabel {\n"
                                     "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                     "	color : #4F6FA0;\n"
                                     "	border-radius : 0px;\n"
                                     "	text-align : left;\n"
                                     "	padding-left: 5px;\n"
                                     "}\n"
                                     "")

        self.gridLayout_28.addWidget(self.labelUser, 5, 0, 1, 1)

        self.labelPlatform = QLabel(self.groupBoxScanner)
        self.labelPlatform.setObjectName(u"labelPlatform")
        self.labelPlatform.setStyleSheet(u"QLabel {\n"
                                         "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                         "	color : #4F6FA0;\n"
                                         "	border-radius : 0px;\n"
                                         "	text-align : left;\n"
                                         "	padding-left: 5px;\n"
                                         "}\n"
                                         "")

        self.gridLayout_28.addWidget(self.labelPlatform, 13, 0, 1, 1)

        self.pushButtonScanner = QPushButton(self.groupBoxScanner)
        self.pushButtonScanner.setObjectName(u"pushButtonScanner")
        self.pushButtonScanner.setStyleSheet(u"QPushButton{\n"
                                             "	background-color: #5F3E77;\n"
                                             "\n"
                                             "	border-top-left-radius: 14px;\n"
                                             "	border-bottom-left-radius: 14px;\n"
                                             "	border-top-right-radius: 14px;\n"
                                             "	border-bottom-right-radius: 14px;\n"
                                             "\n"
                                             "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                             "	color: #FFFFFF;\n"
                                             "	padding : 10px;\n"
                                             "\n"
                                             "	text-align : left;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "	background-color: #222222;\n"
                                             "	border-top-left-radius: 14px;	\n"
                                             "	border-bottom-left-radius: 14px;\n"
                                             "	border-top-right-radius: 14px;\n"
                                             "	border-bottom-right-radius: 14px;\n"
                                             "\n"
                                             "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                             "	color: #FFFFFF;\n"
                                             "	text-align : left;\n"
                                             "\n"
                                             "}")
        icon15 = QIcon()
        icon15.addFile(u"app/resources/img/icons/24x24/cil-lightbulb.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonScanner.setIcon(icon15)
        self.pushButtonScanner.setIconSize(QSize(24, 24))

        self.gridLayout_28.addWidget(self.pushButtonScanner, 0, 0, 1, 2)

        self.verticalSpacer_27 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_27, 14, 0, 1, 2)

        self.lineEditSession = QLineEdit(self.groupBoxScanner)
        self.lineEditSession.setObjectName(u"lineEditSession")
        self.lineEditSession.setStyleSheet(u"QLineEdit{\n"
                                           "	background-color: #222222;\n"
                                           "\n"
                                           "	border-top-left-radius: 14px;\n"
                                           "	border-bottom-left-radius: 14px;\n"
                                           "	border-top-right-radius: 14px;\n"
                                           "	border-bottom-right-radius: 14px;\n"
                                           "\n"
                                           "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                           "	color: #FFFFFF;\n"
                                           "	padding : 10px;\n"
                                           "\n"
                                           "	text-align : left;\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:hover{\n"
                                           "	background-color: #444444;\n"
                                           "	border-top-left-radius: 14px;	\n"
                                           "	border-bottom-left-radius: 14px;\n"
                                           "	border-top-right-radius: 14px;\n"
                                           "	border-bottom-right-radius: 14px;\n"
                                           "\n"
                                           "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                           "	color: #FFFFFF;\n"
                                           "	text-align : left;\n"
                                           "\n"
                                           "}")

        self.gridLayout_28.addWidget(self.lineEditSession, 2, 1, 1, 1)

        self.labelSystem = QLabel(self.groupBoxScanner)
        self.labelSystem.setObjectName(u"labelSystem")
        self.labelSystem.setStyleSheet(u"QLabel {\n"
                                       "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                       "	color : #4F6FA0;\n"
                                       "	border-radius : 0px;\n"
                                       "	text-align : left;\n"
                                       "	padding-left: 5px;\n"
                                       "}\n"
                                       "")

        self.gridLayout_28.addWidget(self.labelSystem, 7, 0, 1, 1)

        self.labelMachine = QLabel(self.groupBoxScanner)
        self.labelMachine.setObjectName(u"labelMachine")
        self.labelMachine.setStyleSheet(u"QLabel {\n"
                                        "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                        "	color : #4F6FA0;\n"
                                        "	border-radius : 0px;\n"
                                        "	text-align : left;\n"
                                        "	padding-left: 5px;\n"
                                        "}\n"
                                        "")

        self.gridLayout_28.addWidget(self.labelMachine, 11, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBoxScanner)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: #222222;\n"
                                      "\n"
                                      "	border-top-left-radius: 14px;\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	padding : 10px;\n"
                                      "\n"
                                      "	text-align : left;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{\n"
                                      "	background-color: #444444;\n"
                                      "	border-top-left-radius: 14px;	\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	text-align : left;\n"
                                      "}")

        self.gridLayout_28.addWidget(self.lineEdit_9, 13, 1, 1, 1)

        self.labelOS = QLabel(self.groupBoxScanner)
        self.labelOS.setObjectName(u"labelOS")
        self.labelOS.setStyleSheet(u"QLabel {\n"
                                   "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                   "	color : #4F6FA0;\n"
                                   "	border-radius : 0px;\n"
                                   "	text-align : left;\n"
                                   "	padding-left: 5px;\n"
                                   "}\n"
                                   "")

        self.gridLayout_28.addWidget(self.labelOS, 6, 0, 1, 1)

        self.lineEditUser = QLineEdit(self.groupBoxScanner)
        self.lineEditUser.setObjectName(u"lineEditUser")
        self.lineEditUser.setStyleSheet(u"QLineEdit {\n"
                                        "	background-color: #222222;\n"
                                        "\n"
                                        "	border-top-left-radius: 14px;\n"
                                        "	border-bottom-left-radius: 14px;\n"
                                        "	border-top-right-radius: 14px;\n"
                                        "	border-bottom-right-radius: 14px;\n"
                                        "\n"
                                        "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                        "	color: #FFFFFF;\n"
                                        "	padding : 10px;\n"
                                        "\n"
                                        "	text-align : left;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit:hover{\n"
                                        "	background-color: #444444;\n"
                                        "	border-top-left-radius: 14px;	\n"
                                        "	border-bottom-left-radius: 14px;\n"
                                        "	border-top-right-radius: 14px;\n"
                                        "	border-bottom-right-radius: 14px;\n"
                                        "\n"
                                        "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                        "	color: #FFFFFF;\n"
                                        "	text-align : left;\n"
                                        "}")

        self.gridLayout_28.addWidget(self.lineEditUser, 5, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBoxScanner)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: #222222;\n"
                                      "\n"
                                      "	border-top-left-radius: 14px;\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	padding : 10px;\n"
                                      "\n"
                                      "	text-align : left;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{\n"
                                      "	background-color: #444444;\n"
                                      "	border-top-left-radius: 14px;	\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	text-align : left;\n"
                                      "}")

        self.gridLayout_28.addWidget(self.lineEdit_5, 9, 1, 1, 1)

        self.labelVersion = QLabel(self.groupBoxScanner)
        self.labelVersion.setObjectName(u"labelVersion")
        self.labelVersion.setStyleSheet(u"QLabel {\n"
                                        "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                        "	color : #4F6FA0;\n"
                                        "	border-radius : 0px;\n"
                                        "	text-align : left;\n"
                                        "	padding-left: 5px;\n"
                                        "}\n"
                                        "")

        self.gridLayout_28.addWidget(self.labelVersion, 8, 0, 1, 1)

        self.labelNode = QLabel(self.groupBoxScanner)
        self.labelNode.setObjectName(u"labelNode")
        self.labelNode.setStyleSheet(u"QLabel {\n"
                                     "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                     "	color : #4F6FA0;\n"
                                     "	border-radius : 0px;\n"
                                     "	text-align : left;\n"
                                     "	padding-left: 5px;\n"
                                     "}\n"
                                     "")

        self.gridLayout_28.addWidget(self.labelNode, 10, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBoxScanner)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: #222222;\n"
                                    "\n"
                                    "	border-top-left-radius: 14px;\n"
                                    "	border-bottom-left-radius: 14px;\n"
                                    "	border-top-right-radius: 14px;\n"
                                    "	border-bottom-right-radius: 14px;\n"
                                    "\n"
                                    "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                    "	color: #FFFFFF;\n"
                                    "	padding : 10px;\n"
                                    "\n"
                                    "	text-align : left;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:hover{\n"
                                    "	background-color: #444444;\n"
                                    "	border-top-left-radius: 14px;	\n"
                                    "	border-bottom-left-radius: 14px;\n"
                                    "	border-top-right-radius: 14px;\n"
                                    "	border-bottom-right-radius: 14px;\n"
                                    "\n"
                                    "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                    "	color: #FFFFFF;\n"
                                    "	text-align : left;\n"
                                    "}")

        self.gridLayout_28.addWidget(self.lineEdit, 6, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBoxScanner)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: #222222;\n"
                                      "\n"
                                      "	border-top-left-radius: 14px;\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	padding : 10px;\n"
                                      "\n"
                                      "	text-align : left;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{\n"
                                      "	background-color: #444444;\n"
                                      "	border-top-left-radius: 14px;	\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	text-align : left;\n"
                                      "}")

        self.gridLayout_28.addWidget(self.lineEdit_4, 8, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_28.addItem(self.verticalSpacer_28, 1, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.groupBoxScanner)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: #222222;\n"
                                      "\n"
                                      "	border-top-left-radius: 14px;\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	padding : 10px;\n"
                                      "\n"
                                      "	text-align : left;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{\n"
                                      "	background-color: #444444;\n"
                                      "	border-top-left-radius: 14px;	\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	text-align : left;\n"
                                      "}")

        self.gridLayout_28.addWidget(self.lineEdit_3, 7, 1, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_28.addItem(self.verticalSpacer_29, 3, 0, 1, 2)

        self.labelSession = QLabel(self.groupBoxScanner)
        self.labelSession.setObjectName(u"labelSession")
        self.labelSession.setStyleSheet(u"QLabel {\n"
                                        "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                        "	color : #4F6FA0;\n"
                                        "	border-radius : 0px;\n"
                                        "	text-align : left;\n"
                                        "	padding-left: 5px;\n"
                                        "}\n"
                                        "")

        self.gridLayout_28.addWidget(self.labelSession, 2, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBoxScanner)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: #222222;\n"
                                      "\n"
                                      "	border-top-left-radius: 14px;\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	padding : 10px;\n"
                                      "\n"
                                      "	text-align : left;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{\n"
                                      "	background-color: #444444;\n"
                                      "	border-top-left-radius: 14px;	\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	text-align : left;\n"
                                      "}")

        self.gridLayout_28.addWidget(self.lineEdit_8, 12, 1, 1, 1)

        self.labelArchitecture = QLabel(self.groupBoxScanner)
        self.labelArchitecture.setObjectName(u"labelArchitecture")
        self.labelArchitecture.setStyleSheet(u"QLabel {\n"
                                             "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                             "	color : #4F6FA0;\n"
                                             "	border-radius : 0px;\n"
                                             "	text-align : left;\n"
                                             "	padding-left: 5px;\n"
                                             "}\n"
                                             "")

        self.gridLayout_28.addWidget(self.labelArchitecture, 12, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBoxScanner)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: #222222;\n"
                                      "\n"
                                      "	border-top-left-radius: 14px;\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	padding : 10px;\n"
                                      "\n"
                                      "	text-align : left;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{\n"
                                      "	background-color: #444444;\n"
                                      "	border-top-left-radius: 14px;	\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	text-align : left;\n"
                                      "}")

        self.gridLayout_28.addWidget(self.lineEdit_6, 10, 1, 1, 1)

        self.labelProcessor = QLabel(self.groupBoxScanner)
        self.labelProcessor.setObjectName(u"labelProcessor")
        self.labelProcessor.setStyleSheet(u"QLabel {\n"
                                          "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                          "	color : #4F6FA0;\n"
                                          "	border-radius : 0px;\n"
                                          "	text-align : left;\n"
                                          "	padding-left: 5px;\n"
                                          "}\n"
                                          "")

        self.gridLayout_28.addWidget(self.labelProcessor, 9, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBoxScanner)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: #222222;\n"
                                      "\n"
                                      "	border-top-left-radius: 14px;\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	padding : 10px;\n"
                                      "\n"
                                      "	text-align : left;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{\n"
                                      "	background-color: #444444;\n"
                                      "	border-top-left-radius: 14px;	\n"
                                      "	border-bottom-left-radius: 14px;\n"
                                      "	border-top-right-radius: 14px;\n"
                                      "	border-bottom-right-radius: 14px;\n"
                                      "\n"
                                      "	font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                      "	color: #FFFFFF;\n"
                                      "	text-align : left;\n"
                                      "}")

        self.gridLayout_28.addWidget(self.lineEdit_7, 11, 1, 1, 1)

        self.gridLayout_26.addWidget(self.groupBoxScanner, 4, 0, 1, 1)

        self.labelSettings = QLabel(self.frameSettingsContent)
        self.labelSettings.setObjectName(u"labelSettings")
        self.labelSettings.setStyleSheet(u"QLabel {\n"
                                         "	font : 77 18pt \"Microsoft JhengHei UI\";\n"
                                         "	color : #FFFFFF;\n"
                                         "	border-radius : 0px;\n"
                                         "	text-align : left;\n"
                                         "	padding-right: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel::hover {\n"
                                         "	color : #4F6FA0;\n"
                                         "}\n"
                                         "")

        self.gridLayout_26.addWidget(
            self.labelSettings, 2, 0, 1, 1, Qt.AlignRight)

        self.verticalSpacer_26 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_26.addItem(self.verticalSpacer_26, 0, 0, 1, 1)

        self.gridLayout_27.addWidget(self.frameSettingsContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetSettings)

        self.gridLayout_2.addWidget(self.stackedWidgetContainer, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frameContainer, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        self.stackedWidgetContainer.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.pushButtonNext.setText("")
        self.pushButtonPrevious.setText("")
        self.pushButtonPlay.setText("")
        self.labelDuration.setText("")
        self.labelTime.setText("")
        self.labelBitrate.setText("")
        self.pushButtonVolume.setText("")
        self.pushButtonAddFavorite.setText("")
        self.labelCodec.setText("")
        self.pushButtonMenu.setText(QCoreApplication.translate(
            "MainWindow", u"PushButton", None))
        self.labelCoverArt.setText("")
        self.labelPlaylist.setText(
            QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.pushButtonAddFile.setText(QCoreApplication.translate(
            "MainWindow", u"Agregar archivo", None))
        self.labelFileOptions.setText(
            QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.pushButtonFavorites.setText(
            QCoreApplication.translate("MainWindow", u"Favoritos", None))
        self.pushButtonPlaylists.setText(
            QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.pushButtonRecentlyPlayed.setText(QCoreApplication.translate(
            "MainWindow", u"Escuchado recientemente", None))
        self.pushButtonAddDirectory.setText(
            QCoreApplication.translate("MainWindow", u"Agregar carpeta", None))
        self.labelMusic.setText(QCoreApplication.translate(
            "MainWindow", u"Musica", None))
        self.pushButtonAddPath.setText(
            QCoreApplication.translate("MainWindow", u"Agregar ruta", None))
        self.pushButtonSaveActualPlaylist.setText(
            QCoreApplication.translate("MainWindow", u"Guarda playlist actual", None))
        self.pushButtonSearch.setText(
            QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButtonSettings.setText("")
        self.pushButtonSong.setText(QCoreApplication.translate(
            "MainWindow", u"PushButton", None))
        self.labelPlaylisr.setText(
            QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.pushButtonMenu_2.setText("")
        self.labelInterest.setText(QCoreApplication.translate(
            "MainWindow", u"Favoritos", None))
        self.pushButtonMenu_3.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelHistory.setText(QCoreApplication.translate(
            "MainWindow", u"Historial", None))
        self.pushButtonMenu_4.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButtonMenu_5.setText("")
        self.groupBoxScanner.setTitle("")
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Sistema", None))
        self.labelUser.setText(QCoreApplication.translate(
            "MainWindow", u"Usuario", None))
        self.labelPlatform.setText(QCoreApplication.translate(
            "MainWindow", u"Plataforma", None))
        self.pushButtonScanner.setText(QCoreApplication.translate(
            "MainWindow", u"Escanear musica", None))
        self.labelSystem.setText(QCoreApplication.translate(
            "MainWindow", u"Sistema", None))
        self.labelMachine.setText(
            QCoreApplication.translate("MainWindow", u"Maquina", None))
        self.labelOS.setText(QCoreApplication.translate(
            "MainWindow", u"Sistema Operativo", None))
        self.labelVersion.setText(
            QCoreApplication.translate("MainWindow", u"Version", None))
        self.labelNode.setText(
            QCoreApplication.translate("MainWindow", u"Nodo", None))
        self.labelSession.setText(
            QCoreApplication.translate("MainWindow", u"Sesion", None))
        self.labelArchitecture.setText(
            QCoreApplication.translate("MainWindow", u"Arquitectura", None))
        self.labelProcessor.setText(QCoreApplication.translate(
            "MainWindow", u"Procesador", None))
        self.labelSettings.setText(
            QCoreApplication.translate("MainWindow", u"Ajustes", None))
    # retranslateUi
