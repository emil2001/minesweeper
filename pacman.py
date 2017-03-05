from tkinter import *
import time
import copy
#YEA
root = Tk()
canv = Canvas(root, width=0, height=0)
canv.pack()
x, y = 150, 150
vxp, vyp = 1, 0
vxg,vyg = 0,0
grid = 30
nvxp, nvyp = 0,0
matr = []
i,j = 0,0
xfield,yfield = 1000,1000
pos_matrix = []
pr,pd,pl,pu = 0,0,0,0
go = False


def shortest_route_count():
    global pos_matrix,xp,yp,xg,yg
    i,j = return_pos_ghost(xg,yg)
    ip, jp = return_pos_pac(xp, yp,pos_matrix)
    queue = [(i,j)]
    pos_matrix[i][j] =0
    while len(queue)>0 and (i != ip or j != jp):
        i,j = queue.pop(0)
        if i-1 >=0 and pos_matrix[i-1][j] == -2:
            pos_matrix[i-1][j] = int(pos_matrix[i][j])+1
            queue+=[(i-1,j)]
        if i+1<len(pos_matrix) and pos_matrix[i + 1][j] == -2:
            pos_matrix[i + 1][j] = int(pos_matrix[i][j]) + 1
            queue += [(i+1, j)]
        if j-1 >= 0 and pos_matrix[i][j-1] == -2:
            pos_matrix[i][j-1] = int(pos_matrix[i][j]) + 1
            queue += [(i, j - 1)]
        if j+1 <len(pos_matrix[i]) and pos_matrix[i][j+1] == -2:
            pos_matrix[i][j+1] = int(pos_matrix[i][j]) + 1
            queue += [(i, j + 1)]

def router():
    global xp,yp,xg,yg,pos_matrix,pos_matrix1
    pos_matrix = copy.deepcopy(pos_matrix1)

    shortest_route_count()
    ip,jp = return_pos_pac(xp,yp,pos_matrix)
    ig,jg = return_pos_ghost(xg,yg)
    path = [(ip,jp)]
    while path[0] != (ig,jg):
        x1,y1 = path[0]
        if y1-1 >= 0 and int(pos_matrix[x1][y1-1])+1 == int(pos_matrix[x1][y1]):
            path = [(x1,y1-1)] +path
        elif y1+1 <len(pos_matrix[x1]) and int(pos_matrix[x1][y1 + 1]) + 1 == int(pos_matrix[x1][y1]):
            path = [(x1, y1 + 1)] + path
        elif x1-1 >= 0 and int(pos_matrix[x1-1][y1]) + 1 == int(pos_matrix[x1][y1]):
            path = [(x1-1, y1 )] + path
        elif x1+1<len(pos_matrix) and int(pos_matrix[x1+1][y1]) + 1 == int(pos_matrix[x1][y1]):
            path = [(x1+1, y1)] + path

    return path



def field_read():
    global x,y,grid,xp,yp,matr,i,j,pos_matrix,xfield,yfield,canv
    a = open('field.txt', 'r')
    f = True
    for line in a:
        for symb in line:
            if symb == '\n':
                continue
            if f:
                matr.append([symb])
            else:
                matr[i].append(symb)
            i += 1

        f = False
        i = 0
        j += 1
    j = 0
    i = 0
    yfield = len(matr[0])*grid
    xfield = (len(matr))*grid
    canv = Canvas(root, width=xfield, height=yfield)
    canv.pack()
    pos_matrix = copy.deepcopy(matr)
    canv.update()
    a.close()

def field_draw():
    global pos_matrix,xp,yp,i,j,grid,xg,yg,pos_matrix1
    for x in pos_matrix:
        for symb in x:
            if symb == '1':
                canv.create_rectangle(i * grid, j * grid, (i + 1) * grid, (j + 1) * grid, fill="blue", tag='solid')
                pos_matrix[i][j] = -1
            if symb == '0':
                pos_matrix[i][j] = -2
            if symb == '9':
                pos_matrix[i][j] = -2
                xp = i * grid
                yp = j * grid
                draw_pac(xp,yp)
            if symb == '4':
                pos_matrix[i][j] = -2
                xg = i*grid
                yg = j*grid
                draw_ghost('green',xg,yg)
            j += 1
        j = 0
        i+=1
    pos_matrix1 = copy.deepcopy(pos_matrix)



def return_pos_ghost(xg,yg):
    ig = (xg + 15) // grid
    jg = (yg + 15) // grid
    return ig, jg


def return_pos_pac(xp, yp,pos_matrix):
    ip = (xp+15)//grid
    jp = (yp + 15) // grid
    if ip >= len(pos_matrix):
        ip = 0
    if jp >= len(pos_matrix[0]):
        jp =0
    return ip,jp

def if_game_over():
    global xg, yg, xp, yp
    if xp-5<=xg<=xp+5 and yp-5<=yg<=yp+5:
        return 1
    else:
        return 0


def game_over():
    global xfield,yfield
    canv.delete('all')
    canv.create_text(xfield//2, yfield//2, text="GAME OVER",
                font="Verdana 40", justify=CENTER, fill="red")
    canv.update()

def draw_field(xfield,yfield):
    canv.create_rectangle(0, 0, xfield, yfield, fill="white", outline="black")


def draw_pac(xp,yp):
    canv.delete('pacman')
    canv.create_oval(xp, yp, xp + 30, yp + 30, fill='yellow', tag='pacman')


def draw_ghost(color,xg,yg):
    canv.delete('ghost')
    canv.create_arc([xg, yg], [xg + 30, yg + 30], start=0, extent=180,
                    style=CHORD,fill =color , outline=color, width=2, tag='ghost')
    canv.create_rectangle(xg, yg+15, xg+30, yg+20, fill=color, outline=color, tag='ghost')
    canv.create_polygon([xg, yg+20], [xg+10, yg+20], [xg+5, yg+30], fill=color, tag='ghost')
    canv.create_polygon([xg+10, yg + 20], [xg + 20, yg + 20], [xg + 15, yg + 30], fill=color, tag='ghost')
    canv.create_polygon([xg+20, yg + 20], [xg + 31, yg + 20], [xg + 25, yg + 30], fill=color, tag='ghost')
    eyebx = xg+5
    eyeby = yg+5
    canv.create_oval([eyebx-1, eyeby], [eyebx+9, eyeby+10], fill="white", tag='ghost')
    canv.create_oval([eyebx+11, eyeby], [eyebx + 21, eyeby + 10], fill="white", tag='ghost')




def draw():
    global x, y,xp,yp,xg,yg
    draw_pac(xp,yp)
    draw_ghost('green',xg,yg)
    canv.update()


def moveleft(event):
    global nvxp, nvyp,pl
    pl = 1
    if if_cant_left(xp, yp, -1):
        return
    nvxp = -1
    nvyp = 0


def moveright(event):
    global nvxp, nvyp,pr
    pr = 1
    if if_cant_right(xp, yp, 1):
        return
    nvxp = 1
    nvyp = 0


def moveup(event):
    global nvxp, nvyp,pu
    pu = 1
    if if_cant_up(xp, yp, -1):
        return
    nvyp = -1
    nvxp = 0


def movedown(event):
    global nvxp,nvyp,pd
    pd = 1
    if if_cant_down(xp, yp, 1):
        return
    nvyp = 1
    nvxp = 0

def moveghost():
    global xp,yp,xg,yg,vxg,vyg,go
    path = router()
    if len(path) ==1 :
        game_over()
        go = True
    elif (xg+15-grid//2)%grid == 0 and (yg+15-grid//2)%grid == 0:
        i1,j1 = path[1]
        ig,jg = return_pos_ghost(xg,yg)
        if ig+1 == i1:
            vxg=1
            vyg = 0
        elif ig-1 == i1:
            vxg =-1
            vyg = 0
        elif jg +1 == j1:
            vyg =1
            vxg = 0
        elif jg-1 == j1:
            vyg=-1
            vxg = 0
    xg+=vxg
    yg+=vyg


def if_cant_right(xp, yp, nvxp):
    ip, jp = return_pos_pac(xp, yp,pos_matrix)
    return ip+1 < len(matr) and matr[ip+1][jp] == '1'


def if_cant_left(xp, yp, nvxp):
    ip, jp = return_pos_pac(xp, yp,pos_matrix)
    return ip>=1 and matr[ip-1][jp] == '1'


def if_cant_up(xp, yp, nvyp):
    ip, jp = return_pos_pac(xp, yp,pos_matrix)
    return jp>=1 and matr[ip][jp-1] == '1'


def if_cant_down(xp, yp, nvyp):
    ip, jp = return_pos_pac(xp, yp,pos_matrix)
    return jp+1 < len(matr[jp]) and matr[ip][jp+1]=='1'


def move_pacman():
    global xp, yp, vxp, vyp, i, j, matr, grid, nvxp, nvyp,xfield,yfield,pl,pr,pd,pu,ip,jp
    if yp - 15 < 0:
        yp += yfield
    if yp + 15 > yfield:
        yp -= (yfield)
    if xp - 15 < 0:
        xp += xfield
    if xp + 15 > xfield:
        xp -= (xfield)
    ip,jp = return_pos_pac(xp,yp,pos_matrix)
    if (xp+15-grid//2)%grid == 0 and (yp+15-grid//2)%grid == 0:
        if if_cant_right(xp, yp, nvxp) and nvxp == 1:
            nvxp = 0
        elif pr and not(if_cant_right(xp, yp, nvxp)):
            nvxp = 1
            nvyp = 0
            pr = 0
        if if_cant_left(xp, yp, nvxp) and nvxp == -1:
            nvxp = 0
        elif pl and not(if_cant_left(xp, yp, nvxp)):
            nvxp = -1
            nvyp = 0
            pl = 0
        if if_cant_up(xp, yp, nvyp) and nvyp == -1:
            nvyp = 0
        elif pu and not(if_cant_up(xp, yp, nvyp)):
            nvyp = -1
            nvxp = 0
            pu = 0
        if if_cant_down(xp, yp, nvyp) and nvyp == 1:
            nvyp = 0
        elif pd and not(if_cant_down(xp, yp, nvyp)):
            nvyp = 1
            nvxp = 0
            pd = 0
        vxp = nvxp
        vyp = nvyp


    xp += vxp
    yp += vyp

field_read()
field_draw()
root.bind('<a>', moveleft)
root.bind('<d>', moveright)
root.bind('<w>', moveup)
root.bind('<s>', movedown)
draw()
while 1:
    move_pacman()
    moveghost()
    if go:
        break
    draw()
    time.sleep(.01)

root.mainloop()