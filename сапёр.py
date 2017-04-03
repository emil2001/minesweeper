from tkinter import*
import random
import time
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
k = 50
x = random.randint(0, m - 1)
y = random.randint(0, n - 1)
list[y][x] = 100
queue = [(x, y)]



def game_over():
    global list
    for j in range(len(list)):
        for i in range(len(list[j])):
            if_mine = list[j][i]
            if if_mine // 100 == 1:
                draw_mine(i, j)


def dfs(i,j):
    global queue, ifield, jfield, list
    if list[j][i]//100 == 1 and (list[j][i]//10)%10 !=2:
        game_over()
        return 0
    elif (list[j][i] // 10) % 10 == 0 and list[j][i] % 10 == 0 and list[j][i] // 100 == 0:
        open(i,j)
    elif list[j][i] % 10 != 0 and (list[j][i] // 10) % 10 == 0 and list[j][i]//100 == 0:
        canvas.create_rectangle(50 + i * 20, 50 + j * 20, 50 + (i + 1) * 20, 50 + (j + 1) * 20, fill='red')
        canvas.create_text(60 + i * 20, 60 + j * 20, text=list[j][i] % 10)
        time.sleep(0.05)
        canvas.update()
        list[j][i] = list[j][i] // 100 + 10 + list[j][i] % 10


def open(i,j):
    global queue, ifield, jfield, list

    canvas.create_rectangle(50 + i * 20, 50 + j * 20, 50 + (i + 1) * 20, 50 + (j + 1) * 20, fill='red')
    time.sleep(0.05)
    canvas.update()
    list[j][i] = list[j][i] // 100 + 10 + list[j][i] % 10
    if i >= 1:
        if j >= 1:
            dfs(i - 1, j - 1)
        dfs(i - 1, j)
        if j < len(list) - 2:
            dfs(i - 1, j + 1)
    if i < len(list[j]) - 2:
        if j >= 1:
            dfs(i + 1, j - 1)
        dfs(i + 1, j)
        if j < len(list) - 2:
            dfs(i + 1, j + 1)
    if j >= 1:
        dfs(i, j - 1)
    if j < len(list) - 2:
        dfs(i, j + 1)



def counter():
    global queue,ifield,jfield,list
    list = [[000] * (m + 1) for i in range(n + 1)]
    for i in range(k):
        x = random.randint(1, m - 2)
        y = random.randint(1, n - 2)
        list[y][x] = 100
        queue += [(x, y)]
    for i in range(0,ifield):
        for j in range(0,jfield):
            x1 = i
            y1 = j
            mine_count = (list[y1 - 1][x1 - 1] + list[y1][x1 - 1] + list[y1 + 1][x1 - 1] + list[y1 + 1][x1] + list[y1 - 1][x1] +
                          list[y1 - 1][x1 + 1] + list[y1][x1 + 1] + list[y1 + 1][x1 + 1]) // 100
            if_mine = list[y1][x1]
            list[y1][x1] = if_mine + mine_count

def bfs(x,y):
    global list
    queue = [(x,y)]
    if list[y][x]//100 == 1:
        game_over()
        return 0
    while len(queue) >0:
        i,j = queue.pop(0)
        if list[j][i]%10 != 0 and (list[j][i] // 10) % 10 == 0 :
            canvas.create_rectangle(50 + i * 20, 50 + j * 20, 50 + (i + 1) * 20, 50 + (j + 1) * 20, fill='red')
            canvas.create_text(60+i*20,60+j*20,text = list[j][i]%10)
            time.sleep(0.05)
            canvas.update()
            list[j][i] = list[j][i] // 100 + 10 + list[j][i] % 10
        if (list[j][i] // 10) % 10 == 0 and list[j][i]%10 ==0 and list[j][i]//100 == 0:
            canvas.create_rectangle(50+i*20,50+j*20,50+(i+1)*20,50+(j+1)*20, fill = 'red')
            time.sleep(0.05)
            canvas.update()
            list[j][i] = list[j][i]//100 + 10 + list[j][i]%10
            if i>=1:
                if j>=1:
                    queue += [(i-1,j-1)]
                queue += [(i-1, j)]
                if j<len(list)-2:
                    queue += [(i-1, j+1)]
            if i<len(list[j])-2:
                if j>=1:
                    queue += [(i+1, j-1)]
                queue += [(i+1, j)]
                if j<len(list)-2:
                    queue += [(i+1, j+1)]
            if j >= 1:
                queue += [(i, j - 1)]
            if j < len(list)-2:
                queue += [(i, j + 1)]





def draw_flag(x,y):
    canvas.create_polygon(58+x*20,50+y*20,67+x*20,55+y*20,58+x*20,60+y*20,fill = 'red',tag = [x,y])
    canvas.create_line(58+x*20,50+y*20,58+x*20,65+y*20,tag = [x,y])
    canvas.create_arc(52+x*20,65+y*20,68+x*20,75+y*20,start = 0,extent = 180,fill = 'black',style = CHORD, tag = [x,y])
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
    dfs(x,y)


    canvas.update()
def clear(event):
    canvas.create_rectangle(10, 10, 10+xreset, 10+yreset, fill='#d1cdcd',tag = 'New',outline = '#d1cdcd')
    canvas.delete('field')
    canvas.delete('New')
    create_field()
    counter()
def but3(event):
    global list
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    if list[y][x]//10%10 == 2:
        canvas.delete([x,y])
        canvas.update()
        list[y][x] = list[y][x] - 20
    elif list[y][x]//10%10 == 0:
        draw_flag(x, y)
        list[y][x] = list[y][x] + 20
    print(list[y][x])
    canvas.update()
create_field()
counter()
canvas.tag_bind('field','<Button-1>',but1)
canvas.tag_bind('New','<Button-1>',clear)
canvas.tag_bind('field','<Button-3>',but3)
root.mainloop()

