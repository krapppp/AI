from PyQt6.QtWidgets import QMainWindow,QApplication
import sys
import cv2

class c_n (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('윈도우 이름') # 윈도우 명
        self.setGeometry(200,200,600,100) # 윈도우 크기

app=QApplication(sys.argv)
m_win=c_n()
m_win.show()
app.exec()