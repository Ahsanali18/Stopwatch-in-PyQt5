# Python PyQt5 Stopwatch
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSoundEffect

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        stopwatch_image_path = "Project#02 Stopwatch/stopwatch_image.png"
        self.setWindowIcon(QIcon(stopwatch_image_path))
        self.time = QTime(0,0,0,0)
        self.sound = QSoundEffect()
        self.time_label= QLabel("00:00:00:00",self)
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.timer = QTimer(self)

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200,100%,85%);
                border-radius: 20px;
            }
        """)

        sound_file_path = "Project#02 Stopwatch/stopwatch_sound.wav"
        self.sound.setSource(QUrl.fromLocalFile(sound_file_path))
        self.sound.setVolume(0.25)
        self.sound.setLoopCount(QSoundEffect.Infinite)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    #method to start the stopwatch
    def start(self):
        self.timer.start(10)
        self.sound.play()

    #method to stop the stopwatch
    def stop(self):
        self.timer.stop()
        self.sound.stop()

    #method to reset the stopwatch
    def reset(self):
        self.timer.stop()
        self.sound.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))
        
    #method to format the stopwatch time
    def format_time(self, time):
        hourse = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 
        return f"{hourse:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    #method to update the display of stopwatch
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())