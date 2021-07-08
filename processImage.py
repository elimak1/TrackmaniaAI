from os import curdir
import numpy as np
import cv2 
import pytesseract
import timeit
import time
# pytesseract install guide to windows https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from matplotlib import image
from matplotlib import pyplot

# !TODO add checking to find out if goal is reached
def getMetaData(img, prev=0):

    #Speed and time are always in place in picture
    speedImg = img[470:540,340:460,:].copy()
    # timeImg = img[550:585,355:445,:].copy()

    """timeImg = cv2.cvtColor(timeImg, cv2.COLOR_BGR2GRAY)
    (thresh, timeImg) = cv2.threshold(
        timeImg, 150, 255, cv2.THRESH_BINARY)
    timeImg = (255-timeImg)
    timestr = pytesseract.image_to_string(timeImg, lang='eng', config='--psm 6')
    try:
        hundreds = int(timestr.split(":")[0])*60*100 + int(timestr.split(":")[1][:2])*100 + int(timestr.split(":")[1][3:5])
    except ValueError:
        hundreds = 0 """
    
    speedImg = cv2.cvtColor(speedImg, cv2.COLOR_BGR2GRAY)
    (thresh, speedImg) = cv2.threshold(
        speedImg, 100, 200, cv2.THRESH_BINARY)
    speedImg = (255-speedImg)
    s = timeit.default_timer()
    

    speedstr = pytesseract.image_to_string(speedImg, lang='eng', config='--psm 6')
    # print(timeit.default_timer()-s)
    
    # should have length of 3, sometimes string has some extra chars
    speedstr = speedstr[:3]
    # Convert common missreads to corresponding numbers
    for i in range(len(speedstr)):
        if(speedstr[i] == "o" or speedstr[i] == "O"):
            speedstr = speedstr[:i] + "0" + speedstr[i + 1:]
        if(speedstr[i] == "s" or speedstr[i] == "S"):
            speedstr = speedstr[:i] + "8" + speedstr[i + 1:]
        if(speedstr[i] == "l" or speedstr[i] == "I"):
            speedstr = speedstr[:i] + "1" + speedstr[i + 1:]

    print(speedstr)
    try:
        speed = int(speedstr)
    except ValueError:
        speed = prev
    return speed, None

def processImage(img=None):
    try:
        img.any()
    except AttributeError :
        # Load default image
        img = cv2.imread(r'trackmania-first-person.png', cv2.IMREAD_UNCHANGED)
        width = 800
        height = 600 
        dim = (width, height)
        # resize image
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
    #processed_img = cv2.Canny(img, threshold1=300, threshold2=400)
    return img
