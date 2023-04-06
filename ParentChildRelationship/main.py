# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer,qDebug
from child import child

def getlist(app,clist):
    for i in range(10):
        c = child(app)
        c.setObjectName("class"+str(i))
        clist.append(c)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clist = []
    getlist(app,clist)
    clist.clear()
    timer = QTimer()
    timer.singleShot(2000,app.quit)
    val = app.exec()
    qDebug("Application exited with code"+ str(val))
    sys.exit()
