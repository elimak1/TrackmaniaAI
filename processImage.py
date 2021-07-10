import numpy as np
import cv2 
import pytesseract
import timeit
import time

# pytesseract install guide to windows https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def getMetaData(img, prev=0):

    #Speed and time are always in place in picture
    speedImg = img[470:540,340:460,:].copy()
    """
    finImg = img[150:200,355:445,:].copy()

    finImg = cv2.cvtColor(finImg, cv2.COLOR_BGR2GRAY)
    (thresh, finImg) = cv2.threshold(
        finImg, 100, 200, cv2.THRESH_BINARY)
    finImg = (255-finImg)

    timestr = pytesseract.image_to_string(finImg, lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789')
    finish = False
    # Time appears in game when goal is reached
    if(len(timestr)>5):
        finish=True
    """
    finish = False

    speedImg = cv2.cvtColor(speedImg, cv2.COLOR_BGR2GRAY)
    (thresh, speedImg) = cv2.threshold(
        speedImg, 100, 200, cv2.THRESH_BINARY)
    speedImg = (255-speedImg)

    s = timeit.default_timer()
    speedstr = pytesseract.image_to_string(speedImg, lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789')
    
    print(timeit.default_timer()-s)
    cv2.imshow("ds",speedImg)
    cv2.waitKey(5430)
    cv2.destroyAllWindows()
    # should have length of 3, sometimes string has some extra chars
    speedstr = speedstr[:3]
    
    try:
        speed = int(speedstr)
    except ValueError:
        speed = prev

    return speed, None, finish

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

im = processImage()
getMetaData(im)
