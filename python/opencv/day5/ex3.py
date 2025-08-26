from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QLabel,QFileDialog
import sys
import cv2
import numpy as np

class c_n (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('윈도우 이름') # 윈도우 명
        self.setGeometry(200,200,600,100) # 윈도우 크기

        v_b=QPushButton('Collect Video',self)
        self.ck_ci_b=QPushButton('Check Video',self)
        self.ct_b=QPushButton('Connect Video',self)
        self.s_b=QPushButton('Save Video',self)
        e_b=QPushButton('End',self)
        self.label=QLabel('Program On',self)

        v_b.setGeometry(10,10,100,30)
        self.ck_ci_b.setGeometry(110,10,100,30)
        self.ct_b.setGeometry(210,10,100,30)
        self.s_b.setGeometry(310,10,100,30)
        e_b.setGeometry(410,10,100,30)
        self.label.setGeometry(10,50,520,30)

        self.ck_ci_b.setEnabled(False)
        self.ct_b.setEnabled(False)
        self.s_b.setEnabled(False)

        v_b.clicked.connect(self.v_b_f)
        self.ck_ci_b.clicked.connect(self.ck_ci_b_f)
        self.ct_b.clicked.connect(self.ct_b_f)
        self.s_b.clicked.connect(self.s_b_f)
        e_b.clicked.connect(self.e_b_f)

    def v_b_f(self):
        self.ck_ci_b.setEnabled(False)
        self.ct_b.setEnabled(False)
        self.s_b.setEnabled(False)
        self.label.setText('c : capture / esc : finish')

        self.cam=cv2.VideoCapture(0)
        if not self.cam.isOpened():sys.exit('Cam Connect Failed')

        self.imgs=[]
        while True:
            ret,img=self.cam.read()
            if not ret:
                print("Capture's Unabled")
                break
            cv2.imshow('v_img',img)
            key=cv2.waitKey(1)

            if key==ord('c'):
                self.imgs.append(img)
            elif key==27:
                self.cam.release()
                cv2.destroyAllWindows('v_img')
                break
            
        if len(self.imgs)>=2:
            self.ck_ci_b.setEnalbed(True)
            self.ct_b.setEnabled(True)
            self.s_b.setEnalbed(True)
    
    def ck_ci_b_f(self):
        self.label.setText(f'imgs : {len(self.imgs)}')
        sk=cv2.resize(self.imgs[0],dsize=(0,0),fx=0.25,fy=0.25)
        for i in range(1,len(self.imgs)):
            sk=np.hstack((sk,cv2.resize(self.imgs[0],dsize=(0,0),fx=0.25,fy=0.25)))
        cv2.imshow('ck_img',sk)
    
    def ct_b_f(self):
        stit=cv2.Stitcher().create()
        st,self.s_imgs=stit.stitch(self.imgs)
        if st==cv2.STITCHER_OK:
            cv2.imshow('end_img',self.s_img)
        else:
            self.label.setText('Panorama Making Failed')
        
    def s_b_f(self):
        s_fname=QFileDialog.getSaveFileName(self,'File Saved','./')
        cv2.imwrite(s_fname[0],self.s_img)

    def e_b_f(self):
        cv2.destroyAllWindows()
        self.close()

app=QApplication(sys.argv)
m_win=c_n()
m_win.show()
app.exec()