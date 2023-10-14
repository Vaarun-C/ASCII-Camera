import cv2 as cv
import math
import os
import sys
#library keyboard please import
import keyboard


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
                    #print(pixel_map[map_color_value(column)], end="")
                    print(f"\x1b[38;2;{r};{g};{b}m{pixel_hash[column]}\x1b[0m", end='')

                print()

            sys.stdout.write(f"\033[{0};{0}H")
            sys.stdout.flush()
            #releasing capture when keyboard click event for b
            if keyboard.read_key()=="b":
                cap.release()
    #cap.pause()
                cv.destroyAllWindows()
#calling the capture function when keyboard click event for button a happens
if keyboard.read_key() == 'a':
    s()

