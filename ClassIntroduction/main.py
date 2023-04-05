# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import *
from Test import Test

if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Test()
    t.close.connect(app.quit, type=Qt.QueuedConnection)
    #QObject.connect(t, SIGNAL('close()'), app.quit, type=Qt.QueuedConnection)
    t.do_stuff()
    val = app.exec()
    qDebug("Value from the receiving the signal: "+ str(val))
    sys.exit(val)
