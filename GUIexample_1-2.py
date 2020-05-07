# Example 2 Part 2: using PyQt5 library for Python desktop applications
#   -> convertion to OOP from part 1
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

class MyWindow(QMainWindow):
    def __init__(self):
        # inherit all properties from QMainWindow)
        super(MyWindow, self).__init__()
        self.setGeometry(500, 200, 400, 300)
        self.setWindowTitle("PyQt5 Window")

        # keeps code clean; all the stuff we want in the window
        self.initUI()

    def initUI(self):
        #set a label with position of label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My new label")
        self.label.move(50,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.click) # event

    def click(self):
        self.label.setText("you still suck. keep mf learning shit")
        self.update()

    # called everytime there's a change to the window
    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv) # need to pass argument "argv" from sys
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window() 

