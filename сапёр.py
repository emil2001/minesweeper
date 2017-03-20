from tkinter import*
import random
root = Tk()
canvas = Canvas(root,width = 500, height = 500)
canvas.pack(fill= BOTH)
xreset = 20
yreset = 20
ifield = 20
jfield = 20


n = 20
m = 20
list = [[000] * (m+1) for i in range(n+1)]
k = 75
x = random.randint(0, m - 1)
y = random.randint(0, n - 1)
list[y][x] = 100
queue = [(x, y)]


def dfs():
    global queue,ifield,jfield,listA

    for i in range(k):
        x = random.randint(1, m - 2)
        y = random.randint(1, n - 2)
        list[y][x] = 100
        queue += [(x, y)]
    #print(queue)
    # for i in range(n):
    #    for j in range(m):
    #        print(list[i][j], end = ' ')
    #    print()
    for i in range(1,ifield):
        for j in range(1,jfield):
            x1 = i
            y1 = j
            mine_count = (list[y1 - 1][x1 - 1] + list[y1][x1 - 1] + list[y1 + 1][x1 - 1] + list[y1 + 1][x1] + list[y1 - 1][x1] +
                          list[y1 - 1][x1 + 1] + list[y1][x1 + 1] + list[y1 + 1][x1 + 1]) // 100
            #print(mine_count)
            if_mine = list[y1][x1]
            if if_mine == 100:
                draw_mine(x1,y1)
            #print(mine_count)
            list[y1][x1] = if_mine + mine_count

    #print(list)

def field_open(x,y):
    global list
    queue = [(x,y)]
    while len(queue) >0:
        i,j = queue.pop(0)
        if list[j][i]%10 != 0 and (list[j][i] // 10) % 10 == 0 :
            canvas.create_rectangle(50 + i * 20, 50 + j * 20, 50 + (i + 1) * 20, 50 + (j + 1) * 20, fill='red')
            canvas.create_text(60+i*20,60+j*20,text = list[j][i]%10)
            #print('game over')
            list[j][i] = list[j][i] // 100 + 10 + list[j][i] % 10
        if (list[j][i] // 10) % 10 == 0 and list[j][i]%10 ==0 and list[j][i]//100 == 0:
            canvas.create_rectangle(50+i*20,50+j*20,50+(i+1)*20,50+(j+1)*20, fill = 'red')
            list[j][i] = list[j][i]//100 + 10 + list[j][i]%10
            if i>=1:
                if j>=1:
                    queue += [(i-1,j-1)]
                queue += [(i-1, j)]
                if j<len(list)-1:
                    queue += [(i-1, j+1)]
            if i<len(list[j])-2:
                if j>=1:
                    queue += [(i+1, j-1)]
                queue += [(i+1, j)]
                if j<len(list)-1:
                    queue += [(i+1, j+1)]
            if j >= 1:
                queue += [(i, j - 1)]
            if j < len(list)-1:
                queue += [(i, j + 1)]





def draw_flag(x,y):
    canvas.create_polygon(58+x*20,50+y*20,67+x*20,55+y*20,58+x*20,60+y*20,fill = 'red')
    canvas.create_line(58+x*20,50+y*20,58+x*20,65+y*20)
    canvas.create_arc(52+x*20,65+y*20,68+x*20,75+y*20,start = 0,extent = 180,fill = 'black',style = CHORD)
def draw_mine(x,y):
    canvas.create_oval(50+x*20,50+y*20,70+x*20,70+y*20,fill = 'black',tag = 'sqwer')
def create_field():
    global square
    square = canvas.create_rectangle(50, 50, 450, 450, fill='#d1cdcd', tag='field')
    ifield = 20
    jfield = 20
    for i in range(21):
        canvas.create_line(50, 50 + i * 20, 450, 50 + i * 20, width = 1)
        canvas.create_line(50 + i * 20, 50, 50 + i * 20, 450,width = 1)
    canvas.create_rectangle(10, 10, 10+xreset, 10+yreset, fill='#d1cdcd',tag = 'New',outline = '#d1cdcd')
    canvas.update()
def but1(event):
    global xreset,yreset,square
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    #draw_mine(x,y)
    field_open(x,y)


    canvas.update()
def clear(event):
    canvas.create_rectangle(10, 10, 10+xreset, 10+yreset, fill='#d1cdcd',tag = 'New',outline = '#d1cdcd')
    #canvas.create()
    canvas.delete('field')
    canvas.delete('New')
    create_field()
def but3(event):
    global list
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    #canvas.create_rectangle(50+x*20,50+y*20,70+x*20,70+y*20,fill = 'blue',tag = 'sqwer')
    draw_flag(x,y)
    list[y][x] = list[y][x] + 20
    print(list[y][x])
    canvas.update()
create_field()
dfs()
canvas.tag_bind('field','<Button-1>',but1)
canvas.tag_bind('New','<Button-1>',clear)
canvas.tag_bind('field','<Button-3>',but3)
root.mainloop()

