from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QLabel,QFileDialog
import sys
import cv2

class c_n (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('video') # 윈도우 명
        self.setGeometry(200,200,500,100) # 윈도우 크기

        v_on=QPushButton('Video On',self)
        v_off=QPushButton('Video Off',self)
        v_sv=QPushButton('Video Saved',self)
        v_c=QPushButton('Video Captured',self)
        self.label=QLabel('Program On',self)

        v_on.setGeometry(10,10,100,30)
        v_off.setGeometry(110,10,100,30)
        v_sv.setGeometry(210,10,100,30)
        v_c.setGeometry(310,10,100,30)
        self.label.setGeometry(410,10,100,30)

        v_on.clicked.connect(self.v_on_f) # 동작 결정
        v_off.clicked.connect(self.v_off_f)
        v_sv.clicked.connect(self.v_sv_f)
        v_c.clicked.connect(self.v_c_f)

    def v_on_f(self):
        self.label.setText('v_on_f 동작')
        self.cam=cv2.VideoCapture(0)
        if not self.cam.isOpened(): self.close()
        while True:
            ret,self.img=self.cam.read()
            if not ret: break
            cv2.imshow('video',self.img)
            cv2.waitKey(1)
    
    def v_off_f(self):
        self.label.setText('v_off_f 동작')
        self.cam.release()
        cv2.destroyAllWindows()
        self.close()

    def v_sv_f(self):
        self.label.setText('v_sv_f 동작')
        fname=QFileDialog.getSaveFileName(self,'파일 저장','./')
        cv2.imwrite(fname[0],self.img)

    def v_c_f(self):
        self.label.setText('v_c_f 동작')
        self.cap_img=self.img
        cv2.imshow('cap_img',self.cap_img)

app=QApplication(sys.argv)
m_win=c_n()
m_win.show()
app.exec()