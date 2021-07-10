import numpy as np
import cv2 

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

