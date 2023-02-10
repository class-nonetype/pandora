# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets
from PyQt5 import QtCore


class ProgressWindowView(QtWidgets.QMainWindow):

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

        self.horizontalSpacer_2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.labelProgress = QtWidgets.QLabel(self.frameContainer)
        self.labelProgress.setObjectName(u"labelProgress")
        self.labelProgress.setStyleSheet(u"QLabel {\n"
                                         "\n"
                                         "	font : 25 15pt \"Microsoft YaHei UI Light\";\n"
                                         "	color : #FFFFFF;\n"
                                         "	\n"
                                         "	text-align: left;\n"
                                         "\n"
                                         "}")

        self.gridLayout_2.addWidget(self.labelProgress, 0, 1, 1, 1)

        self.progressBar = QtWidgets.QProgressBar(self.frameContainer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
                                       "	border: 2px solid #D37242;\n"
                                       "	border-radius: 5px;\n"
                                       "	text-align: center;\n"
                                       "	font : 77 12pt \"Microsoft JhengHei UI\" bold;\n"
                                       "	color : #999999;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "	background-color: #61364F;\n"
                                       "	margin: 0.5px;\n"
                                       "}")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(
            QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout_2.addWidget(self.progressBar, 1, 1, 1, 1)

        self.horizontalSpacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.verticalSpacer = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.gridLayout.addWidget(self.frameContainer, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.labelProgress.setText("")
