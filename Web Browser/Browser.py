import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(lambda i: self.tabs.removeTab(i) if self.tabs.count() > 1 else None)
        self.setCentralWidget(self.tabs)
        self.add_tab()
        self.showMaximized()
        
        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)  
        
        back_button = QAction('Back', self)
        back_button.triggered.connect(lambda: self.tabs.currentWidget().back())
        navbar.addAction(back_button)
        
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navbar.addAction(forward_button)
        
        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navbar.addAction(reload_button)
        
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)
        
        new_tab_btn = QAction('+', self)
        new_tab_btn.triggered.connect(lambda: self.add_tab())
        navbar.addAction(new_tab_btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        
    def add_tab(self, url=QUrl("http://duckduckgo.com")):
        browser = QWebEngineView()
        browser.setUrl(url)
        browser.urlChanged.connect(self.update_url)
        i = self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentIndex(i)


        
        
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl('https://duckduckgo.com'))
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.tabs.currentWidget().setUrl(QUrl(url))
        
    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Chrome = bloat')
window = MainWindow()
app.exec()
