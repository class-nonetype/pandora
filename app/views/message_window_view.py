from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from PyQt5.QtCore import (
    Qt

)

from PyQt5.QtWidgets import (
    QMessageBox
)

from PyQt5 import (QtWidgets, QtCore)

class MessageWindowView(QMessageBox):

    def __init__(self):
        QMessageBox.__init__(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)


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

    def set_title(self, title : str):
        self.title = title
        return self.title

    def set_message(self, message : str):
        self.message = message
        return self.message
    
    def set_status(self, status : str):
        self.status = status
        return self.status

    def setupUi(self):

        self.setWindowTitle(self.title)
        self.resize(450, 280)

        self.setText(self.message)
        self.setIcon(self.status)

        # Naranjo : D37242
        
        self.setStyleSheet(
            "QLabel{\n"
            "    font : 75 12pt \"Microsoft JhengHei UI\";\n"
            "    color : #FFFFFF;\n"
            "    border-radius : 0px;\n"
            "    text-align : left;\n"
            "    border : flat 0px;\n"
            "}\n"
            "\n"

            "QWidget {\n"
            "    background-color: #5F3E77;\n"
            "    border : flat 1px;\n"
            "}\n"
            "\n"

            "QPushButton{\n"
            "    background-color : #D37242;\n"
            "    font : 75 13pt \"Microsoft JhengHei UI\";\n"
            "    color : #FFFFFF;\n"
            "    border-radius : 0px;\n"
            "    border : flat 0px;\n"
            "    border-top-left-radius: 12px;\n"
            "    border-bottom-left-radius: 12px;\n"
            "    border-top-right-radius: 12px;\n"
            "    border-bottom-right-radius: 12px;\n"
            "    width : 60px;"
            "    text-align : center;\n"
            "    padding-left: 8px;\n"
            "    padding-right: 8px;\n"
            "    padding-top: 5px;\n"
            "    padding-bottom: 5px;\n"
            "}\n"
            "\n"

            "QPushButton:hover{\n"
            "    background-color: #FFFFFF;\n"
            "    font : 75 13pt \"Microsoft JhengHei UI\";\n"
            "    color : #000000;\n"
            "    border : flat 0px;\n"
            
            "    border-top-left-radius: 12px;\n"
            "    border-bottom-left-radius: 12px;\n"
            "    border-top-right-radius: 12px;\n"
            "    border-bottom-right-radius: 12px;\n"
            "}\n"
            "\n"

            "QFrame {\n"
            "    background-color: #5F3E77;\n"
            #"    border: 2px solid;\n"
            #"    border-color : #D37242;\n"
            "}"

        )
