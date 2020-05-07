# Example 2 using PyQt5 library for Python desktop applications
#   -> procedural programming example 
#   -> Original tutorials: https://www.youtube.com/watch?v=Vde5SH8e1OQ&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj&index=1
# ------------------------------------------------------------------------
# Download only QT designer (mac):
#  =>    https://build-system.fman.io/qt-designer-download

# Download QT Design Studio:
#  =>    https://download.qt.io/official_releases/qtdesignstudio/1.2.0/
# ------------------------------------------------------------------------

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Procedural programming example:

def click():
    print("clicked")


def window():
    app = QApplication(sys.argv) # need to pass argument "argv" from sys
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("PyQt5 Window")

    #set a label with position of label
    label = QtWidgets.QLabel(win)
    label.setText("my first label")
    label.move(50,50) 
    
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(click) # event

    win.show()
    sys.exit(app.exec_())

window()


