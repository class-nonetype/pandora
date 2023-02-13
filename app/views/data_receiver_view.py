# -*- coding: utf-8 -*-


from PyQt5 import (
    QtCore,
    QtWidgets,
    QtGui
)

from app.views.side_grip_view import SideGripView


class DataReceiverView(QtWidgets.QMainWindow):
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
        self.resize(688, 236)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frameContainer = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameContainer.setStyleSheet("QFrame {\n"
                                          "\n"
                                          "    background-color : #252525;\n"
                                          "}")
        self.frameContainer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frameContainer.setLineWidth(0)
        self.frameContainer.setObjectName("frameContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameContainer)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameDataReceiver = QtWidgets.QFrame(parent=self.frameContainer)
        self.frameDataReceiver.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel)
        self.frameDataReceiver.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameDataReceiver.setObjectName("frameDataReceiver")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameDataReceiver)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 4, 1)
        self.lineEditData = QtWidgets.QLineEdit(parent=self.frameDataReceiver)
        self.lineEditData.setMinimumSize(QtCore.QSize(480, 42))
        self.lineEditData.setMaximumSize(QtCore.QSize(480, 42))
        self.lineEditData.setStyleSheet("QLineEdit{\n"
                                        "    background-color: #121212;\n"
                                        "\n"
                                        "    border-radius : 20px;\n"
                                        "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
                                        "    color: #FFFFFF;\n"
                                        "    padding : 10px;\n"
                                        "    text-align : left;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit:hover{\n"
                                        "    background-color: #303030;\n"
                                        "}")
        self.lineEditData.setObjectName("lineEditData")
        self.gridLayout_3.addWidget(
            self.lineEditData, 2, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelTitle = QtWidgets.QLabel(parent=self.frameDataReceiver)
        self.labelTitle.setStyleSheet("QLabel {\n"
                                      "\n"
                                      "    font : 25 15pt \"Microsoft YaHei UI Light\";\n"
                                      "    color : #FFFFFF;\n"
                                      "    \n"
                                      "    text-align: left;\n"
                                      "\n"
                                      "}")
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout_3.addWidget(self.labelTitle, 1, 1, 1, 2)
        self.pushButtonConfirm = QtWidgets.QPushButton(
            parent=self.frameDataReceiver)
        self.pushButtonConfirm.setMinimumSize(QtCore.QSize(170, 36))
        self.pushButtonConfirm.setMaximumSize(QtCore.QSize(170, 36))
        self.pushButtonConfirm.setStyleSheet("QPushButton{\n"
                                             "    background-color: #5F3E77;\n"
                                             "\n"
                                             "    border-radius : 18px;\n"
                                             "\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app/resources/img/icons/24x24/cil-arrow-circle-right.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonConfirm.setIcon(icon)
        self.pushButtonConfirm.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.gridLayout_3.addWidget(
            self.pushButtonConfirm, 2, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 3, 4, 1)
        self.gridLayout_2.addWidget(self.frameDataReceiver, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frameContainer, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonConfirm.setText(_translate("MainWindow", "Confirmar"))




    def set_title(self, title: str):
        return self.labelTitle.setText(title)

    def get_data(self) -> str:
        return self.lineEditData.text()