from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QLabel,QFileDialog
import sys
import cv2
import numpy as np

class c_n (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('그림 분할') # 윈도우 명
        self.setGeometry(200,200,600,100) # 윈도우 크기

        f_l_b=QPushButton('File Load',self)
        b_i_b=QPushButton('Drawing',self)
        p_b=QPushButton('+',self)
        m_b=QPushButton('-',self)
        c_b=QPushButton('Cut',self)
        s_b=QPushButton('Saved',self)
        e_b=QPushButton('End',self)
        
        self.label=QLabel('Program On',self)
        self.p_label=QLabel('  ',self)

        f_l_b.setGeometry(10,10,100,30)
        b_i_b.setGeometry(110,10,100,30)
        p_b.setGeometry(210,10,50,30)
        m_b.setGeometry(260,10,50,30)
        c_b.setGeometry(310,10,100,30)
        s_b.setGeometry(410,10,100,30)
        e_b.setGeometry(510,10,100,30)
        self.label.setGeometry(10,50,200,30)
        self.p_label.setGeometry(210,50,200,20)

        f_l_b.clicked.connect(self.f_l_b_f)
        b_i_b.clicked.connect(self.b_i_b_f)
        p_b.clicked.connect(self.p_b_f)
        m_b.clicked.connect(self.m_b_f)
        c_b.clicked.connect(self.c_b_f)
        s_b.clicked.connect(self.s_b_f)
        e_b.clicked.connect(self.e_b_f)

        self.L_C,self.R_C=(0,0,255),(255,0,0)
        self.P_SIZE=5

    def f_l_b_f(self): # 파일 로드
        l_fname=QFileDialog.getOpenFileName(self,'File Load','./')
        self.img=cv2.imread(l_fname[0])
        if self.img is None: sys.exit('File is None')
        self.label.setText('File Load Success')
        self.show_img=self.img.copy()
        cv2.imshow('show_img',self.show_img)
        self.mask = np.zeros((self.img.shape[0], self.img.shape[1]), dtype=np.uint8)
        self.mask[:,:]=cv2.GC_PR_BGD

    def dw_b(self,event,x,y,f,p): # 붓 소환
        if event==cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self.show_img,(x,y),self.P_SIZE,self.L_C,self,-1)
            cv2.circle(self.mask,(x,y),self.P_SIZE,cv2.GC_FGD,self,-1)
        elif event==cv2.EVENT_RBUTTONDOWN:
            cv2.circle(self.show_img,(x,y),self.P_SIZE,self.R_C,self,-1)
            cv2.circle(self.mask,(x,y),self.P_SIZE,cv2.GC_FGD,self,-1)
        elif event==cv2.EVENT_MOUSEMOVE and f==cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(self.show_img,(x,y),self.P_SIZE,self.L_C,-1)
            cv2.circle(self.mask,(x,y),self.P_SIZE,cv2.GC_FGD,-1)
        elif event==cv2.EVENT_MOUSEMOVE and f==cv2.EVENT_FLAG_RBUTTON:
            cv2.circle(self.show_img,(x,y),self.P_SIZE,self.R_C,-1)
            cv2.circle(self.mask,(x,y),self.P_SIZE,cv2.GC_FGD,-1)
        cv2.imshow('show_img',self.show_img)

        
    def b_i_b_f(self): # 붓 소환
        self.label.setText('Summon Tool')
        self.p_label.setText(f'size : {self.P_SIZE}')
        cv2.setMouseCallback('show_img',self.dw_b)

    def p_b_f(self): # 붓크기 증가
        self.P_SIZE=min(30,self.P_SIZE+1)
        self.p_label.setText(f'size : {self.P_SIZE}')

    def m_b_f(self): # 붓크기 감소
        self.P_SIZE=min(30,self.P_SIZE-1)
        self.p_label.setText(f'size : {self.P_SIZE}')

    def c_b_f(self): # 자르기 기능
        backgr=np.zeros((1,65),np.float64)
        forgr=np.zeros((1,65),np.float64)
        cv2.grabCut(self.img,self.mask,None,backgr,forgr,5,cv2.GC_INIT_WITH_MASK)
        mask1=np.where((self.mask==cv2.GC_BGD)|(self.mask==cv2.GC_PR_BGD),0,1).astype('uint8')
        self.cut_img=self.img*mask1[:,:,np.newaxis]
        cv2.imshow('cut_img',self.cut_img)

    def s_b_f(self): # 파일 저장
        s_fname=QFileDialog.getSaveFileName(self,'File Saved','./')
        cv2.imwrite(s_fname[0], self.cut_img)

    def e_b_f(self): # 종료 기능
        cv2.destroyAllWindows()
        self.close()

app=QApplication(sys.argv)
m_win=c_n()
m_win.show()
app.exec()