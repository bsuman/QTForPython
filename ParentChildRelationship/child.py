# This Python file uses the following encoding: utf-8
from PySide6 import QtCore



class child(QtCore.QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        QtCore.qDebug("child constructor called"+str(self)+ str(super))

    def __del__(self):
        QtCore.qDebug("child destructor called"+str(self)+ str(super))
