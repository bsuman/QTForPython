# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QTextStream,qDebug

def print_to_console():
    print("Enter you name:")
    name = str(input())
    print("Entered Name is:",name)

def print_to_console_qt():
    file = QFile()
    file.open(sys.stdin.fileno(), QFile.ReadOnly)
    stream = QTextStream(file)

    ofile = QFile()
    ofile.open(sys.stdout.fileno(), QFile.WriteOnly)
    stream2 = QTextStream(ofile)

    stream2 <<"Enter your name:"
    stream2.flush()

    name = stream.readLine()

    stream2 << "Entered name is " << name
    stream2.flush()

    file.close()
    ofile.close()

def print_to_console_debug():
    stream2 = "Enter your name:"
    qDebug(stream2)
    file = QFile()
    file.open(sys.stdin.fileno(), QFile.ReadOnly)
    stream = QTextStream(file)
    name = stream.readLine()
    stream2 =  "Entered name is " + name
    qDebug(stream2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #print_to_console()
    #print_to_console_qt()
    print_to_console_debug()
    sys.exit(app.exec())
