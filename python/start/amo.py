import turtle as t
 
t.setup(500, 700)
body_color = 'red'
glacss_color = 'skyblue'

 
# 몸 그리기
def body(): 
    t.pensize(20)
    t.fillcolor(body_color)
    t.begin_fill()
 
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)
 
    t.right(180)
    t.circle(100, -180)
 
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)
 
    t.circle(40, -180)
 
    t.left(7)
    t.backward(50)
 
    t.penup()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    t.right(240)
    t.circle(50, -70)
 
    t.end_fill()
 
# 글래스 그리기
def glass():
    t.penup()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
 
    t.pendown()
    t.fillcolor(glacss_color)
    t.begin_fill()
 
    t.right(150)
    t.circle(90, -55)
 
    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
 
    t.circle(50, -190)
    t.right(170)
    t.forward(80)
 
    t.right(180)
    t.circle(45, -30)
 
    t.end_fill()
 
# 어몽어스 가방 그리기
def Bag():
    t.penup()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)
 
    t.fillcolor(body_color)
    t.begin_fill()
 
    t.pendown()
    t.forward(30)
    t.right(255)
 
    t.circle(300, -30)
    t.right(260)
    t.forward(30)
 
    t.end_fill()
 
 
body()
glass()
Bag()
t.ht() # 마지막 터틀을 숨김
 
t.mainloop()