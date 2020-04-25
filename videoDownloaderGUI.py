from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QLabel, QLineEdit, \
    QComboBox
from VideoYT import VideoYT
import sys
import re

pattern_res = r'res="([A-Za-z0-9_\./\\-]*)"'
pattern_itag = r'itag="([A-Za-z0-9_\./\\-]*)"'
pattern_abr = r'abr="([A-Za-z0-9_\./\\-]*)"'
pattern_format = r'mime_type="video/([A-Za-z0-9_\./\\-]*)"'


class VideoDownloaderGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.vyt = VideoYT.__class__
        self.choice = '0'
        self.x_size = 500
        self.y_size = 500
        self.url_textbox = QLineEdit(self)
        self.file_name_textbox = QLineEdit(self)
        self.combo_with_preferences = QComboBox(self)
        self.init_gui()

    def init_gui(self):
        self.set_all_widgets()
        self.resize(self.x_size, self.y_size)
        self.center_window()
        self.setWindowTitle("YouTube Downloader")
        self.show()

    def set_all_widgets(self):
        label_enter_url = QLabel(self)
        label_enter_url.setText("Enter YouTube link")
        label_enter_url.move(int(self.x_size / 2 - label_enter_url.width() / 2), 30)

        self.url_textbox.resize(450, 20)
        self.url_textbox.move(int(self.x_size / 2 - self.url_textbox.width() / 2), 50)

        button_get_video = self.set_button(
            self.x_size / 4,
            90,
            "Get this video",
            "Get this video and choose your download preferences"
        )
        button_get_video.clicked.connect(self.get_video_from_url)

        button_get_audio = self.set_button(
            self.x_size * 3 / 4,
            90,
            "Get just audio",
            "Get only audio from video and choose your download preferences"
        )
        button_get_audio.clicked.connect(self.get_audio_from_url)

        self.combo_with_preferences.resize(400, 40)
        self.combo_with_preferences.move(int(self.x_size/2 - self.combo_with_preferences.width()/2), 130)

        self.file_name_textbox.resize(200, 20)
        self.file_name_textbox.move(int(self.x_size/2 - self.file_name_textbox.width()/2), 200)

        button_download = self.set_button(
            self.x_size/2,
            230,
            "Download",
            "Download and save with selected preferences"
        )
        button_download.clicked.connect(self.download_file)

    def download_file(self):
        self.vyt.download_video(self.file_name_textbox.text(), self.combo_with_preferences.currentData(), self.choice)

    def get_video_from_url(self):
        self.choice = '1'
        url = self.url_textbox.text()
        self.vyt = VideoYT(url)
        by_resolution = self.vyt.get_video_resolutions()
        self.combo_with_preferences.clear()
        for x in by_resolution:
            print(x)
            self.combo_with_preferences.addItem("Video itag: {0}, resolution: {1}, format: {2}\n"
                                                .format(
                                                    re.search(pattern_itag, str(x)).group(1),
                                                    re.search(pattern_res, str(x)).group(1),
                                                    re.search(pattern_format, str(x)).group(1)),
                                                re.search(pattern_itag, str(x)).group(1))

    def get_audio_from_url(self):
        self.choice = '2'
        url = self.url_textbox.text()
        self.vyt = VideoYT(url)
        self.combo_with_preferences.clear()

        for x in self.vyt.get_sound_only():
            self.combo_with_preferences.addItem("Audio itag: {0}, quality: {1}\n"
                                                .format(re.search(pattern_itag, str(x)).group(1),
                                                        re.search(pattern_abr, str(x)).group(1)),
                                                re.search(pattern_itag, str(x)).group(1))

    def set_button(self, x, y, butt_tittle, description):
        butt = QPushButton(butt_tittle, self)
        butt.setToolTip(description)
        butt.resize(butt.sizeHint())
        butt.move(int(x - butt.width() / 2), int(y))
        return butt

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vd = VideoDownloaderGUI()
    sys.exit(app.exec_())
