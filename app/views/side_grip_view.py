# -*- coding: utf-8 -*-


from PyQt5 import (
    QtCore,
    QtWidgets,
)




class SideGripView(QtWidgets.QWidget):

    def __init__(self, parent, edge):
        QtWidgets.QWidget.__init__(self, parent)
        
        #   border-bottom-left-radius: 24px;
        #   border-radius: 20px;

        self.WidgetSideGrip = QtWidgets.QWidget(self)
        self.WidgetSideGrip.setObjectName('WidgetSideGrip')
        self.WidgetSideGrip.setStyleSheet('''
            QWidget#WidgetSideGrip {
                border: 12px solid #46355e;
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

