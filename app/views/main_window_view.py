# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



class SideGrip(QtWidgets.QWidget):

    def __init__(self, parent, edge):
        QtWidgets.QWidget.__init__(self, parent)

        #self.setStyleSheet("border : 1px solid #000000;")

        self.WidgetSideGrip = QtWidgets.QWidget(self)
        self.WidgetSideGrip.setObjectName('WidgetSideGrip')
        self.WidgetSideGrip.setStyleSheet('''
            QWidget#WidgetSideGrip {
                background: #D37242;
                border-radius: 20px;
                border: 12px solid #D37242;                   
            }
        ''')

        self.BoxLayoutSideGrip = QtWidgets.QVBoxLayout(self)
        self.BoxLayoutSideGrip.setContentsMargins(0, 0, 0, 0)
        self.BoxLayoutSideGrip.addWidget(self.WidgetSideGrip)

        if edge == QtCore.Qt.LeftEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunction = self.resizeLeft

        elif edge == QtCore.Qt.TopEdge:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunction = self.resizeTop

        elif edge == QtCore.Qt.RightEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunction = self.resizeRight

        else:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunction = self.resizeBottom

        self.mousePos = None



    def resizeLeft(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunction(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None



class MainWindowView(QtWidgets.QMainWindow):
    _gripSize = 1

    def __init__(self, Controller):
        super().__init__()

        self.Controller = Controller

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.sideGrips = [
            SideGrip(self, QtCore.Qt.LeftEdge), 
            SideGrip(self, QtCore.Qt.TopEdge), 
            SideGrip(self, QtCore.Qt.RightEdge), 
            SideGrip(self, QtCore.Qt.BottomEdge), 
        ]
        self.cornerGrips = [QtWidgets.QSizeGrip(self) for i in range(4)]

    @property
    def gripSize(self):
        return self._gripSize

    def setGripSize(self, size):
        if size == self._gripSize:
            return
        self._gripSize = max(2, size)
        self.updateGrips()

    def updateGrips(self):
        self.setContentsMargins(*[self.gripSize] * 4)

        outRect = self.rect()
        inRect = outRect.adjusted(self.gripSize, self.gripSize,
            -self.gripSize, -self.gripSize)

        # top left
        self.cornerGrips[0].setGeometry(
            QtCore.QRect(outRect.topLeft(), inRect.topLeft()))

        # top right
        self.cornerGrips[1].setGeometry(
            QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())

        # bottom right
        self.cornerGrips[2].setGeometry(
            QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))

        # bottom left
        self.cornerGrips[3].setGeometry(
            QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

        # left edge
        self.sideGrips[0].setGeometry(
            0, inRect.top(), self.gripSize, inRect.height())

        # top edge
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self.gripSize)

        # right edge
        self.sideGrips[2].setGeometry(
            inRect.left() + inRect.width(), 
            inRect.top(), self.gripSize, inRect.height())

        # bottom edge
        self.sideGrips[3].setGeometry(
            self.gripSize, inRect.top() + inRect.height(), 
            inRect.width(), self.gripSize)

    def closeEvent(self, event):
        self.destroy()

    def resizeEvent(self, event):
        QtWidgets.QMainWindow.resizeEvent(self, event)
        self.updateGrips()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        self.m_drag = False

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
        self.resize(519, 815)
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
        self.gridLayout_4.setObjectName(u"gridLayout_4")
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

        self.gridLayout_11.addItem(self.horizontalSpacer_7, 1, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

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

        self.gridLayout_11.addWidget(self.labelCoverArt, 1, 2, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_14, 0, 2, 1, 1)


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

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

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

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frameLibraryContent = QFrame(self.widgetLibrary)
        self.frameLibraryContent.setObjectName(u"frameLibraryContent")
        self.frameLibraryContent.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color : #111111;\n"
"}")
        self.frameLibraryContent.setFrameShape(QFrame.StyledPanel)
        self.frameLibraryContent.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frameLibraryContent)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.labelFileOptions = QLabel(self.frameLibraryContent)
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

        self.gridLayout_13.addWidget(self.labelFileOptions, 1, 0, 1, 1)

        self.listViewPlaylist = QListView(self.frameLibraryContent)
        self.listViewPlaylist.setObjectName(u"listViewPlaylist")
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

        self.gridLayout_13.addWidget(self.listViewPlaylist, 4, 0, 1, 2)

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

        self.gridLayout_13.addWidget(self.labelPlaylist, 3, 0, 1, 1)

        self.frameOptions = QFrame(self.frameLibraryContent)
        self.frameOptions.setObjectName(u"frameOptions")
        self.frameOptions.setFrameShape(QFrame.StyledPanel)
        self.frameOptions.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frameOptions)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
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
        icon5 = QIcon()
        icon5.addFile(u"app/resources/img/icons/24x24/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddDirectory.setIcon(icon5)
        self.pushButtonAddDirectory.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddDirectory, 2, 0, 1, 1)

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
        icon6 = QIcon()
        icon6.addFile(u"app/resources/img/icons/24x24/cil-music-note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddFile.setIcon(icon6)
        self.pushButtonAddFile.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddFile, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_9, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_6, 6, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_7, 9, 0, 1, 1)

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

        self.gridLayout_15.addWidget(self.pushButtonFavorites, 8, 0, 1, 1)

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
        icon7 = QIcon()
        icon7.addFile(u"app/resources/img/icons/24x24/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddPath.setIcon(icon7)
        self.pushButtonAddPath.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonAddPath, 3, 0, 1, 1)

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
        icon8 = QIcon()
        icon8.addFile(u"app/resources/img/icons/24x24/cil-list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPlaylists.setIcon(icon8)
        self.pushButtonPlaylists.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.pushButtonPlaylists, 5, 0, 1, 1)

        self.labelInterests = QLabel(self.frameOptions)
        self.labelInterests.setObjectName(u"labelInterests")
        self.labelInterests.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_15.addWidget(self.labelInterests, 7, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout_13.addWidget(self.frameOptions, 2, 0, 1, 2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_13.addItem(self.verticalSpacer_8, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.frameLibraryContent)
        self.pushButton.setObjectName(u"pushButton")
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
        icon9 = QIcon()
        icon9.addFile(u"app/resources/img/icons/24x24/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.pushButton, 3, 1, 1, 1)


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
        self.labelPlaylisr = QLabel(self.framePlaylistContent)
        self.labelPlaylisr.setObjectName(u"labelPlaylisr")
        self.labelPlaylisr.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_17.addWidget(self.labelPlaylisr, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_10, 0, 0, 1, 1)

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
        self.listViewPlaylists.setResizeMode(QListView.Fixed)
        self.listViewPlaylists.setLayoutMode(QListView.SinglePass)
        self.listViewPlaylists.setItemAlignment(Qt.AlignLeading)

        self.gridLayout_17.addWidget(self.listViewPlaylists, 3, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_11, 2, 0, 1, 1)


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
        self.labelInterest = QLabel(self.frameInterestContent)
        self.labelInterest.setObjectName(u"labelInterest")
        self.labelInterest.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_19.addWidget(self.labelInterest, 1, 0, 1, 1)

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
        self.listViewInterest.setResizeMode(QListView.Fixed)
        self.listViewInterest.setLayoutMode(QListView.SinglePass)
        self.listViewInterest.setItemAlignment(Qt.AlignLeading)

        self.gridLayout_19.addWidget(self.listViewInterest, 3, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_12, 0, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_13, 2, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frameInterestContent, 0, 0, 1, 1)

        self.stackedWidgetContainer.addWidget(self.widgetInterest)

        self.gridLayout_2.addWidget(self.stackedWidgetContainer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameContainer, 1, 0, 1, 1)

        self.frameWindowTitleBar = QFrame(self.centralwidget)
        self.frameWindowTitleBar.setObjectName(u"frameWindowTitleBar")
        self.frameWindowTitleBar.setMaximumSize(QSize(16777215, 46))
        self.frameWindowTitleBar.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color : #000000;\n"
"\n"
"}")
        self.frameWindowTitleBar.setFrameShape(QFrame.NoFrame)
        self.frameWindowTitleBar.setFrameShadow(QFrame.Plain)
        self.frameWindowTitleBar.setLineWidth(0)
        self.gridLayout_3 = QGridLayout(self.frameWindowTitleBar)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.labelWindowTitle = QLabel(self.frameWindowTitleBar)
        self.labelWindowTitle.setObjectName(u"labelWindowTitle")
        self.labelWindowTitle.setStyleSheet(u"QLabel {\n"
"	font : 77 15pt \"Microsoft JhengHei UI\";\n"
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

        self.gridLayout_3.addWidget(self.labelWindowTitle, 0, 0, 1, 1)

        self.framePushButtonWindowPanel = QFrame(self.frameWindowTitleBar)
        self.framePushButtonWindowPanel.setObjectName(u"framePushButtonWindowPanel")
        self.framePushButtonWindowPanel.setFrameShape(QFrame.NoFrame)
        self.framePushButtonWindowPanel.setFrameShadow(QFrame.Plain)
        self.framePushButtonWindowPanel.setLineWidth(0)
        self.gridLayout_8 = QGridLayout(self.framePushButtonWindowPanel)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButtonRestore = QPushButton(self.framePushButtonWindowPanel)
        self.pushButtonRestore.setObjectName(u"pushButtonRestore")
        self.pushButtonRestore.setMinimumSize(QSize(42, 42))
        self.pushButtonRestore.setMaximumSize(QSize(42, 42))
        self.pushButtonRestore.setStyleSheet(u"QPushButton {\n"
"	background-color : #000000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color : #555555;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"app/resources/img/icons/24x24/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRestore.setIcon(icon10)
        self.pushButtonRestore.setIconSize(QSize(18, 18))

        self.gridLayout_8.addWidget(self.pushButtonRestore, 0, 2, 1, 1)

        self.pushButtonMinimize = QPushButton(self.framePushButtonWindowPanel)
        self.pushButtonMinimize.setObjectName(u"pushButtonMinimize")
        self.pushButtonMinimize.setMinimumSize(QSize(42, 42))
        self.pushButtonMinimize.setMaximumSize(QSize(42, 42))
        self.pushButtonMinimize.setStyleSheet(u"QPushButton {\n"
"	background-color : #000000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color : #555555;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"app/resources/img/icons/24x24/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMinimize.setIcon(icon11)
        self.pushButtonMinimize.setIconSize(QSize(18, 18))

        self.gridLayout_8.addWidget(self.pushButtonMinimize, 0, 0, 1, 1)

        self.pushButtonClose = QPushButton(self.framePushButtonWindowPanel)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        self.pushButtonClose.setMinimumSize(QSize(42, 42))
        self.pushButtonClose.setMaximumSize(QSize(42, 42))
        self.pushButtonClose.setStyleSheet(u"QPushButton {\n"
"	background-color : #A93226;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color : #87281E\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"app/resources/img/icons/24x24/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonClose.setIcon(icon12)
        self.pushButtonClose.setIconSize(QSize(18, 18))
        self.pushButtonClose.setFlat(False)

        self.gridLayout_8.addWidget(self.pushButtonClose, 0, 3, 1, 1)


        self.gridLayout_3.addWidget(self.framePushButtonWindowPanel, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frameWindowTitleBar, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        self.stackedWidgetContainer.setCurrentIndex(0)


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
        self.labelFileOptions.setText(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.labelPlaylist.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.pushButtonAddDirectory.setText(QCoreApplication.translate("MainWindow", u"Agregar carpeta", None))
        self.pushButtonAddFile.setText(QCoreApplication.translate("MainWindow", u"Agregar archivo", None))
        self.pushButtonFavorites.setText(QCoreApplication.translate("MainWindow", u"Favoritos", None))
        self.pushButtonAddPath.setText(QCoreApplication.translate("MainWindow", u"Agregar ruta", None))
        self.pushButtonPlaylists.setText(QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.labelInterests.setText(QCoreApplication.translate("MainWindow", u"Interes", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Guarda playlist actual", None))
        self.labelPlaylisr.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.labelInterest.setText(QCoreApplication.translate("MainWindow", u"Favoritos", None))
        self.labelWindowTitle.setText(QCoreApplication.translate("MainWindow", u"VZPlayer", None))
        self.pushButtonRestore.setText("")
        self.pushButtonMinimize.setText("")
        self.pushButtonClose.setText("")
    # retranslateUi

