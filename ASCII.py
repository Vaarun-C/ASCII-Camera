import cv2 as cv
import math
import os
import sys
#library keyboard please import
import keyboard
import numpy as np

#library for ss
import pyautogui
#library for image
#from PIL import Image,text_to_image
#from Screenshot import Screenshot_clipping
f = open("color.txt",'w')
z = open("char.txt","w")

os.system("clear|cls")

pixel_map = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
pixel_hash = []

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 35)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 20)

def map_color_value(old_value):
    return math.floor(((old_value - 0) / (255 - 0)) * (len(pixel_map)-1 - 0) + 0)

for i in range(256):
    pixel_hash.append(pixel_map[map_color_value(i)])
#putting capture under a function because nice to work with 
    def s():
        while True :
            #print('ok')

            #if keyboard.is_pressed("a"):
            ret, image = cap.read()
            if image is None:
                break

            image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

            for i,row in enumerate(image_gray):
                for j,column in enumerate(row):
                    r,g,b = image[i][j]
                    #print(r,g,b)
                    #print(pixel_map[map_color_value(column)], end="")
                    print(f"\x1b[48;2;{r};{g};{b}m{pixel_hash[column]}\x1b[0m", end='')
                    f.writelines(f"[{r},{g},{b}],\n")
                    z.writelines(f"[{pixel_hash[column]}]\n")    

                print()


            sys.stdout.write(f"\033[{0};{0}H")
            sys.stdout.flush()
            #releasing capture when keyboard click event for b
            if keyboard.read_key()=="b":
                cap.release()
    #cap.pause()
                #cv.destroyAllWindows()
#calling the capture function when keyboard click event for button a happens
def ss():

    image = pyautogui.screenshot() 
    image = cv.cvtColor(np.array(image), cv.COLOR_BGR2RGB)
    cv.imwrite("image1.png", image) 

    
def v():
    image = cv.imread('image1.png',cv.COLOR_BGR2RGB)
    cv.imshow('pic',image)
    cv.waitKey(0)
    f = open("color.txt",'r')
    z = open("char.txt",'r')
    #data=f.readlines()
    #dat=z.readlines()
    for i in f:
        cr = i
        for j in z:
            ch =j
            print(f"\x1b[48;2;{i[0]};{i[1]};{i[2]}m{j}\x1b[0m", end='')

        
        
        
while True:
    if keyboard.read_key() == 'a':
        s()
    elif keyboard.read_key()=='s':
        ss()
    elif keyboard.read_key()=='v':
        v()








