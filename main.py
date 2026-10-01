import sys
import requests
from PyQt5.QtWidgets  import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class WeatherAPI(QWidget):
    def __int__(self):
        pass
        super().__init__()
        pass


def main():
    app = QApplication(sys.argv)
    windows= WeatherAPI()
    windows.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    