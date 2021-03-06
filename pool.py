from tkinter import *
import math
import time 

root = Tk()
canv = Canvas(root, width = 2000, height = 2000)
canv.pack()


class table:
    def __init__(self,c1,c2,h,w,x,y):
        self.c1 = c1
        self.c2 = c2
        self.x = x
        self.y = y
        self.h = h
        self.w = w
    def draw(self):
        canv.delete('table')
        canv.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.h,fill = self.c1, outline = self.c2, tag = 'table')

class stick:
    def __init__(self,N,alp,v,l,color,xb,yb):

        self.N = N
        self.l = l
        self.alp = math.radians(alp)
        self.v = v
        self.color = color
        self.xb = xb
        self.yb = yb
    def draw(self):
        #a = ball(self.xb, self.yb, 10, "black", 1)
        canv.delete('stick')
        canv.create_line(self.xb+math.cos(self.alp)*self.v,self.yb-math.sin(self.alp)*self.v,self.xb+math.cos(self.alp)*self.v+math.cos(self.alp)*self.l,self.yb-math.sin(self.alp)*self.v-math.sin(self.alp)*self.l,width=3,fill = 'brown',tag = 'stick')
    def rotate(self,angle):
        self.alp += math.radians(angle)
 #   def select(self,N):
 #       self.N = N
    def redraw(self):
        canv.delete('stick')
        self.xb = a.x
        self.yb = a.y
        stick.draw()
    def charge(self,event):
        self.v += 5
        stick.draw()


class ball:
    def __init__(self, x, y, r, color,N):
        self.N = N
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = 0
        self.vy = 0
        self.v = 0
        self.alp = 0
    def move(self):

        self.x += self.vx
        self.y += self.vy
        if (-2 < self.v and self.v < 2):
            self.v = 0
        else:
            self.v -=1
        if self.vx <0:
            self.vx = -self.v*math.cos(self.alp)
        elif self.vx >0:
            self.vx = -self.v * math.cos(self.alp)
        if self.vy<0:
            self.vy = self.v * math.sin(self.alp)
        elif self.vy>0:
            self.vy = self.v * math.sin(self.alp)
    def collide(self):
        s = math.sqrt((a.x-b.x)**2 +(a.y-b.y)**2)
        if b.y - a.y >0:
            alp1 = math.acos((b.x-a.x)/s)
        else:
            alp1 = -math.acos((b.x-a.x)/s)
        #if
        #if s == a.r+b.r:
           # a.v = a.v +
    def border(self):
        if self.y - self.r <= 0:
            self.vy = -self.vy
            self.alp =( math.radians(90) - (self.alp - math.radians(180)))*2+self.alp
            #self.v = math.sqrt(self.vx**2+self.vy**2)



    def change_sp(self, x,y):
        self.vx+=x
        self.vy+=y
    def draw(self):
        canv.delete(self.N)
        #canv.update()
        canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, tag = self.N)

alp = 50
v = 0
a = ball(200, 200, 10, "black",'a')
b = ball(300, 200, 10, "green",'b')
table = table('green', 'brown',400,200,300,100)
stick = stick(1,alp,v,200,'white',a.x,a.y)

#def move_top(event):
  #  print(1)
   # global a,stick
 #   a.change_sp(0,-10)
  #  stick.redraw()
def change_angle(event):
    global stick
    stick.rotate(5)
    stick.draw()
    a.alp = stick.alp
def change_angle_reversed(event):
    global stick
    stick.rotate(-5)
    stick.draw()
    a.alp = stick.alp

def STRIKE( event):
    a.vx = -math.cos(stick.alp) * stick.v/5
    a.vy = math.sin(stick.alp) * stick.v/5
    a.v = math.sqrt(a.vx**2+a.vy**2)
    stick.v = 0
    stick.draw()



root.bind("<Up>", change_angle_reversed)
root.bind("<Down>", change_angle)
#root.bind("<Left>",move_top)
root.bind("<BackSpace>", stick.charge)
root.bind("<space>",STRIKE)


a.alp = stick.alp

while True:
    #table.draw()
    a.border()
    a.move()
    b.move()
    a.draw()
    b.draw()

    if a.vx == 0 and a.vy == 0:
        stick.redraw()
    canv.update()
    time.sleep(0.02)

root.mainloop()
