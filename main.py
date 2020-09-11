#main.py
import os
import time
from kbhit import KBHit
import random

#   ╔═══╗
#   ║═══║
#   ╚═══╝

# bodypart types
bodypart = ["║ ", "══", "╔═","╗ ", "╚═", "╝ "]
#bodypart = ["██", "██", "██","██", "██", "██"]
def sublist(list1,list2):
    if len(list1) == len(list2):
        newlist = []
        for i in range(len(list1)):
            newlist.append(list1[i]- list2[i])

        return  newlist

    raise "Not the same length"



class window():
    def __init__(self,winsize):
        self.winsize=tuple(winsize)
        self.buffer = None
        self.clearbuffer("  ")
        self.clear = "clear"
        if os.name=="nt":
            self.clear="cls"

    def drawscreen(self):
        #clear terminal then draw screen
        os.system(self.clear)

        for i in range(self.winsize[1]):
            print("".join(self.buffer[i]))


    def setpixel(self,pos ,chararcter):
        self.buffer[pos[1]][pos[0]] = chararcter


    def setpixels(self,pos1,pos2,chararcter):

        if pos1[0] == pos2[0]:
            for y in range(pos1[1],pos2[1]+1):
                self.setpixel((pos1[0],y), chararcter)
        elif pos1[1]==pos2[1]:

            for x in range(pos1[0],pos2[0]+1):
                self.setpixel((x,pos1[1]), chararcter)
        else:
            for y in range(pos1[1],pos2[1]+1):
                for x in range(pos1[0],pos2[0]+1):
                    self.setpixel((x,y), chararcter)


    def clearbuffer(self, chararcter="  "):
        self.buffer = [[chararcter for _ in range(self.winsize[0])] for _ in range(self.winsize[1])]


def drawborders(wind):

    wind.setpixel((0,0), "╔═")
    wind.setpixels((1,0), (wind.winsize[0]-2,0), "══")
    wind.setpixel((wind.winsize[0]-1,0), "╗ ")

    wind.setpixel((0,wind.winsize[1]-1), "╚═")
    wind.setpixels((1,wind.winsize[1]-1), (wind.winsize[0]-2,wind.winsize[1]-1), "══")
    wind.setpixel((wind.winsize[0]-1,wind.winsize[1]-1), "╝ ")

    wind.setpixels((0,1), (0,wind.winsize[1]-2), "║ ")
    wind.setpixels((wind.winsize[0]-1,1), (wind.winsize[0]-1,wind.winsize[1]-2), "║ ")

def drawpart(wind, pos, type):
    wind.setpixel(pos, bodypart[type])


def drawsnake(wind, body):
    calpos = sublist(body[0],body[1])
    if calpos[0]!=0:
        drawpart(wind, body[0], 1)
    elif calpos[1]!=0:
        drawpart(wind, body[0], 0)

    for i in range(1, len(body[:-1])):

        low = sublist(body[i-1],body[i])
        high = sublist(body[i],body[i+1])

        up = False
        down = False
        left = False
        right = False
        if low[0]==-1:
            left=True
        elif low[0]==1:
            right=True
        elif low[1]==-1:
            up=True
        elif low[1]==1:
            down=True

        if high[0]==1:
            left=True
        elif high[0]==-1:
            right=True
        elif high[1]==1:
            up=True
        elif high[1]==-1:
            down=True

        if up and left:
            drawpart(wind,body[i], 5)
        elif up and right:
            drawpart(wind,body[i], 4)
        elif down and left:
            drawpart(wind,body[i], 3)
        elif down and right:
            drawpart(wind,body[i], 2)
        elif up and down:
            drawpart(wind,body[i], 0)
        elif left and right:
            drawpart(wind,body[i], 1)

    calpos = sublist(body[-2],body[-1])
    if calpos[0]!=0:
        drawpart(wind,body[-1], 1)
    else:
        drawpart(wind,body[-1], 0)

def drawapple(wind,applepos):
    wind.setpixel(applepos, "* ")

def movelist(list, head):
    newlist = [head]

    for i in list[:-1]:
        newlist.append(i)
    return newlist

def randompos(wind):
    x = random.randint(2, wind.winsize[0]-2)
    y = random.randint(2, wind.winsize[1]-2)
    return [x, y]

def calculatedelay(bodylen):
    de = -0.05 * bodylen**.5 + 0.6
    return max(de, 0.15)
    return 0

delay = calculatedelay(2)
mainwin = window((25,25))   # 25,25

applepos = randompos(mainwin)
snakebod = [randompos(mainwin)]
snakebod.append(snakebod[0])




mainwin.clearbuffer("  ")
drawborders(mainwin)
drawsnake(mainwin, snakebod)
mainwin.drawscreen()





kb = KBHit()

dir = [0, 0]

dtime = time.time()
while True:
    fdir = [0, 0]
    if kb.kbhit():  # keyboard
        c = kb.getch()
        if ord(c) == 27: # ESC
            break

        if ord(c) == 119: #W
            fdir = [0,-1]
        elif ord(c) == 97: #A
            fdir = [-1,0]
        elif ord(c) == 115: #S
            fdir = [0,1]
        elif ord(c) == 100: #D
            fdir = [1,0]

        if fdir != [0, 0]:
            if [snakebod[0][0] + fdir[0],snakebod[0][1]+ fdir[1]] not in snakebod:
                dir = list(fdir)




    if time.time()-dtime > delay and dir != [0,0]:
        dtime = time.time()
        head = [snakebod[0][0] + dir[0],snakebod[0][1] + dir[1]]
        snakebod = movelist(snakebod, head)

        if mainwin.buffer[snakebod[0][1]][snakebod[0][0]] == "* ":
            applepos= randompos(mainwin)
            snakebod.append(snakebod[-1])
            delay = calculatedelay(len(snakebod))
        elif mainwin.buffer[snakebod[0][1]][snakebod[0][0]] != "  ":
            break

        mainwin.clearbuffer("  ")
        drawborders(mainwin)
        drawapple(mainwin, applepos)
        drawsnake(mainwin, snakebod)
        mainwin.drawscreen()

kb.set_normal_term()
print("You Lost Haha")
print("Youre score = {0}".format(len(snakebod)))
