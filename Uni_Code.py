from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.urlList = []
        self.i = 0
        self.setWindowTitle("Uni-Code")
        self.setWindowIcon(QIcon("icons/logo.png"))
        self.browser = QWebEngineView(self)
        home = "http://google.com"
        self.browser.load(QUrl(home))

        self.update_title()
        self.browser.show()
        self.history()

        #Buttons
        self.back_button = QPushButton(self)
        self.back_button.setIcon(QIcon('icons/back-button.png'))
        self.back_button.clicked.connect(self.backbutton)

        self.next_button = QPushButton(self)
        self.next_button.setIcon(QIcon('icons/next-button.png'))
        self.next_button.clicked.connect(self.forwardbutton)

        self.reload_button = QPushButton(self)
        self.reload_button.setIcon(QIcon('icons/refresh-button.png'))
        self.reload_button.clicked.connect(self.reloadbutton)

        self.home_button = QPushButton(self)
        self.home_button.setIcon(QIcon('icons/home-button.png'))
        self.home_button.clicked.connect(self.navigate_home)

        self.search_button = QPushButton(self)
        self.search_button.setIcon(QIcon('icons/logo.png'))
        self.search_button.clicked.connect(self.navigate_to_url)

        #url bar
        self.urlbar = QLineEdit(self)
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setFont(QFont("Calibri", 12))
        self.urlbar.setText(home)

        #tool bar
        self.tool_bar = QHBoxLayout()
        self.tool_bar.addWidget(self.back_button)
        self.tool_bar.addWidget(self.next_button)
        self.tool_bar.addWidget(self.reload_button)
        self.tool_bar.addWidget(self.home_button)
        self.tool_bar.addWidget(self.urlbar)
        self.tool_bar.addWidget(self.search_button)

        #tool bar + web page
        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.tool_bar)
        self.v_box.addWidget(self.browser)
        self.setLayout(self.v_box)

        self.show()

    #after clicked back button
    def backbutton(self):
        self.i -= 1
        self.browser.load(QUrl(self.urlList[self.i - 1]))
        self.urlbar.setText(self.browser.url().toString())
        #print(self.urlList)
        self.button_check()

    #after clicked next button
    def forwardbutton(self):
        self.i += 1
        self.browser.load(QUrl(self.urlList[self.i - 1]))
        self.urlbar.setText(self.browser.url().toString())
        #print(self.urlList)
        self.button_check()

    #web browser name
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s  Uni-Code" % title)

    #after clicked home button
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))
        self.browser.load(QUrl("http://google.com"))
        self.update_title()
        self.button_check()

    #after clicked search button
    def navigate_to_url(self):
        url = "https://" + self.urlbar.text()
        self.browser.load(QUrl(url))
        self.update_title()
        self.urlbar.setText(self.browser.url().toString())
        self.history()
        print(self.urlList)
        self.button_check()

    def history(self):
        urlx = self.browser.url().toString()
        self.urlList.append(urlx)
        self.i += 1
        #print(self.urlList)
        #print(self.i)

    #after clicked refrech button
    def reloadbutton(self):
        url1 = self.urlbar.text()
        self.browser.load(QUrl(url1))
        self.update_title()
        self.urlbar.setText(self.browser.url().toString())
        print(url1)
        self.button_check()

    def button_check(self):
        #print("checkbuttons: i = " )
        #print(self.i)
        if self.i == 1:
            self.back_button.setEnabled(0)
        else:
            self.back_button.setEnabled(1)
        if self.i == len(self.urlList):
            self.next_button.setEnabled(0)
        else:
            self.next_button.setEnabled(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.processEvents()
    window = MainWindow()
    sys.exit(app.exec())
