# Example 1 Part 1: using PyQt5 library for Python desktop applications
#     -> Using OOP
# ------------------------------------------------------------------------
# Download only QT designer (mac):
#  =>    https://build-system.fman.io/qt-designer-download

# Download QT Design Studio:
#  =>    https://download.qt.io/official_releases/qtdesignstudio/1.2.0/
# ------------------------------------------------------------------------

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


# main window class that inherets from QMainWindow
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 500, 400) # x_position, y_position, width, height
        self.setWindowTitle("PyQt5 Window")

        self.show()

# create application object
app = QApplication(sys.argv) # need to pass argument "argv" from sys

# create object from the windom
window = Window()

# waiting on application to excit and then execute to close the application
sys.exit(app.exec_())
