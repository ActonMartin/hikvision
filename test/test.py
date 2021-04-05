from ui.ui_test import Ui_MainWindow
from PyQt5.QtCore import QObject, QSettings, QTimer, Qt, pyqtSignal,QEvent
from PyQt5.QtGui import QCursor, QIcon, QImage, QPixmap, QTextCursor
from PyQt5.QtWidgets import (QApplication, QFileSystemModel, QGraphicsPixmapItem, QGraphicsScene, QMainWindow, QMenu,QMessageBox)
import sys
from camera import Camera
import cv2

class mainwindows(QMainWindow):
    def __init__(self):
        super(mainwindows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cam1 = Camera()
        self.cam1.activatecamera(0)
        self.ui.pushButton.clicked.connect(self.takeshot)
        self.timer_camera = QTimer()
        self.timer_camera.timeout.connect(self.show_image_on_label)
        self.timer_camera.start(100)


    def takeshot(self):
        self.cam1.takeshot()

    def show_image_on_label(self):
        self.image = self.cam1.show_thread()
        show = cv2.resize(self.image, (int(1200), int(960)))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.ui.label.setPixmap(QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage





if __name__ == "__main__":
    APP = QApplication(sys.argv)
    LOGWINDOW = mainwindows()
    LOGWINDOW.show()
    sys.exit(APP.exec_())