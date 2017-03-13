from tkinter import*
root = Tk()
canvas = Canvas(root,width = 500, height = 500)
canvas.pack(fill= BOTH)
xreset = 20
yreset = 20
def draw_flag(x,y):
    canvas.create_polygon(58+x*20,50+y*20,67+x*20,55+y*20,58+x*20,60+y*20,fill = 'red')
    canvas.create_line(58+x*20,50+y*20,58+x*20,65+y*20)
    canvas.create_arc(52+x*20,65+y*20,68+x*20,75+y*20,start = 0,extent = 180,fill = 'black',style = CHORD)
def draw_mine(x,y):
    canvas.create_oval(50+x*20,50+y*20,70+x*20,70+y*20,fill = 'black',tag = 'sqwer')
def create_field():
    global square
    square = canvas.create_rectangle(50, 50, 450, 450, fill='#d1cdcd', tag='field')
    for i in range(21):
        canvas.create_line(50, 50 + i * 20, 450, 50 + i * 20, width = 1)
        canvas.create_line(50 + i * 20, 50, 50 + i * 20, 450,width = 1)
    canvas.create_rectangle(10, 10, 10+xreset, 10+yreset, fill='#d1cdcd',tag = 'New',outline = '#d1cdcd')
    #canvas.create_rectangle(10,10,12,10+yreset,fill = 'gray',outline = 'gray')
    #canvas.create_rectangle(10,10)
    #canvas.create_line(10,10,10+xreset,10+yreset,tag = 'New')
    #canvas.create_line(10+xreset, 10, 10, 10+yreset,tag = 'New')
    canvas.update()
def but1(event):
    global xreset,yreset,square
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    draw_mine(x,y)
    #canvas.create_rectangle(50+x*20,50+y*20,70+x*20,70+y*20,fill = 'red',tag = 'sqwer')
    canvas.update()
def clear(event):
    canvas.create_rectangle(10, 10, 10+xreset, 10+yreset, fill='#d1cdcd',tag = 'New',outline = '#d1cdcd')
    #canvas.create()
    canvas.delete('field')
    canvas.delete('New')
    create_field()
def but3(event):
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    #canvas.create_rectangle(50+x*20,50+y*20,70+x*20,70+y*20,fill = 'blue',tag = 'sqwer')
    draw_flag(x,y)
    canvas.update()
create_field()

canvas.tag_bind('field','<Button-1>',but1)
canvas.tag_bind('New','<Button-1>',clear)
canvas.tag_bind('field','<Button-3>',but3)
root.mainloop()

