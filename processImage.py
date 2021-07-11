import numpy
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
 
    img = cv2.resize(img, (400,300), interpolation = cv2.INTER_AREA)
    return img
