# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Signal, qDebug


class Test(QObject):
    close = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def do_stuff(self):
        qDebug("Doing stuff in Python!!")
        self.close.emit()
