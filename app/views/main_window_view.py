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
            return self.stackedWidgetContainer.setCurrentWidget(self.widgetLibrary)

        elif event.key() == QtCore.Qt.Key_F2:
            return self.stackedWidgetContainer.setCurrentWidget(self.widgetContainer)


        else:
            super().keyPressEvent(event)

    def setupUi(self):
        self.setObjectName("mainWindow")
        self.setEnabled(True)
        self.resize(552, 896)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
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
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetContainer = QStackedWidget(self.frameContainer)
        self.stackedWidgetContainer.setObjectName(u"stackedWidgetContainer")
        self.stackedWidgetContainer.setStyleSheet(u"")
        self.stackedWidgetContainer.setLineWidth(0)
        self.widgetContainer = QWidget()
        self.widgetContainer.setObjectName(u"widgetContainer")
        self.widgetContainer.setStyleSheet(u"QWidget {\n"
"\n"
"	background-color : #111111;\n"
"\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widgetContainer)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.framePlayerContent = QFrame(self.widgetContainer)
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
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.framePlayContent = QFrame(self.framePlayerContent)
        self.framePlayContent.setObjectName(u"framePlayContent")
        self.framePlayContent.setFrameShape(QFrame.NoFrame)
        self.framePlayContent.setFrameShadow(QFrame.Plain)
        self.framePlayContent.setLineWidth(0)
        self.gridLayout_9 = QGridLayout(self.framePlayContent)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frameCoverArt = QFrame(self.framePlayContent)
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
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_7, 2, 3, 1, 1)

        self.labelCoverArt = QLabel(self.frameCoverArt)
        self.labelCoverArt.setObjectName(u"labelCoverArt")
        self.labelCoverArt.setMinimumSize(QSize(450, 450))
        self.labelCoverArt.setMaximumSize(QSize(450, 450))
        self.labelCoverArt.setSizeIncrement(QSize(0, 0))
        self.labelCoverArt.setBaseSize(QSize(100, 100))
        self.labelCoverArt.setAutoFillBackground(False)
        self.labelCoverArt.setLineWidth(0)
        self.labelCoverArt.setScaledContents(True)
        self.labelCoverArt.setWordWrap(False)

        self.gridLayout_11.addWidget(self.labelCoverArt, 2, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_6, 2, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_14, 0, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 1, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frameCoverArt, 0, 0, 1, 1)

        self.frameSong = QFrame(self.framePlayContent)
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

        self.gridLayout_10.addWidget(self.labelArtistSong, 3, 0, 1, 1, Qt.AlignHCenter)

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

        self.gridLayout_10.addWidget(self.labelTitleSong, 1, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer, 0, 0, 1, 1)

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

        self.gridLayout_10.addWidget(self.labelAlbumSong, 2, 0, 1, 1, Qt.AlignHCenter)

        self.frameSongTime = QFrame(self.frameSong)
        self.frameSongTime.setObjectName(u"frameSongTime")
        self.frameSongTime.setFrameShape(QFrame.StyledPanel)
        self.frameSongTime.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frameSongTime)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalSliderTime = QSlider(self.frameSongTime)
        self.horizontalSliderTime.setObjectName(u"horizontalSliderTime")
        self.horizontalSliderTime.setMinimumSize(QSize(300, 0))
        self.horizontalSliderTime.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	border: 1px solid #333333;\n"
"	height: 4px;\n"
"\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	width : 12px;\n"
"	height : 12px;\n"
"	background-color : #111111;\n"
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
        icon = QIcon()
        icon.addFile(u"app/resources/img/icons/24x24/cil-volume-high.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonVolume.setIcon(icon)
        self.pushButtonVolume.setIconSize(QSize(24, 24))

        self.gridLayout_12.addWidget(self.pushButtonVolume, 0, 0, 1, 1)

        self.horizontalSliderVolume = QSlider(self.frameVolume)
        self.horizontalSliderVolume.setObjectName(u"horizontalSliderVolume")
        self.horizontalSliderVolume.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	border: 1px solid #333333;\n"
"	height: 4px;\n"
"\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	width : 2px;\n"
"	height : 8px;\n"
"	background-color : #111111;\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"	background: #333333;\n"
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
        icon1 = QIcon()
        icon1.addFile(u"app/resources/img/icons/24x24/cil-heart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddFavorite.setIcon(icon1)
        self.pushButtonAddFavorite.setIconSize(QSize(24, 24))

        self.gridLayout_12.addWidget(self.pushButtonAddFavorite, 0, 2, 1, 1)


        self.gridLayout_14.addWidget(self.frameVolume, 4, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_5, 0, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_3, 1, 2, 1, 1)

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
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        icon2 = QIcon()
        icon2.addFile(u"app/resources/img/icons/24x24/cil-media-step-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNext.setIcon(icon2)
        self.pushButtonNext.setIconSize(QSize(24, 24))
        self.pushButtonNext.setFlat(True)

        self.gridLayout_6.addWidget(self.pushButtonNext, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        icon3 = QIcon()
        icon3.addFile(u"app/resources/img/icons/24x24/cil-media-step-backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPrevious.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u"app/resources/img/icons/24x24/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPlay.setIcon(icon4)
        self.pushButtonPlay.setIconSize(QSize(24, 24))
        self.pushButtonPlay.setFlat(True)

        self.gridLayout_6.addWidget(self.pushButtonPlay, 0, 3, 1, 1)


        self.gridLayout_14.addWidget(self.framePlayerFunction, 2, 2, 1, 1)

        self.labelBitrate = QLabel(self.frameSongTime)
        self.labelBitrate.setObjectName(u"labelBitrate")
        self.labelBitrate.setStyleSheet(u"QLabel {\n"
"	font : 22 11pt \"Microsoft JhengHei UI\" bold;\n"
"	color : #FFFFFF;\n"
"	border-radius : 0px;\n"
"	text-align : left;\n"
"	padding-left: 5px;\n"
"}")

        self.gridLayout_14.addWidget(self.labelBitrate, 5, 2, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 3, 2, 1, 1)

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

        self.labelCodec = QLabel(self.frameSongTime)
        self.labelCodec.setObjectName(u"labelCodec")
        self.labelCodec.setStyleSheet(u"QLabel {\n"
"	font : 22 9pt \"Microsoft JhengHei UI\" bold;\n"
"	color : #FFFFFF;\n"
"	border-radius : 0px;\n"
"	text-align : left;\n"
"	padding-left: 5px;\n"
"}")

        self.gridLayout_14.addWidget(self.labelCodec, 6, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.labelTime.raise_()
        self.framePlayerFunction.raise_()
        self.frameVolume.raise_()
        self.labelCodec.raise_()
        self.labelBitrate.raise_()
        self.horizontalSliderTime.raise_()
        self.labelDuration.raise_()

        self.gridLayout_10.addWidget(self.frameSongTime, 5, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frameSong, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.framePlayContent, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.framePlayerContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetContainer)
        self.widgetLibrary = QWidget()
        self.widgetLibrary.setObjectName(u"widgetLibrary")
        self.widgetLibrary.setStyleSheet(u"QWidget {\n"
"\n"
"	background-color : #111111;\n"
"\n"
"}")
        self.gridLayout_7 = QGridLayout(self.widgetLibrary)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frameLibraryContent = QFrame(self.widgetLibrary)
        self.frameLibraryContent.setObjectName(u"frameLibraryContent")
        self.frameLibraryContent.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color : #111111;\n"
"}")
        self.frameLibraryContent.setFrameShape(QFrame.NoFrame)
        self.frameLibraryContent.setFrameShadow(QFrame.Plain)
        self.frameLibraryContent.setLineWidth(0)
        self.gridLayout_13 = QGridLayout(self.frameLibraryContent)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(9)
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setContentsMargins(9, 0, 9, 0)
        self.labelPlaylist = QLabel(self.frameLibraryContent)
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

        self.gridLayout_13.addWidget(self.labelPlaylist, 3, 1, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_13.addItem(self.verticalSpacer_8, 0, 0, 1, 11)

        self.frameOptions = QFrame(self.frameLibraryContent)
        self.frameOptions.setObjectName(u"frameOptions")
        self.frameOptions.setFrameShape(QFrame.NoFrame)
        self.frameOptions.setFrameShadow(QFrame.Plain)
        self.frameOptions.setLineWidth(0)
        self.gridLayout_15 = QGridLayout(self.frameOptions)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_9, 7, 0, 1, 1)

        self.pushButtonPlaylists = QPushButton(self.frameOptions)
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
        icon5 = QIcon()
        icon5.addFile(u"app/resources/img/icons/24x24/cil-list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPlaylists.setIcon(icon5)
        self.pushButtonPlaylists.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonPlaylists, 13, 0, 1, 1)

        self.labelMusic = QLabel(self.frameOptions)
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

        self.pushButtonAddPath = QPushButton(self.frameOptions)
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
        icon6 = QIcon()
        icon6.addFile(u"app/resources/img/icons/24x24/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddPath.setIcon(icon6)
        self.pushButtonAddPath.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddPath, 5, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_16, 9, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_15, 2, 0, 1, 1)

        self.pushButtonAlbums = QPushButton(self.frameOptions)
        self.pushButtonAlbums.setObjectName(u"pushButtonAlbums")
        self.pushButtonAlbums.setStyleSheet(u"QPushButton{\n"
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
        icon7.addFile(u"app/resources/img/icons/24x24/cil-library.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAlbums.setIcon(icon7)
        self.pushButtonAlbums.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAlbums, 11, 0, 1, 1)

        self.pushButtonSongs = QPushButton(self.frameOptions)
        self.pushButtonSongs.setObjectName(u"pushButtonSongs")
        self.pushButtonSongs.setStyleSheet(u"QPushButton{\n"
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
        icon8.addFile(u"app/resources/img/icons/24x24/cil-music-note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSongs.setIcon(icon8)
        self.pushButtonSongs.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonSongs, 12, 0, 1, 1)

        self.pushButtonAddDirectory = QPushButton(self.frameOptions)
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
        icon9 = QIcon()
        icon9.addFile(u"app/resources/img/icons/24x24/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddDirectory.setIcon(icon9)
        self.pushButtonAddDirectory.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddDirectory, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_6, 15, 0, 1, 1)

        self.pushButtonArtists = QPushButton(self.frameOptions)
        self.pushButtonArtists.setObjectName(u"pushButtonArtists")
        self.pushButtonArtists.setStyleSheet(u"QPushButton{\n"
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
        icon10.addFile(u"app/resources/img/icons/24x24/cil-people.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonArtists.setIcon(icon10)
        self.pushButtonArtists.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonArtists, 10, 0, 1, 1)

        self.labelFileOptions = QLabel(self.frameOptions)
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

        self.gridLayout_15.addWidget(self.labelFileOptions, 1, 0, 1, 1, Qt.AlignLeft)

        self.pushButtonFavorites = QPushButton(self.frameOptions)
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
        self.pushButtonFavorites.setIcon(icon1)
        self.pushButtonFavorites.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonFavorites, 14, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_18, 6, 0, 1, 1)

        self.pushButtonAddFile = QPushButton(self.frameOptions)
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
        icon11 = QIcon()
        icon11.addFile(u"app/resources/img/icons/24x24/cil-copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddFile.setIcon(icon11)
        self.pushButtonAddFile.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddFile, 3, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frameOptions, 2, 0, 1, 11)

        self.lineEditSearcher = QLineEdit(self.frameLibraryContent)
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

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_9, 5, 3, 1, 1)

        self.pushButtonSaveActualPlaylist = QPushButton(self.frameLibraryContent)
        self.pushButtonSaveActualPlaylist.setObjectName(u"pushButtonSaveActualPlaylist")
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
        icon12 = QIcon()
        icon12.addFile(u"app/resources/img/icons/24x24/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveActualPlaylist.setIcon(icon12)
        self.pushButtonSaveActualPlaylist.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.pushButtonSaveActualPlaylist, 3, 5, 1, 4)

        self.listViewPlaylist = QListView(self.frameLibraryContent)
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

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_10, 4, 1, 1, 8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 3, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_13, 6, 1, 1, 8)

        self.pushButtonSearch = QPushButton(self.frameLibraryContent)
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
        icon13 = QIcon()
        icon13.addFile(u"app/resources/img/icons/24x24/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSearch.setIcon(icon13)
        self.pushButtonSearch.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.pushButtonSearch, 5, 5, 1, 4)

        self.pushButtonSettings = QPushButton(self.frameLibraryContent)
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
        icon14 = QIcon()
        icon14.addFile(u"app/resources/img/icons/24x24/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSettings.setIcon(icon14)
        self.pushButtonSettings.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.pushButtonSettings, 1, 7, 1, 1)

        self.pushButtonSong = QPushButton(self.frameLibraryContent)
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
        self.pushButtonSong.setIcon(icon)
        self.pushButtonSong.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.pushButtonSong, 1, 8, 1, 1)


        self.gridLayout_7.addWidget(self.frameLibraryContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetLibrary)
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
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
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

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_11, 4, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

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

        self.gridLayout_17.addWidget(self.labelPlaylisr, 3, 0, 1, 1, Qt.AlignRight)

        self.pushButton = QPushButton(self.framePlaylistContent)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(42, 42))
        self.pushButton.setMaximumSize(QSize(42, 42))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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
        icon15 = QIcon()
        icon15.addFile(u"app/resources/img/icons/24x24/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon15)
        self.pushButton.setIconSize(QSize(24, 24))

        self.gridLayout_17.addWidget(self.pushButton, 2, 0, 1, 1)


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
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
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

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_13, 5, 0, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

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

        self.gridLayout_19.addWidget(self.labelInterest, 3, 0, 1, 1, Qt.AlignRight)

        self.pushButton_3 = QPushButton(self.frameInterestContent)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(42, 42))
        self.pushButton_3.setMaximumSize(QSize(42, 42))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_3.setIcon(icon15)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.gridLayout_19.addWidget(self.pushButton_3, 2, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frameInterestContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetInterest)
        self.widgetArtists = QWidget()
        self.widgetArtists.setObjectName(u"widgetArtists")
        self.widgetArtists.setStyleSheet(u"QWidget {\n"
"\n"
"	background-color : #111111;\n"
"\n"
"}")
        self.gridLayout_21 = QGridLayout(self.widgetArtists)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frameArtistsContent = QFrame(self.widgetArtists)
        self.frameArtistsContent.setObjectName(u"frameArtistsContent")
        self.frameArtistsContent.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color : #111111;\n"
"}")
        self.frameArtistsContent.setFrameShape(QFrame.NoFrame)
        self.frameArtistsContent.setFrameShadow(QFrame.Plain)
        self.frameArtistsContent.setLineWidth(0)
        self.gridLayout_20 = QGridLayout(self.frameArtistsContent)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_20 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_20.addItem(self.verticalSpacer_20, 0, 0, 1, 1)

        self.listViewArtists = QListView(self.frameArtistsContent)
        self.listViewArtists.setObjectName(u"listViewArtists")
        self.listViewArtists.setStyleSheet(u"QListView {\n"
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
        self.listViewArtists.setFrameShadow(QFrame.Plain)
        self.listViewArtists.setDragEnabled(True)
        self.listViewArtists.setDragDropMode(QAbstractItemView.DragDrop)
        self.listViewArtists.setDefaultDropAction(Qt.MoveAction)
        self.listViewArtists.setResizeMode(QListView.Fixed)
        self.listViewArtists.setLayoutMode(QListView.SinglePass)
        self.listViewArtists.setItemAlignment(Qt.AlignLeading)

        self.gridLayout_20.addWidget(self.listViewArtists, 4, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_20.addItem(self.verticalSpacer_21, 3, 0, 1, 1)

        self.labelArtists = QLabel(self.frameArtistsContent)
        self.labelArtists.setObjectName(u"labelArtists")
        self.labelArtists.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_20.addWidget(self.labelArtists, 2, 0, 1, 1, Qt.AlignRight)

        self.pushButton_4 = QPushButton(self.frameArtistsContent)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(42, 42))
        self.pushButton_4.setMaximumSize(QSize(42, 42))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_4.setIcon(icon15)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.gridLayout_20.addWidget(self.pushButton_4, 1, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frameArtistsContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetArtists)
        self.widgetAlbum = QWidget()
        self.widgetAlbum.setObjectName(u"widgetAlbum")
        self.widgetAlbum.setStyleSheet(u"QWidget {\n"
"\n"
"	background-color : #111111;\n"
"\n"
"}")
        self.gridLayout_23 = QGridLayout(self.widgetAlbum)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frameAlbumContent = QFrame(self.widgetAlbum)
        self.frameAlbumContent.setObjectName(u"frameAlbumContent")
        self.frameAlbumContent.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color : #111111;\n"
"}")
        self.frameAlbumContent.setFrameShape(QFrame.NoFrame)
        self.frameAlbumContent.setFrameShadow(QFrame.Plain)
        self.frameAlbumContent.setLineWidth(0)
        self.gridLayout_22 = QGridLayout(self.frameAlbumContent)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frameAlbum = QFrame(self.frameAlbumContent)
        self.frameAlbum.setObjectName(u"frameAlbum")
        self.frameAlbum.setFrameShape(QFrame.StyledPanel)
        self.frameAlbum.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frameAlbum)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_29.addItem(self.verticalSpacer_7, 6, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_29.addItem(self.verticalSpacer_17, 4, 0, 1, 1)

        self.listViewAlbumSongs = QListView(self.frameAlbum)
        self.listViewAlbumSongs.setObjectName(u"listViewAlbumSongs")
        self.listViewAlbumSongs.setFrameShape(QFrame.NoFrame)
        self.listViewAlbumSongs.setFrameShadow(QFrame.Plain)
        self.listViewAlbumSongs.setLineWidth(0)

        self.gridLayout_29.addWidget(self.listViewAlbumSongs, 5, 0, 1, 1)

        self.labelAlbumArtist = QLabel(self.frameAlbum)
        self.labelAlbumArtist.setObjectName(u"labelAlbumArtist")
        self.labelAlbumArtist.setStyleSheet(u"QLabel {\n"
"	font : 77 15pt \"Microsoft JhengHei UI\";\n"
"	color : #4F6FA0;\n"
"	border-radius : 0px;\n"
"	text-align : left;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"")

        self.gridLayout_29.addWidget(self.labelAlbumArtist, 3, 0, 1, 1, Qt.AlignHCenter)

        self.labelAlbumCoverArt = QLabel(self.frameAlbum)
        self.labelAlbumCoverArt.setObjectName(u"labelAlbumCoverArt")
        self.labelAlbumCoverArt.setMinimumSize(QSize(300, 300))
        self.labelAlbumCoverArt.setMaximumSize(QSize(300, 300))
        self.labelAlbumCoverArt.setSizeIncrement(QSize(400, 400))
        self.labelAlbumCoverArt.setPixmap(QPixmap(u"../img/default/cover-art.png"))
        self.labelAlbumCoverArt.setScaledContents(True)

        self.gridLayout_29.addWidget(self.labelAlbumCoverArt, 0, 0, 1, 1, Qt.AlignHCenter)

        self.labelAlbumTitle = QLabel(self.frameAlbum)
        self.labelAlbumTitle.setObjectName(u"labelAlbumTitle")
        self.labelAlbumTitle.setStyleSheet(u"QLabel {\n"
"	font : 77 20pt \"Microsoft JhengHei UI\";\n"
"	color : #FFFFFF;\n"
"	border-radius : 0px;\n"
"	text-align : left;\n"
"	padding-left: 5px;\n"
"}")

        self.gridLayout_29.addWidget(self.labelAlbumTitle, 2, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_19 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_29.addItem(self.verticalSpacer_19, 1, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frameAlbum, 4, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_22.addItem(self.verticalSpacer_23, 3, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_22.addItem(self.verticalSpacer_22, 0, 0, 1, 1)

        self.labelAlbum = QLabel(self.frameAlbumContent)
        self.labelAlbum.setObjectName(u"labelAlbum")
        self.labelAlbum.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_22.addWidget(self.labelAlbum, 2, 0, 1, 1, Qt.AlignRight)

        self.pushButton_5 = QPushButton(self.frameAlbumContent)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(42, 42))
        self.pushButton_5.setMaximumSize(QSize(42, 42))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_5.setIcon(icon15)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.gridLayout_22.addWidget(self.pushButton_5, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frameAlbumContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetAlbum)
        self.widgetSongs = QWidget()
        self.widgetSongs.setObjectName(u"widgetSongs")
        self.widgetSongs.setStyleSheet(u"QWidget {\n"
"\n"
"	background-color : #111111;\n"
"\n"
"}")
        self.gridLayout_25 = QGridLayout(self.widgetSongs)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frameSongsContent = QFrame(self.widgetSongs)
        self.frameSongsContent.setObjectName(u"frameSongsContent")
        self.frameSongsContent.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color : #111111;\n"
"}")
        self.frameSongsContent.setFrameShape(QFrame.NoFrame)
        self.frameSongsContent.setFrameShadow(QFrame.Plain)
        self.frameSongsContent.setLineWidth(0)
        self.gridLayout_24 = QGridLayout(self.frameSongsContent)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.listViewSongs = QListView(self.frameSongsContent)
        self.listViewSongs.setObjectName(u"listViewSongs")
        self.listViewSongs.setStyleSheet(u"QListView {\n"
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
        self.listViewSongs.setFrameShadow(QFrame.Plain)
        self.listViewSongs.setDragEnabled(True)
        self.listViewSongs.setDragDropMode(QAbstractItemView.DragDrop)
        self.listViewSongs.setDefaultDropAction(Qt.MoveAction)
        self.listViewSongs.setResizeMode(QListView.Fixed)
        self.listViewSongs.setLayoutMode(QListView.SinglePass)
        self.listViewSongs.setItemAlignment(Qt.AlignLeading)

        self.gridLayout_24.addWidget(self.listViewSongs, 4, 0, 1, 1)

        self.labelSongs = QLabel(self.frameSongsContent)
        self.labelSongs.setObjectName(u"labelSongs")
        self.labelSongs.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_24.addWidget(self.labelSongs, 2, 0, 1, 1, Qt.AlignRight)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_24.addItem(self.verticalSpacer_25, 3, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_24.addItem(self.verticalSpacer_24, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frameSongsContent)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(42, 42))
        self.pushButton_6.setMaximumSize(QSize(42, 42))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_6.setIcon(icon15)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.gridLayout_24.addWidget(self.pushButton_6, 1, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frameSongsContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetSongs)
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
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
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

        self.verticalSpacer_29 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_28.addItem(self.verticalSpacer_29, 3, 0, 1, 2)

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

        self.pushButtonScanner = QPushButton(self.groupBoxScanner)
        self.pushButtonScanner.setObjectName(u"pushButtonScanner")
        self.pushButtonScanner.setStyleSheet(u"QPushButton{\n"
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
        icon16 = QIcon()
        icon16.addFile(u"app/resources/img/icons/24x24/cil-lightbulb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonScanner.setIcon(icon16)
        self.pushButtonScanner.setIconSize(QSize(24, 24))

        self.gridLayout_28.addWidget(self.pushButtonScanner, 0, 0, 1, 2)

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

        self.verticalSpacer_28 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_28.addItem(self.verticalSpacer_28, 1, 0, 1, 2)

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

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_27, 14, 0, 1, 2)

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


        self.gridLayout_26.addWidget(self.groupBoxScanner, 4, 0, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_26.addItem(self.verticalSpacer_26, 0, 0, 1, 1)

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

        self.gridLayout_26.addWidget(self.labelSettings, 2, 0, 1, 1, Qt.AlignRight)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_26.addItem(self.verticalSpacer_30, 3, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frameSettingsContent)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(42, 42))
        self.pushButton_7.setMaximumSize(QSize(42, 42))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_7.setIcon(icon15)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.gridLayout_26.addWidget(self.pushButton_7, 1, 0, 1, 1)


        self.gridLayout_27.addWidget(self.frameSettingsContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetSettings)

        self.gridLayout_2.addWidget(self.stackedWidgetContainer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameContainer, 1, 0, 1, 1)

 

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        self.stackedWidgetContainer.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelCoverArt.setText("")
        self.labelArtistSong.setText("")
        self.labelTitleSong.setText("")
        self.labelAlbumSong.setText("")
        self.pushButtonVolume.setText("")
        self.pushButtonAddFavorite.setText("")
        self.pushButtonNext.setText("")
        self.pushButtonPrevious.setText("")
        self.pushButtonPlay.setText("")
        self.labelBitrate.setText("")
        self.labelDuration.setText("")
        self.labelTime.setText("")
        self.labelCodec.setText("")
        self.labelPlaylist.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.pushButtonPlaylists.setText(QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.labelMusic.setText(QCoreApplication.translate("MainWindow", u"Musica", None))
        self.pushButtonAddPath.setText(QCoreApplication.translate("MainWindow", u"Agregar ruta", None))
        self.pushButtonAlbums.setText(QCoreApplication.translate("MainWindow", u"Albumes", None))
        self.pushButtonSongs.setText(QCoreApplication.translate("MainWindow", u"Canciones", None))
        self.pushButtonAddDirectory.setText(QCoreApplication.translate("MainWindow", u"Agregar carpeta", None))
        self.pushButtonArtists.setText(QCoreApplication.translate("MainWindow", u"Artistas", None))
        self.labelFileOptions.setText(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.pushButtonFavorites.setText(QCoreApplication.translate("MainWindow", u"Favoritos", None))
        self.pushButtonAddFile.setText(QCoreApplication.translate("MainWindow", u"Agregar archivo", None))
        self.pushButtonSaveActualPlaylist.setText(QCoreApplication.translate("MainWindow", u"Guarda playlist actual", None))
        self.pushButtonSearch.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButtonSettings.setText("")
        self.pushButtonSong.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelPlaylisr.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.pushButton.setText("")
        self.labelInterest.setText(QCoreApplication.translate("MainWindow", u"Favoritos", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelArtists.setText(QCoreApplication.translate("MainWindow", u"Artistas", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelAlbumArtist.setText("")
        self.labelAlbumCoverArt.setText("")
        self.labelAlbumTitle.setText("")
        self.labelAlbum.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelSongs.setText(QCoreApplication.translate("MainWindow", u"Canciones", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.groupBoxScanner.setTitle("")
        self.labelPlatform.setText(QCoreApplication.translate("MainWindow", u"Plataforma", None))
        self.labelNode.setText(QCoreApplication.translate("MainWindow", u"Nodo", None))
        self.labelProcessor.setText(QCoreApplication.translate("MainWindow", u"Procesador", None))
        self.labelOS.setText(QCoreApplication.translate("MainWindow", u"Sistema Operativo", None))
        self.labelVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.labelSystem.setText(QCoreApplication.translate("MainWindow", u"Sistema", None))
        self.pushButtonScanner.setText(QCoreApplication.translate("MainWindow", u"Escanear musica", None))
        self.labelUser.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.labelArchitecture.setText(QCoreApplication.translate("MainWindow", u"Arquitectura", None))
        self.labelSession.setText(QCoreApplication.translate("MainWindow", u"Sesion", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sistema", None))
        self.labelMachine.setText(QCoreApplication.translate("MainWindow", u"Maquina", None))
        self.labelSettings.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.pushButton_7.setText("")
    # retranslateUi

