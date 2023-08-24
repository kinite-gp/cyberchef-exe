from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

pwd = os.getcwd()
print(pwd)

url = "file:///" + pwd.replace("\\","/") + "/chef/main.html"

print(f"{url}")

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowIcon(QIcon("small.ico"))

        self.resize(700, 700)

        self.browser = QWebEngineView()
        self.browser.setPage(QWebEnginePage(self.browser))
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.show()

app = QApplication(sys.argv)
app.setApplicationName("CyberChef")
window = MainWindow()
window.browser.load(QUrl(url))
app.exec_()