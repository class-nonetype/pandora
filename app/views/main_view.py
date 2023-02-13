# -*- coding: utf-8 -*-


from PyQt5 import (
    QtCore,
    QtWidgets,
    QtGui
)

from app.views.side_grip_view import SideGripView


class MainView(QtWidgets.QMainWindow):
    _gripSize = 1

    def __init__(self, Controller):
        super().__init__()

        self.Controller = Controller

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.FramelessWindowHint)
        self.sideGrips = [
            SideGripView(self, QtCore.Qt.LeftEdge),
            SideGripView(self, QtCore.Qt.TopEdge),
            SideGripView(self, QtCore.Qt.RightEdge),
            SideGripView(self, QtCore.Qt.BottomEdge),
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
        if event.buttons() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and QtCore.Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        self.m_drag = False

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            QtWidgets.qApp.quit()

        elif event.key() == QtCore.Qt.Key_F1:
            pass

        elif event.key() == QtCore.Qt.Key_F2:
            pass

        elif event.key() == QtCore.Qt.Key_F3:
            pass

        elif event.key() == QtCore.Qt.Key_F4:
            pass

        elif event.key() == QtCore.Qt.Key_F7:
            return self.radioButtonDarkMode.setChecked(True)

        elif event.key() == QtCore.Qt.Key_F8:
            return self.radioButtonLightMode.setChecked(True)

        else:
            super().keyPressEvent(event)

    def setupUi(self):
        if self.objectName():
            self.setObjectName(u"MainWindow")

        self.setEnabled(True)
        self.resize(450, 800)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")



        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frameContainer = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameContainer.setStyleSheet("QFrame {\n"
"\n"
"    background-color : #121212;\n"
"\n"
"}")
        self.frameContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameContainer.setObjectName("frameContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameContainer)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameWindowTitleBar = QtWidgets.QFrame(parent=self.frameContainer)
        self.frameWindowTitleBar.setMinimumSize(QtCore.QSize(0, 50))
        self.frameWindowTitleBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameWindowTitleBar.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.frameWindowTitleBar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameWindowTitleBar.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frameWindowTitleBar.setLineWidth(0)
        self.frameWindowTitleBar.setObjectName("frameWindowTitleBar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameWindowTitleBar)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 2, 1, 1)
        self.frameWindowTitleBarPushButtons = QtWidgets.QFrame(parent=self.frameWindowTitleBar)
        self.frameWindowTitleBarPushButtons.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameWindowTitleBarPushButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frameWindowTitleBarPushButtons.setLineWidth(0)
        self.frameWindowTitleBarPushButtons.setObjectName("frameWindowTitleBarPushButtons")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frameWindowTitleBarPushButtons)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButtonMinimizeWindow = QtWidgets.QPushButton(parent=self.frameWindowTitleBarPushButtons)
        self.pushButtonMinimizeWindow.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonMinimizeWindow.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonMinimizeWindow.setStyleSheet("QPushButton {\n"
"    background-color : transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color : #202020;\n"
"}")
        self.pushButtonMinimizeWindow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-window-minimize.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonMinimizeWindow.setIcon(icon)
        self.pushButtonMinimizeWindow.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonMinimizeWindow.setObjectName("pushButtonMinimizeWindow")
        self.gridLayout_8.addWidget(self.pushButtonMinimizeWindow, 0, 0, 1, 1)
        self.pushButtonRestoreWindow = QtWidgets.QPushButton(parent=self.frameWindowTitleBarPushButtons)
        self.pushButtonRestoreWindow.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonRestoreWindow.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonRestoreWindow.setStyleSheet("QPushButton {\n"
"    background-color : transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color : #202020;\n"
"}")
        self.pushButtonRestoreWindow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-window-maximize.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonRestoreWindow.setIcon(icon1)
        self.pushButtonRestoreWindow.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonRestoreWindow.setObjectName("pushButtonRestoreWindow")
        self.gridLayout_8.addWidget(self.pushButtonRestoreWindow, 0, 2, 1, 1)
        self.pushButtonCloseWindow = QtWidgets.QPushButton(parent=self.frameWindowTitleBarPushButtons)
        self.pushButtonCloseWindow.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonCloseWindow.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonCloseWindow.setStyleSheet("QPushButton {\n"
"    background-color : #A93226;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color : #87281E\n"
"}")
        self.pushButtonCloseWindow.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-x.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCloseWindow.setIcon(icon2)
        self.pushButtonCloseWindow.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonCloseWindow.setFlat(False)
        self.pushButtonCloseWindow.setObjectName("pushButtonCloseWindow")
        self.gridLayout_8.addWidget(self.pushButtonCloseWindow, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.frameWindowTitleBarPushButtons, 3, 3, 1, 1)
        self.labelWindowTitleBar = QtWidgets.QLabel(parent=self.frameWindowTitleBar)
        self.labelWindowTitleBar.setStyleSheet("QLabel {\n"
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
        self.labelWindowTitleBar.setObjectName("labelWindowTitleBar")
        self.gridLayout_3.addWidget(self.labelWindowTitleBar, 3, 1, 1, 1)
        self.labelWindowIcon = QtWidgets.QLabel(parent=self.frameWindowTitleBar)
        self.labelWindowIcon.setMinimumSize(QtCore.QSize(42, 42))
        self.labelWindowIcon.setMaximumSize(QtCore.QSize(42, 42))
        self.labelWindowIcon.setStyleSheet("QLabel{\n"
"    background-color: #5F3E77;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: #46355e;\n"
"\n"
"}")
        self.labelWindowIcon.setText("")
        self.labelWindowIcon.setPixmap(QtGui.QPixmap("app/resources/img/window/icon.png"))
        self.labelWindowIcon.setScaledContents(True)
        self.labelWindowIcon.setObjectName("labelWindowIcon")
        self.gridLayout_3.addWidget(self.labelWindowIcon, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frameWindowTitleBar, 0, 0, 1, 1)
        self.frameControlView = QtWidgets.QFrame(parent=self.frameContainer)
        self.frameControlView.setStyleSheet("QFrame {\n"
"    background-color : transparent;\n"
"}")
        self.frameControlView.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameControlView.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameControlView.setObjectName("frameControlView")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameControlView)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.frameControlView)
        self.pushButtonBack.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonBack.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonBack.setStyleSheet("QPushButton{\n"
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
        self.pushButtonBack.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-arrow-circle-left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonBack.setIcon(icon3)
        self.pushButtonBack.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.gridLayout_4.addWidget(self.pushButtonBack, 0, 0, 1, 1)
        self.pushButtonSettings = QtWidgets.QPushButton(parent=self.frameControlView)
        self.pushButtonSettings.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonSettings.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonSettings.setStyleSheet("QPushButton{\n"
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
        self.pushButtonSettings.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSettings.setIcon(icon4)
        self.pushButtonSettings.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.gridLayout_4.addWidget(self.pushButtonSettings, 0, 2, 1, 1)
        self.pushButtonPlayer = QtWidgets.QPushButton(parent=self.frameControlView)
        self.pushButtonPlayer.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonPlayer.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonPlayer.setStyleSheet("QPushButton{\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-music-note.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPlayer.setIcon(icon5)
        self.pushButtonPlayer.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonPlayer.setObjectName("pushButtonPlayer")
        self.gridLayout_4.addWidget(self.pushButtonPlayer, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.pushButtonPlaylistPlayer = QtWidgets.QPushButton(parent=self.frameControlView)
        self.pushButtonPlaylistPlayer.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonPlaylistPlayer.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonPlaylistPlayer.setStyleSheet("QPushButton{\n"
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
        self.pushButtonPlaylistPlayer.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-list.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPlaylistPlayer.setIcon(icon6)
        self.pushButtonPlaylistPlayer.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonPlaylistPlayer.setFlat(True)
        self.pushButtonPlaylistPlayer.setObjectName("pushButtonPlaylistPlayer")
        self.gridLayout_4.addWidget(self.pushButtonPlaylistPlayer, 0, 5, 1, 1)
        self.gridLayout_2.addWidget(self.frameControlView, 1, 0, 1, 1)
        self.stackedWidgetContent = QtWidgets.QStackedWidget(parent=self.frameContainer)
        self.stackedWidgetContent.setLineWidth(0)
        self.stackedWidgetContent.setObjectName("stackedWidgetContent")
        self.playerWidget = QtWidgets.QWidget()
        self.playerWidget.setObjectName("playerWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.playerWidget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.framePlayerContainer = QtWidgets.QFrame(parent=self.playerWidget)
        self.framePlayerContainer.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.framePlayerContainer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.framePlayerContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.framePlayerContainer.setLineWidth(0)
        self.framePlayerContainer.setObjectName("framePlayerContainer")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.framePlayerContainer)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_5.setSpacing(9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.framePlayer = QtWidgets.QFrame(parent=self.framePlayerContainer)
        self.framePlayer.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.framePlayer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.framePlayer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.framePlayer.setLineWidth(0)
        self.framePlayer.setObjectName("framePlayer")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.framePlayer)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.framePlayerContent = QtWidgets.QFrame(parent=self.framePlayer)
        self.framePlayerContent.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.framePlayerContent.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.framePlayerContent.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.framePlayerContent.setLineWidth(0)
        self.framePlayerContent.setObjectName("framePlayerContent")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.framePlayerContent)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.labelAlbum = QtWidgets.QLabel(parent=self.framePlayerContent)
        self.labelAlbum.setStyleSheet("QLabel {\n"
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
        self.labelAlbum.setText("")
        self.labelAlbum.setObjectName("labelAlbum")
        self.gridLayout_10.addWidget(self.labelAlbum, 4, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelArtist = QtWidgets.QLabel(parent=self.framePlayerContent)
        self.labelArtist.setStyleSheet("QLabel {\n"
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
        self.labelArtist.setText("")
        self.labelArtist.setObjectName("labelArtist")
        self.gridLayout_10.addWidget(self.labelArtist, 6, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_10.addItem(spacerItem3, 7, 0, 1, 1)
        self.labelCoverArt = QtWidgets.QLabel(parent=self.framePlayerContent)
        self.labelCoverArt.setMinimumSize(QtCore.QSize(350, 350))
        self.labelCoverArt.setMaximumSize(QtCore.QSize(350, 350))
        self.labelCoverArt.setStyleSheet("QLabel {\n"
"\n"
"    border : 2px solid #5F3E77;\n"
"\n"
"}")
        self.labelCoverArt.setText("")
        self.labelCoverArt.setScaledContents(True)
        self.labelCoverArt.setObjectName("labelCoverArt")
        self.gridLayout_10.addWidget(self.labelCoverArt, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.framePlayerControl = QtWidgets.QFrame(parent=self.framePlayerContent)
        self.framePlayerControl.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.framePlayerControl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.framePlayerControl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.framePlayerControl.setObjectName("framePlayerControl")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.framePlayerControl)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalSliderTime = QtWidgets.QSlider(parent=self.framePlayerControl)
        self.horizontalSliderTime.setMinimumSize(QtCore.QSize(300, 0))
        self.horizontalSliderTime.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #333333;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width : 10px;\n"
"    height : 10px;\n"
"    border : 2px;\n"
"    border-radius : 4px;\n"
"    background-color : #FFFFFF;\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"    background: #222222;\n"
"    border-top-right-radius: 9px;\n"
"    border-bottom-right-radius: 9px;\n"
"    border-top-left-radius: 9px;\n"
"    border-bottom-left-radius: 9px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"    background: #5F3E77;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top-left-radius: 9px;\n"
"    border-bottom-left-radius: 9px;\n"
"}")
        self.horizontalSliderTime.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSliderTime.setObjectName("horizontalSliderTime")
        self.gridLayout_14.addWidget(self.horizontalSliderTime, 0, 2, 1, 1)
        self.frameVolume = QtWidgets.QFrame(parent=self.framePlayerControl)
        self.frameVolume.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.frameVolume.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameVolume.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameVolume.setObjectName("frameVolume")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frameVolume)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButtonVolume = QtWidgets.QPushButton(parent=self.frameVolume)
        self.pushButtonVolume.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonVolume.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonVolume.setStyleSheet("QPushButton {\n"
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
        self.pushButtonVolume.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-volume-high.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonVolume.setIcon(icon7)
        self.pushButtonVolume.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonVolume.setObjectName("pushButtonVolume")
        self.gridLayout_12.addWidget(self.pushButtonVolume, 0, 0, 1, 1)
        self.horizontalSliderVolume = QtWidgets.QSlider(parent=self.frameVolume)
        self.horizontalSliderVolume.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #202020;\n"
"    height:  6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width :  6px;\n"
"    height : 6px;\n"
"    border : 2px;\n"
"    border-radius : 2px;\n"
"    background-color : #FFFFFF;\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"    background: #202020;\n"
"    border-top-right-radius: 9px;\n"
"    border-bottom-right-radius: 9px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"    background: #4F6FA0;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top-left-radius: 9px;\n"
"    border-bottom-left-radius: 9px;\n"
"}")
        self.horizontalSliderVolume.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSliderVolume.setObjectName("horizontalSliderVolume")
        self.gridLayout_12.addWidget(self.horizontalSliderVolume, 0, 1, 1, 1)
        self.pushButtonAddFavorite = QtWidgets.QPushButton(parent=self.frameVolume)
        self.pushButtonAddFavorite.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonAddFavorite.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonAddFavorite.setStyleSheet("QPushButton {\n"
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
        self.pushButtonAddFavorite.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-heart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAddFavorite.setIcon(icon8)
        self.pushButtonAddFavorite.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonAddFavorite.setObjectName("pushButtonAddFavorite")
        self.gridLayout_12.addWidget(self.pushButtonAddFavorite, 0, 2, 1, 1)
        self.gridLayout_14.addWidget(self.frameVolume, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_14.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_14.addItem(spacerItem5, 1, 2, 1, 1)
        self.frameControl = QtWidgets.QFrame(parent=self.framePlayerControl)
        self.frameControl.setMinimumSize(QtCore.QSize(0, 50))
        self.frameControl.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameControl.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.frameControl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameControl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameControl.setObjectName("frameControl")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frameControl)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(9)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 0, 5, 1, 1)
        self.pushButtonNext = QtWidgets.QPushButton(parent=self.frameControl)
        self.pushButtonNext.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonNext.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonNext.setStyleSheet("QPushButton {\n"
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
        self.pushButtonNext.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-media-step-forward.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonNext.setIcon(icon9)
        self.pushButtonNext.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonNext.setFlat(True)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.gridLayout_6.addWidget(self.pushButtonNext, 0, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem7, 0, 1, 1, 1)
        self.pushButtonPrevious = QtWidgets.QPushButton(parent=self.frameControl)
        self.pushButtonPrevious.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonPrevious.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonPrevious.setStyleSheet("QPushButton {\n"
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
        self.pushButtonPrevious.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-media-step-backward.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPrevious.setIcon(icon10)
        self.pushButtonPrevious.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonPrevious.setFlat(True)
        self.pushButtonPrevious.setObjectName("pushButtonPrevious")
        self.gridLayout_6.addWidget(self.pushButtonPrevious, 0, 2, 1, 1)
        self.pushButtonPlay = QtWidgets.QPushButton(parent=self.frameControl)
        self.pushButtonPlay.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonPlay.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonPlay.setStyleSheet("QPushButton {\n"
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
        self.pushButtonPlay.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-media-play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPlay.setIcon(icon11)
        self.pushButtonPlay.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonPlay.setFlat(True)
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.gridLayout_6.addWidget(self.pushButtonPlay, 0, 3, 1, 1)
        self.gridLayout_14.addWidget(self.frameControl, 2, 2, 1, 1)
        self.labelBitrate = QtWidgets.QLabel(parent=self.framePlayerControl)
        self.labelBitrate.setStyleSheet("QLabel {\n"
"    font : 22 11pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-left: 5px;\n"
"}")
        self.labelBitrate.setText("")
        self.labelBitrate.setObjectName("labelBitrate")
        self.gridLayout_14.addWidget(self.labelBitrate, 5, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_14.addItem(spacerItem8, 3, 2, 1, 1)
        self.labelDurationTime = QtWidgets.QLabel(parent=self.framePlayerControl)
        self.labelDurationTime.setStyleSheet("QLabel {\n"
"    font : 80 8pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-left: 5px;\n"
"}")
        self.labelDurationTime.setText("")
        self.labelDurationTime.setObjectName("labelDurationTime")
        self.gridLayout_14.addWidget(self.labelDurationTime, 0, 3, 1, 1)
        self.labelCurrentTime = QtWidgets.QLabel(parent=self.framePlayerControl)
        self.labelCurrentTime.setStyleSheet("QLabel {\n"
"    font : 80 8pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-left: 5px;\n"
"}")
        self.labelCurrentTime.setText("")
        self.labelCurrentTime.setObjectName("labelCurrentTime")
        self.gridLayout_14.addWidget(self.labelCurrentTime, 0, 1, 1, 1)
        self.labelCodec = QtWidgets.QLabel(parent=self.framePlayerControl)
        self.labelCodec.setStyleSheet("QLabel {\n"
"    font : 22 9pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-left: 5px;\n"
"}")
        self.labelCodec.setText("")
        self.labelCodec.setObjectName("labelCodec")
        self.gridLayout_14.addWidget(self.labelCodec, 6, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_14.addItem(spacerItem9, 0, 0, 1, 1)
        self.labelCurrentTime.raise_()
        self.frameControl.raise_()
        self.frameVolume.raise_()
        self.labelCodec.raise_()
        self.labelBitrate.raise_()
        self.horizontalSliderTime.raise_()
        self.labelDurationTime.raise_()
        self.gridLayout_10.addWidget(self.framePlayerControl, 8, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_10.addItem(spacerItem10, 0, 0, 1, 1)
        self.labelTitle = QtWidgets.QLabel(parent=self.framePlayerContent)
        self.labelTitle.setStyleSheet("QLabel {\n"
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
        self.labelTitle.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.labelTitle.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.labelTitle.setLineWidth(0)
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout_10.addWidget(self.labelTitle, 3, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_10.addItem(spacerItem11, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.framePlayerContent, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.framePlayer, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.framePlayerContainer, 0, 0, 1, 1)
        self.stackedWidgetContent.addWidget(self.playerWidget)
        self.libraryWidget = QtWidgets.QWidget()
        self.libraryWidget.setObjectName("libraryWidget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.libraryWidget)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frameLibraryContainer = QtWidgets.QFrame(parent=self.libraryWidget)
        self.frameLibraryContainer.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.frameLibraryContainer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameLibraryContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frameLibraryContainer.setLineWidth(0)
        self.frameLibraryContainer.setObjectName("frameLibraryContainer")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frameLibraryContainer)
        self.gridLayout_13.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_13.setSpacing(9)
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_13.addItem(spacerItem12, 0, 0, 1, 5)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_13.addItem(spacerItem13, 4, 1, 1, 3)
        self.frameLibrary = QtWidgets.QFrame(parent=self.frameLibraryContainer)
        self.frameLibrary.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameLibrary.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frameLibrary.setLineWidth(0)
        self.frameLibrary.setObjectName("frameLibrary")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frameLibrary)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.pushButtonAddPath = QtWidgets.QPushButton(parent=self.frameLibrary)
        self.pushButtonAddPath.setStyleSheet("QPushButton{\n"
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
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAddPath.setIcon(icon12)
        self.pushButtonAddPath.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonAddPath.setObjectName("pushButtonAddPath")
        self.gridLayout_15.addWidget(self.pushButtonAddPath, 7, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_15.addItem(spacerItem14, 2, 0, 1, 1)
        self.labelLibraryFileTitle = QtWidgets.QLabel(parent=self.frameLibrary)
        self.labelLibraryFileTitle.setStyleSheet("QLabel {\n"
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
        self.labelLibraryFileTitle.setObjectName("labelLibraryFileTitle")
        self.gridLayout_15.addWidget(self.labelLibraryFileTitle, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem15 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_15.addItem(spacerItem15, 6, 0, 1, 1)
        self.pushButtonFavorites = QtWidgets.QPushButton(parent=self.frameLibrary)
        self.pushButtonFavorites.setStyleSheet("QPushButton{\n"
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
        self.pushButtonFavorites.setIcon(icon8)
        self.pushButtonFavorites.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonFavorites.setObjectName("pushButtonFavorites")
        self.gridLayout_15.addWidget(self.pushButtonFavorites, 13, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_15.addItem(spacerItem16, 12, 0, 1, 1)
        self.labelLibraryMusicTitle = QtWidgets.QLabel(parent=self.frameLibrary)
        self.labelLibraryMusicTitle.setStyleSheet("QLabel {\n"
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
        self.labelLibraryMusicTitle.setObjectName("labelLibraryMusicTitle")
        self.gridLayout_15.addWidget(self.labelLibraryMusicTitle, 9, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButtonPlaylists = QtWidgets.QPushButton(parent=self.frameLibrary)
        self.pushButtonPlaylists.setStyleSheet("QPushButton{\n"
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
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-library.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPlaylists.setIcon(icon13)
        self.pushButtonPlaylists.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonPlaylists.setFlat(True)
        self.pushButtonPlaylists.setObjectName("pushButtonPlaylists")
        self.gridLayout_15.addWidget(self.pushButtonPlaylists, 11, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_15.addItem(spacerItem17, 8, 0, 1, 1)
        self.pushButtonAddDirectory = QtWidgets.QPushButton(parent=self.frameLibrary)
        self.pushButtonAddDirectory.setStyleSheet("QPushButton{\n"
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
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-folder-open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAddDirectory.setIcon(icon14)
        self.pushButtonAddDirectory.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonAddDirectory.setObjectName("pushButtonAddDirectory")
        self.gridLayout_15.addWidget(self.pushButtonAddDirectory, 5, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_15.addItem(spacerItem18, 4, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_15.addItem(spacerItem19, 10, 0, 1, 1)
        self.pushButtonAddFile = QtWidgets.QPushButton(parent=self.frameLibrary)
        self.pushButtonAddFile.setStyleSheet("QPushButton{\n"
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
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAddFile.setIcon(icon15)
        self.pushButtonAddFile.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonAddFile.setObjectName("pushButtonAddFile")
        self.gridLayout_15.addWidget(self.pushButtonAddFile, 3, 0, 1, 1)
        self.gridLayout_13.addWidget(self.frameLibrary, 3, 0, 1, 5)
        self.labelLibraryWidgetTitle = QtWidgets.QLabel(parent=self.frameLibraryContainer)
        self.labelLibraryWidgetTitle.setStyleSheet("QLabel {\n"
"    font : 77 18pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    color : #4F6FA0;\n"
"}\n"
"")
        self.labelLibraryWidgetTitle.setObjectName("labelLibraryWidgetTitle")
        self.gridLayout_13.addWidget(self.labelLibraryWidgetTitle, 1, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_13.addItem(spacerItem20, 2, 0, 1, 5)
        self.gridLayout_11.addWidget(self.frameLibraryContainer, 0, 0, 1, 1)
        self.stackedWidgetContent.addWidget(self.libraryWidget)
        self.settingsWidget = QtWidgets.QWidget()
        self.settingsWidget.setObjectName("settingsWidget")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.settingsWidget)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.frameSettingsContainer = QtWidgets.QFrame(parent=self.settingsWidget)
        self.frameSettingsContainer.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.frameSettingsContainer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameSettingsContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frameSettingsContainer.setLineWidth(0)
        self.frameSettingsContainer.setObjectName("frameSettingsContainer")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.frameSettingsContainer)
        self.gridLayout_26.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_26.setSpacing(9)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.labelSettingsWidgetTitle = QtWidgets.QLabel(parent=self.frameSettingsContainer)
        self.labelSettingsWidgetTitle.setStyleSheet("QLabel {\n"
"    font : 77 18pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    color : #4F6FA0;\n"
"}\n"
"")
        self.labelSettingsWidgetTitle.setObjectName("labelSettingsWidgetTitle")
        self.gridLayout_26.addWidget(self.labelSettingsWidgetTitle, 2, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_26.addItem(spacerItem21, 3, 0, 1, 2)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_26.addItem(spacerItem22, 6, 0, 1, 2)
        spacerItem23 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_26.addItem(spacerItem23, 0, 0, 1, 2)
        self.frameMode = QtWidgets.QFrame(parent=self.frameSettingsContainer)
        self.frameMode.setStyleSheet("QFrame {\n"
"    background-color: #5F3E77;\n"
"    border-radius : 40px;\n"
"}\n"
"\n"
"")
        self.frameMode.setObjectName("frameMode")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frameMode)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.labelSettingsModeTitle = QtWidgets.QLabel(parent=self.frameMode)
        self.labelSettingsModeTitle.setStyleSheet("QLabel {\n"
"    font : 77 18pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    color : #4F6FA0;\n"
"}\n"
"")
        self.labelSettingsModeTitle.setObjectName("labelSettingsModeTitle")
        self.gridLayout_20.addWidget(self.labelSettingsModeTitle, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.radioButtonLightMode = QtWidgets.QRadioButton(parent=self.frameMode)
        self.radioButtonLightMode.setStyleSheet("QRadioButton {\n"
"    font : 75 11pt \"Microsoft JhengHei UI\"  bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    padding-left : 20px\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    color : #3A609B;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton::checked {\n"
"    color : #3A609B;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    color : #3A609B;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    color : #3A609B;\n"
"}")
        self.radioButtonLightMode.setObjectName("radioButtonLightMode")
        self.gridLayout_20.addWidget(self.radioButtonLightMode, 5, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_20.addItem(spacerItem24, 2, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_20.addItem(spacerItem25, 0, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_20.addItem(spacerItem26, 6, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_20.addItem(spacerItem27, 4, 0, 1, 1)
        self.radioButtonDarkMode = QtWidgets.QRadioButton(parent=self.frameMode)
        self.radioButtonDarkMode.setStyleSheet("QRadioButton {\n"
"    font : 75 11pt \"Microsoft JhengHei UI\"  bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    padding-left : 20px\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    color : #3A609B;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton::checked {\n"
"    color : #3A609B;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    color : #3A609B;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    color : #3A609B;\n"
"}")
        self.radioButtonDarkMode.setObjectName("radioButtonDarkMode")
        self.gridLayout_20.addWidget(self.radioButtonDarkMode, 3, 0, 1, 1)
        self.gridLayout_26.addWidget(self.frameMode, 4, 0, 1, 2)
        self.gridLayout_16.addWidget(self.frameSettingsContainer, 0, 0, 1, 1)
        self.stackedWidgetContent.addWidget(self.settingsWidget)
        self.playlistsWidget = QtWidgets.QWidget()
        self.playlistsWidget.setObjectName("playlistsWidget")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.playlistsWidget)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.framePlaylistContainer = QtWidgets.QFrame(parent=self.playlistsWidget)
        self.framePlaylistContainer.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.framePlaylistContainer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.framePlaylistContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.framePlaylistContainer.setLineWidth(0)
        self.framePlaylistContainer.setObjectName("framePlaylistContainer")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.framePlaylistContainer)
        self.gridLayout_17.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_17.setSpacing(9)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.lineEditPlaylistSearcher = QtWidgets.QLineEdit(parent=self.framePlaylistContainer)
        self.lineEditPlaylistSearcher.setMinimumSize(QtCore.QSize(280, 42))
        self.lineEditPlaylistSearcher.setMaximumSize(QtCore.QSize(16777215, 42))
        self.lineEditPlaylistSearcher.setStyleSheet("QLineEdit{\n"
"    background-color: #222222;\n"
"\n"
"    border-radius : 20px;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color: #FFFFFF;\n"
"    padding : 10px;\n"
"    text-align : left;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: #222222;\n"
"}")
        self.lineEditPlaylistSearcher.setObjectName("lineEditPlaylistSearcher")
        self.gridLayout_17.addWidget(self.lineEditPlaylistSearcher, 6, 0, 1, 2)
        self.pushButtonSaveActualPlaylist = QtWidgets.QPushButton(parent=self.framePlaylistContainer)
        self.pushButtonSaveActualPlaylist.setMinimumSize(QtCore.QSize(250, 42))
        self.pushButtonSaveActualPlaylist.setMaximumSize(QtCore.QSize(250, 42))
        self.pushButtonSaveActualPlaylist.setStyleSheet("QPushButton{\n"
"    background-color: transparent;\n"
"    border-radius : 20px;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color: #FFFFFF;\n"
"    padding : 10px;\n"
"    text-align : left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #222222;\n"
"    color: #FFFFFF;\n"
"\n"
"}")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-library-add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSaveActualPlaylist.setIcon(icon16)
        self.pushButtonSaveActualPlaylist.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonSaveActualPlaylist.setObjectName("pushButtonSaveActualPlaylist")
        self.gridLayout_17.addWidget(self.pushButtonSaveActualPlaylist, 7, 0, 1, 1)
        self.listViewPlaylists = QtWidgets.QListView(parent=self.framePlaylistContainer)
        self.listViewPlaylists.setMinimumSize(QtCore.QSize(150, 0))
        self.listViewPlaylists.setMaximumSize(QtCore.QSize(300, 16777215))
        self.listViewPlaylists.setStyleSheet("QListView {\n"
"    background-color : #181818;\n"
"    font : 77 13pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 24px;\n"
"    text-align : left;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QListView::hover {\n"
"    color : #4F6FA0;\n"
"}")
        self.listViewPlaylists.setObjectName("listViewPlaylists")
        self.gridLayout_17.addWidget(self.listViewPlaylists, 8, 2, 1, 1)
        self.pushButtonSearchPlaylist = QtWidgets.QPushButton(parent=self.framePlaylistContainer)
        self.pushButtonSearchPlaylist.setMinimumSize(QtCore.QSize(150, 42))
        self.pushButtonSearchPlaylist.setMaximumSize(QtCore.QSize(150, 42))
        self.pushButtonSearchPlaylist.setStyleSheet("QPushButton{\n"
"    background-color: #5F3E77;\n"
"    border-radius : 20px;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color: #FFFFFF;\n"
"    padding : 10px;\n"
"    text-align : left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #46355e;\n"
"    color: #FFFFFF;\n"
"\n"
"}")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-arrow-right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSearchPlaylist.setIcon(icon17)
        self.pushButtonSearchPlaylist.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonSearchPlaylist.setObjectName("pushButtonSearchPlaylist")
        self.gridLayout_17.addWidget(self.pushButtonSearchPlaylist, 6, 2, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_17.addItem(spacerItem28, 5, 0, 1, 3)
        self.listViewPlayer = QtWidgets.QListView(parent=self.framePlaylistContainer)
        self.listViewPlayer.setMinimumSize(QtCore.QSize(300, 0))
        self.listViewPlayer.setStyleSheet("QListView {\n"
"    background-color : #181818;\n"
"    font : 77 13pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 24px;\n"
"    text-align : left;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QListView::hover {\n"
"    color : #4F6FA0;\n"
"}")
        self.listViewPlayer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.listViewPlayer.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.listViewPlayer.setDragEnabled(True)
        self.listViewPlayer.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.listViewPlayer.setDefaultDropAction(QtCore.Qt.DropAction.MoveAction)
        self.listViewPlayer.setAlternatingRowColors(False)
        self.listViewPlayer.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.listViewPlayer.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.listViewPlayer.setItemAlignment(QtCore.Qt.AlignmentFlag.AlignLeading)
        self.listViewPlayer.setObjectName("listViewPlayer")
        self.gridLayout_17.addWidget(self.listViewPlayer, 8, 0, 1, 1)
        self.labelPlaylistWidgetTitle = QtWidgets.QLabel(parent=self.framePlaylistContainer)
        self.labelPlaylistWidgetTitle.setStyleSheet("QLabel {\n"
"    font : 77 18pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    color : #4F6FA0;\n"
"}\n"
"")
        self.labelPlaylistWidgetTitle.setObjectName("labelPlaylistWidgetTitle")
        self.gridLayout_17.addWidget(self.labelPlaylistWidgetTitle, 4, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        spacerItem29 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_17.addItem(spacerItem29, 1, 0, 1, 3)
        self.gridLayout_18.addWidget(self.framePlaylistContainer, 0, 0, 1, 1)
        self.stackedWidgetContent.addWidget(self.playlistsWidget)
        self.favoritesWidget = QtWidgets.QWidget()
        self.favoritesWidget.setObjectName("favoritesWidget")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.favoritesWidget)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.frameInterestContainer = QtWidgets.QFrame(parent=self.favoritesWidget)
        self.frameInterestContainer.setStyleSheet("QFrame {\n"
"\n"
"    background-color : transparent;\n"
"\n"
"}")
        self.frameInterestContainer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameInterestContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frameInterestContainer.setLineWidth(0)
        self.frameInterestContainer.setObjectName("frameInterestContainer")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frameInterestContainer)
        self.gridLayout_19.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_19.setSpacing(9)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.listViewInterest = QtWidgets.QListView(parent=self.frameInterestContainer)
        self.listViewInterest.setStyleSheet("QListView {\n"
"    font : 77 13pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QListView::hover {\n"
"    color : #4F6FA0;\n"
"}")
        self.listViewInterest.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.listViewInterest.setDragEnabled(True)
        self.listViewInterest.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.listViewInterest.setDefaultDropAction(QtCore.Qt.DropAction.MoveAction)
        self.listViewInterest.setAlternatingRowColors(False)
        self.listViewInterest.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.listViewInterest.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.listViewInterest.setItemAlignment(QtCore.Qt.AlignmentFlag.AlignLeading)
        self.listViewInterest.setObjectName("listViewInterest")
        self.gridLayout_19.addWidget(self.listViewInterest, 5, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_19.addItem(spacerItem30, 1, 0, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_19.addItem(spacerItem31, 4, 0, 1, 1)
        self.labelFavoriteWidgetTitle = QtWidgets.QLabel(parent=self.frameInterestContainer)
        self.labelFavoriteWidgetTitle.setStyleSheet("QLabel {\n"
"    font : 77 18pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    color : #4F6FA0;\n"
"}\n"
"")
        self.labelFavoriteWidgetTitle.setObjectName("labelFavoriteWidgetTitle")
        self.gridLayout_19.addWidget(self.labelFavoriteWidgetTitle, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_21.addWidget(self.frameInterestContainer, 0, 0, 1, 1)
        self.stackedWidgetContent.addWidget(self.favoritesWidget)
        self.gridLayout_2.addWidget(self.stackedWidgetContent, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frameContainer, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.stackedWidgetContent.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.labelWindowTitleBar.setText(_translate("MainWindow", "Pandora"))
        self.pushButtonAddPath.setText(
            _translate("MainWindow", "Agregar ruta"))
        self.labelLibraryFileTitle.setText(_translate("MainWindow", "Archivo"))
        self.pushButtonFavorites.setText(_translate("MainWindow", "Favoritos"))
        self.labelLibraryMusicTitle.setText(_translate("MainWindow", "Musica"))
        self.pushButtonPlaylists.setText(_translate("MainWindow", "Playlists"))
        self.pushButtonAddDirectory.setText(
            _translate("MainWindow", "Agregar carpeta"))
        self.pushButtonAddFile.setText(
            _translate("MainWindow", "Agregar archivo"))
        self.labelLibraryWidgetTitle.setText(
            _translate("MainWindow", "Libreria"))
        self.labelSettingsWidgetTitle.setText(
            _translate("MainWindow", "Ajustes"))
        self.labelSettingsModeTitle.setText(_translate("MainWindow", "Tema"))
        self.radioButtonLightMode.setText(
            _translate("MainWindow", "Modo Claro"))
        self.radioButtonDarkMode.setText(
            _translate("MainWindow", "Modo Oscuro"))

        self.pushButtonSaveActualPlaylist.setText(
            _translate("MainWindow", "Guardar lista actual"))
        self.pushButtonSearchPlaylist.setText(
            _translate("MainWindow", "Buscar"))
        self.labelPlaylistWidgetTitle.setText(
            _translate("MainWindow", "Playlist"))
        self.labelFavoriteWidgetTitle.setText(
            _translate("MainWindow", "Favoritos"))
