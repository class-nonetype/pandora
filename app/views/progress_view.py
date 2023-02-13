# -*- coding: utf-8 -*-


from PyQt5 import (
    QtCore,
    QtWidgets,
)

from app.views.side_grip_view import SideGripView



class ProgressView(QtWidgets.QMainWindow):
    _gripSize = 1

    def __init__(self):
        super().__init__()

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
            pass

        elif event.key() == QtCore.Qt.Key_F8:
            pass

        else:
            super().keyPressEvent(event)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(800, 200)
        
        self.centralwidget = QtWidgets.QWidget(parent = self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frameContainer = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameContainer.setStyleSheet("QFrame {\n"
                                          "\n"
                                          "    background-color : #46355e;\n"
                                          "}")
        self.frameContainer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frameContainer.setLineWidth(0)
        self.frameContainer.setObjectName("frameContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameContainer)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.frameProgress = QtWidgets.QFrame(parent=self.frameContainer)
        self.frameProgress.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameProgress.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameProgress.setObjectName("frameProgress")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameProgress)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.progressBar = QtWidgets.QProgressBar(parent=self.frameProgress)
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                       "    border: 2px solid #D37242;\n"
                                       "    border-radius: 5px;\n"
                                       "    text-align: center;\n"
                                       "    font : 77 12pt \"Microsoft JhengHei UI\" bold;\n"
                                       "    color : #999999;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: #61364F;\n"
                                       "    margin: 0.5px;\n"
                                       "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 2, 0, 1, 1)
        self.labelProgress = QtWidgets.QLabel(parent=self.frameProgress)
        self.labelProgress.setStyleSheet("QLabel {\n"
                                         "\n"
                                         "    font : 25 15pt \"Microsoft YaHei UI Light\";\n"
                                         "    color : #FFFFFF;\n"
                                         "    \n"
                                         "    text-align: left;\n"
                                         "\n"
                                         "}")
        self.labelProgress.setText("")
        self.labelProgress.setObjectName("labelProgress")
        self.gridLayout_3.addWidget(self.labelProgress, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frameProgress, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.frameContainer, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
