import sys
import subprocess

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QToolBar, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

class App:
    def __init__(self):
        self.title = None
        self.php_path = None
        self.url_port = None
        self.app_created = False
        
    def create_app(self, window_title:str, url_port:int, php_path:str):
        self.title = window_title
        self.url_port = url_port
        self.php_path = php_path
        self.app_created = True
        
    def run(self):
        try:
            self.__start_php__()
            self.__start_widget__()
        except Exception as e:
            print(e)
            
        finally:
            self.php_process.terminate()
        
    def __start_php__(self):
        self.php_process = subprocess.Popen(
            [
                "php",
                "-S", f"127.0.0.1:{self.url_port}",
                "-t", f"{self.php_path}"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
    def __start_widget__(self):
        app = QApplication(sys.argv)
                    
        window = QMainWindow()
        window.setWindowTitle(self.title)
        window.resize(600, 400)
                
        webview = QWebEngineView()
        webview.setUrl(QUrl(f"http://127.0.0.1:{self.url_port}/"))
        window.setCentralWidget(webview)
                
        window.show()
        sys.exit(app.exec())
    