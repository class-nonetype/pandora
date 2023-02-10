# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


class DataReceiverWindowView(QtWidgets.QMainWindow):

    def __init__(self, Controller):
        super().__init__()

        self.Controller = Controller

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.FramelessWindowHint)

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

    def setupUi(self):
        self.setObjectName("mainWindow")
        self.setEnabled(True)
        self.resize(800, 150)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.frameContainer = QtWidgets.QFrame(self.centralwidget)
        self.frameContainer.setObjectName(u"frameContainer")
        self.frameContainer.setStyleSheet(u"QFrame {\n"
                                          "\n"
                                          "	background-color : #5F3E77;\n"
                                          "}")
        self.frameContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameContainer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameContainer.setLineWidth(0)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameContainer)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.horizontalSpacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 4)

        self.lineEditData = QtWidgets.QLineEdit(self.frameContainer)
        self.lineEditData.setObjectName(u"lineEditData")
        self.lineEditData.setMinimumSize(QtCore.QSize(480, 0))
        self.lineEditData.setMaximumSize(QtCore.QSize(480, 16777215))
        self.lineEditData.setStyleSheet(u"QLineEdit{\n"
                                        "	background-color: #000000;\n"
                                        "	font : 22 15pt \"Microsoft JhengHei UI Light\";\n"
                                        "	color : #FFFFFF;\n"
                                        "	border-radius : 0px;\n"
                                        "	text-align : left;\n"
                                        "	padding : 2px;\n"
                                        "	border-top : 2px solid #D37242;\n"
                                        "	border-bottom : 2px solid #D37242;\n"
                                        "	border-left : 2px solid #D37242;\n"
                                        "	border-right: 2px solid #D37242;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit:hover{\n"
                                        "	background-color: #000000;\n"
                                        "	font : 22 15pt \"Microsoft JhengHei UI Light\";\n"
                                        "	color : #FFFFFF;\n"
                                        "\n"
                                        "}")

        self.gridLayout_2.addWidget(
            self.lineEditData, 2, 1, 1, 1, QtCore.Qt.AlignLeft)

        self.horizontalSpacer_2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.pushButtonConfirm = QtWidgets.QPushButton(self.frameContainer)
        self.pushButtonConfirm.setObjectName(u"pushButtonConfirm")
        self.pushButtonConfirm.setMinimumSize(QtCore.QSize(170, 36))
        self.pushButtonConfirm.setMaximumSize(QtCore.QSize(170, 36))
        self.pushButtonConfirm.setStyleSheet(u"QPushButton{\n"
                                             "	background-color: #D37242;\n"
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
                                             "	background-color: #000000;\n"
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
        icon = QtGui.QIcon()
        icon.addFile(u"app/resources/img/icons/24x24/cil-arrow-circle-right.png",
                     QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonConfirm.setIcon(icon)
        self.pushButtonConfirm.setIconSize(QtCore.QSize(24, 24))

        self.gridLayout_2.addWidget(
            self.pushButtonConfirm, 2, 2, 1, 1, QtCore.Qt.AlignRight)

        self.labelTitle = QtWidgets.QLabel(self.frameContainer)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"QLabel {\n"
                                      "\n"
                                      "	font : 25 15pt \"Microsoft YaHei UI Light\";\n"
                                      "	color : #FFFFFF;\n"
                                      "	\n"
                                      "	text-align: left;\n"
                                      "\n"
                                      "}")

        self.gridLayout_2.addWidget(self.labelTitle, 0, 1, 2, 3)

        self.gridLayout.addWidget(self.frameContainer, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.pushButtonConfirm.setText(
            QtCore.QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.labelTitle.setText("")
    # retranslateUi

    def set_title(self, title: str):
        return self.labelTitle.setText(title)

    def get_data(self) -> str:
        return self.lineEditData.text()
