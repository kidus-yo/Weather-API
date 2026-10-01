import sys
import requests
from PyQt5.QtWidgets  import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class WeatherAPI(QWidget):
    def __init__(self):
        super().__init__()
        self.city_Label = QLabel("Enter city name?: ", self)
        self.city_name= QLineEdit(self)
        self.weather_buttton = QPushButton("Get Weather", self)


def main():
    app = QApplication(sys.argv)
    windows= WeatherAPI()
    windows.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    