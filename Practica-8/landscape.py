from tkinter import *
import math
import random

def ecFlower(w,x,y,l,a,sl,da,n):
    if n==0:
        return

    if n>5:
        color='gold'
    elif n>2:
        color='green3'
    elif n>0:
        color='purple2'

    x2=x+l
    y2=y
    ar=math.radians(a)

    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno

    x2=xrot + x
    y2=yrot + y

    w.create_line(x,y,x2,y2,fill=color)

    ecFlower(w,x2,y2,l*sl,a-2*da,sl,da,n-1)
    ecFlower(w,x2,y2,l*sl,a+0.5*da,sl,da,n-1)
    ecFlower(w,x2,y2,l*sl,a,sl,da,n-1)
    ecFlower(w,(x+x2)/2,(y+y2)/2,l*sl,a-da,sl*.8,da,n-1)
    ecFlower(w,(x+x2)/2,(y+y2)/2,l*sl,a+da,sl*.8,da,n-1)
    
    return

def ecGrass(w,x,y,l,a,sl,da,n):
    if n==0:
        return

    if n>5:
        color='SpringGreen4'
    elif n>2:
        color='dark green'
    elif n>0:
        color='green4'

    x2=x+l
    y2=y
    ar=math.radians(a)

    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno

    x2=xrot + x
    y2=yrot + y

    w.create_line(x,y,x2,y2,fill=color)

    ecGrass(w,x2,y2,l*sl,a,sl,da,n-1)
    ecGrass(w,x2,y2,l*sl,a+2*da,sl,da,n-1)
    ecGrass(w,(x+x2)/2,(y+y2)/2,l*sl,a+3*da,sl,da,n-1)
    ecGrass(w,(x+x2)/2,(y+y2)/2,l*sl,a+3*da,sl,da,n-1)

    return

def ecRiver(w,x,y,l,a,sl,da,n):
    if n==0:
        return

    if n>5:
        color='RoyalBlue2'
    elif n>2:
        color='DodgerBlue3'
    elif n>0:
        color='SteelBlue2'

    
    x2=x+l
    y2=y
    ar=math.radians(a)

    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno

    x2=xrot + x
    y2=yrot + y

    w.create_line(x,y,x2,y2,fill=color)

    ecRiver(w,x2,y2,l*sl,a,sl,da,n-1)
    ecRiver(w,x2,y2,l*sl,a+da,sl,da,n-1)
    ecRiver(w,x2,y2,l*sl,a-2*da,sl,da,n-1)

    return

def ecTree(w,x,y,l,a,sl,da,n):
    if n==0:
        return

    if n>5:
        color='saddle brown'
    elif n>2:
        color='SpringGreen4'
    elif n>0:
        color='SpringGreen2'

    x2=x+l
    y2=y
    ar=math.radians(a)

    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno

    x2=xrot + x
    y2=yrot + y

    w.create_line(x,y,x2,y2,fill=color)

    ecTree(w,x2,y2,l*sl,a-2*da,sl,da,n-1)
    ecTree(w,x2,y2,l*sl,a+da,sl,da,n-1)
    ecTree(w,x2,y2,l*sl,a,sl,da,n-1)
    ecTree(w,(x+x2)/2,(y+y2)/2,l*sl,a-da,sl*.8,da,n-1)
    ecTree(w,(x+x2)/2,(y+y2)/2,l*sl,a+da,sl*.8,da,n-1)

    return


def ecSakuraTree(w,x,y,l,a,sl,da,n):
    if n==0:
        return

    if n>5:
        color='brown'
    elif n>2:
        color='pink'
    elif n>0:
        color='white'

    x2=x+l
    y2=y
    ar=math.radians(a)

    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno

    x2=xrot + x
    y2=yrot + y

    w.create_line(x,y,x2,y2,fill=color)

    ecSakuraTree(w,x2,y2,l*sl,a-2*da,sl,da,n-1)
    ecSakuraTree(w,x2,y2,l*sl,a+da,sl,da,n-1)
    ecSakuraTree(w,x2,y2,l*sl,a,sl,da,n-1)
    ecSakuraTree(w,(x+x2)/2,(y+y2)/2,l*sl,a-da,sl*.8,da,n-1)
    ecSakuraTree(w,(x+x2)/2,(y+y2)/2,l*sl,a+da,sl*.8,da,n-1)

    return


def ecCloud(w,x,y,l,a,sl,da,n):
    if n==0:
        return

    color='white'

    x2=x+l
    y2=y
    ar=math.radians(a)

    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno

    x2=xrot + x
    y2=yrot + y

    w.create_line(x,y,x2,y2,fill=color)

    w.create_oval((x-l/2),(y-l/2),(x+l/2),(y+l/2),fill='white',outline='gray77') 
    ecCloud(w,x2,y2,l*sl,a-da,sl,da,n-1)
    ecCloud(w,x2,y2,l*sl,a-2*da,sl,da,n-1)
    ecCloud(w,x2,y2,l*sl,a-3*da,sl,da,n-1)

    return

def ecMountain(w,x,y,l,a,sl,da,n):
    if n==0:
        return

    color='saddle brown'

    x2=x+l
    y2=y
    ar=math.radians(a)

    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno

    x2=xrot + x
    y2=yrot + y

    w.create_line(x,y,x2,y2,fill=color)

    if(y>280):return
    ecMountain(w,x2,y2,l*sl,a-da,sl,da,n-1)
    ecMountain(w,x2,y2,l*sl,a-1.5*da,sl,da,n-1)
    ecMountain(w,x2,y2,l*sl,a-2.5*da,sl,da,n-1)
    #ecMountain(w,x2,y2,l*sl,a-3*da,sl,da,n-1)

    return

if __name__ == '__main__':

    master = Tk()

    xmax=500
    ymax=500

    w = Canvas(master, width=xmax, height=ymax)
    w.pack()

    ## Draw a mountain
    ecMountain(w,150,280,150,120,0.8,20,24)

    ## Draw some clouds
    ecCloud(w,10,50,50,120,0.8,35,6)
    ecCloud(w,60,50,50,120,0.8,25,6)
    ecCloud(w,100,50,50,120,0.8,30,6)
    ecCloud(w,150,50,50,120,0.8,30,6)
    ecCloud(w,200,50,50,120,0.8,35,7)
    ecCloud(w,200,50,60,120,0.8,40,7)
    ecCloud(w,300,50,60,120,0.8,30,7)
    ecCloud(w,350,55,65,120,0.8,35,5)
    ecCloud(w,400,50,65,120,0.8,30,6)
    ecCloud(w,450,50,70,120,0.8,40,6)
    ecCloud(w,400,50,55,120,0.8,35,6)

    ## Put some trees
    ecTree(w,50,420,50,186,0.6,20,8)
    ecTree(w,60,417,60,177,0.7,30,7)
    ecTree(w,70,420,30,180,0.6,35,8)
    ecTree(w,80,414,40,182,0.6,25,7)
    ecTree(w,90,421,35,179,0.7,20,9)
    ecTree(w,100,418,55,176,0.6,30,7)

    ## Put some sakura trees
    ecSakuraTree(w,150,425,110,181,0.5,30,8)
    ecSakuraTree(w,175,410,30,177,0.6,20,8)
    ecSakuraTree(w,200,422,90,177,0.6,20,8)
    ecSakuraTree(w,225,410,70,177,0.6,20,8)
    ecSakuraTree(w,250,415,40,184,0.7,20,8)
    ecSakuraTree(w,275,410,56,177,0.6,35,9)
    ecSakuraTree(w,300,420,54,179,0.6,30,8)

    ## Draw some grass
    i = 1
    while i < 500:
        i += 2
        j = random.randint(1,100)
        ecGrass(w,i,400+j,10,50,0.6,10,3)
        j = random.randint(1,100)
        ecGrass(w,i,400+j,10,50,0.6,10,3)
        j = random.randint(1,100)
        ecGrass(w,i,400+j,10,50,0.6,10,3)
        j = random.randint(1,100)
        ecGrass(w,i,400+j,10,50,0.6,10,3)
        j = random.randint(1,100)
        ecGrass(w,i,400+j,10,50,0.6,10,3)
        j = random.randint(1,100)
        ecGrass(w,i,400+j,10,50,0.6,10,3)
    
    ## Draw some flowers
    i = 1
    while i < 500:
        i += random.randint(5,20)
        j = random.randint(1,100)
        ecFlower(w,i,400+j,10,50,0.6,10,3)
        j = random.randint(1,100)
        ecFlower(w,i,400+j,10,50,0.6,10,3)
        j = random.randint(1,100)
     
    mainloop()