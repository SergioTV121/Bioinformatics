#Practica 4 dinamica molecular
#Tinoco Videgaray Sergio Ernesto
#Bioinformatics
#20/03/24

import cv2
import numpy as np
#from google.colab.patches import cv2_imshow
#import math
import time
from IPython import display as display

import ipywidgets as ipw
from PIL import Image
from io import BytesIO

m=1

color=(255,255,255)
maxX=500
maxY=500
x0=int(maxX/2)
y0=int(maxY/2)


def draw_circle(x,y):
  cv2.circle(img,(int(x0+x),int(y0-y)),10,color,-1)

def new_r(r,v,a):
  rx,ry=r
  vx,vy=v
  ax,ay=a

  new_rx = rx + vx*delta_t + 0.5*ax*(delta_t**2)
  new_ry = ry + vy*delta_t + 0.5*ay*(delta_t**2)
  return new_rx, new_ry

def new_v(v,a):
  vx,vy=v
  ax,ay=a

  new_vx = vx + ax*delta_t
  new_vy = vy + ay*delta_t
  return new_vx,new_vy

def new_a(f):
  fx,fy=f

  new_ax =  fx/m
  new_ay =  fy/m
  return new_ax,new_ay

def Fg():
  return 0,-9.8*m

# def Fs(a,b,d_eq,k):
#   ax,ay=a
#   bx,by=b

#   ABx,ABy=bx-ax,by-ay

#   magAB=np.sqrt(ABx**2+ABy**2)

#   nABx,nABy=ABx/magAB,ABy/magAB

#   magF=-k*(magAB-d_eq)

#   return nABx*magF,nABy*magF

# def Fc(a,b,qA,qB):
#   ax,ay=a
#   bx,by=b

#   ABx,ABy=bx-ax,by-ay

#   magAB=np.sqrt(ABx**2+ABy**2)

#   nABx,nABy=ABx/magAB,ABy/magAB

#   magF=qA*qB/(magAB**2)

#   return nABx*magF,nABy*magF

def update():
  global x1,y1,ax,ay,vx,vy

#  fx,fy=Fg()
  ax,ay=new_a((fx,fy))
  x1,y1=new_r((x1,y1),(vx,vy),(ax,ay))
  vx,vy=new_v((vx,vy),(ax,ay))

  if x1>maxX/2: x1=-maxX/2
  if y1>maxY/2: y1=-maxY/2

  return

def draw():
  draw_circle(x1,y1)

x1,y1=0,0
vx,vy=10,10
ax,ay=0,0
fx,fy=0,0
MaxIterations = 10
delta_t=.1

img = np.zeros((maxX, maxY, 3), dtype="uint8")
wIm = ipw.Image()
display.display(wIm)

for count in range(MaxIterations):
  img[:]=(0,0,0)

  update()
  draw()
  cv2.putText( img,str(count)+" f=("+str(fx)+","+str(fy)+")",(25,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
  pilIm = Image.fromarray(img, mode="RGB")
  with BytesIO() as fOut:
      pilIm.save(fOut, format="png")
      byPng = fOut.getvalue()

  # set the png bytes as the image value;
  # this updates the image in the browser.
  wIm.value=byPng
  pilIm.show()
#  time.sleep(0.001)

# Parabolic throwing
# x1,y1=-maxX/2+10,0
# vx,vy=30,40
# ax,ay=0,0
# fx,fy=0,0
# MaxIterations = 500
# delta_t=.02

# #Spring
#   fsx,fsy=Fs((x2,y2),(x1,y1),100,.5)
#   fx+=fsx;fy+=fsy
# x1,y1=0,maxY/2-110
# x2,y2=0,maxY/2-10
# vx,vy=20,0
# ax,ay=0,0
# fx,fy=0,0
# MaxIterations = 2000
# delta_t=.05

#Coulomb
#   fcx,fcy=Fc((x3,y3),(x1,y1),20,20)
#   fx+=fcx;fy+=fcy

# x3,y3=20,maxY/2-120