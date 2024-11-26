from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl


class Window(QWidget):

    def __init__(self, filename):
        super().__init__()

        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 600, 300)
        self.setWindowIcon(QIcon('player.png'))
        self.content_path = filename

        p = self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)

        self.init_ui()

        self.show()

    def init_ui(self):

        # Create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # Create video widget object
        videowidget = QVideoWidget()
        videowidget.setStyleSheet("border: 2px solid rgb(0, 43, 91)")

        # Create open button
        openBtn = QPushButton('Open File')
        openBtn.clicked.connect(self.open_file)

        # Create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setIcon(QIcon('Frontend\Images\play_btn.png'))
        self.playBtn.setFixedSize(150, 50)
        self.playBtn.clicked.connect(self.play_video)
        self.playBtn.setStyleSheet("QPushButton {\n"
                                   "border: 3px solid rgb(43, 72, 101);\n"
                                   "border-radius: 10px;\n"
                                   "background-color: rgb(43, 72, 101);\n"
                                   "color: rgb(137, 218, 199)\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::hover:!pressed {\n"
                                   "background-color: rgb(0, 43, 91);\n"
                                   "border: 3px solid rgb(0, 43, 91); \n"
                                   "}")

        # Create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)
        self.slider.setStyleSheet("QSlider::handle:horizontal {background-color:#002B5B;}")

        # Create volume slider
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setFixedSize(150, 30)
        self.volume_slider.sliderMoved.connect(self.set_volume)
        self.volume_slider.setStyleSheet("QSlider::handle:horizontal {background-color:#002B5B;}")

        # Create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Create volume label
        self.volume_lbl = QLabel("Volume")
        self.volume_lbl.setStyleSheet("color: white")
        self.volume_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.volume_lbl.setMinimumSize(350, 0)
        self.volume_lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # Set widgets to the hbox layout
        hboxLayout.addWidget(self.slider)

        hbox2 = QHBoxLayout()
        # hbox2.addWidget(openBtn)
        hbox2.addWidget(self.playBtn)
        hbox2.addWidget(self.volume_lbl)
        hbox2.addWidget(self.volume_slider)

        # Create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addLayout(hbox2)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)

        filename = self.content_path

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))

        # Media player signals
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.volumeChanged.connect(self.volume_changed)
        self.mediaPlayer.setVolume(50)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):

        print('Playing...')

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(QIcon('Frontend\Images\pause_btn.png'))

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
            )

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

    def volume_changed(self, volume):
        self.volume_slider.setValue(volume)

    def set_volume(self, volume):
        self.mediaPlayer.setVolume(volume)

# app = QApplication(sys.argv)
# window = Window()
# sys.exit(app.exec_())
