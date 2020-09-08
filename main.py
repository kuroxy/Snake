#main.py
import os

#   ╔═ ══ ╗ 00
#   ║     ║  0
#   ╚═ ══ ╝

# bodypart types
bodypart = ["║ ", "══", "╔═","╗ ", "╚═", "╝ "]

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

    def drawscreen(self):
        #clear terminal then draw screen
        os.system("cls||clear")

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

    for pos in range(len(body[1:-1])):
        low = sublist(body[i-1],body[1])
        high = sublist(body[i],body[i+1])

        if low[0]==1 and low[1]==0: # right
            if high[0]
            drawpart()


snakebod = [[10,10],[10,11]]

mainwin = window((25,25))
drawborders(mainwin)
drawsnake(mainwin, snakebod)
mainwin.drawscreen()
