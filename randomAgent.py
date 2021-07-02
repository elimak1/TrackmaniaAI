import random
import time
import cv2

# import pydirectinput
import keyboard

from matplotlib.pyplot import imshow

from captureWindow import captureWindow
# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start
keyboard.wait('B')
time.sleep(sleepy)


def relase_all():
    keyboard.release("w")
    keyboard.release("a")
    keyboard.release("d")
    keyboard.release("s")


# Randomly pick action then sleep.
# 0 w
# 1 a
# 2 d
# 3 s

for i in range(10):
    xd = captureWindow()
    print(xd.shape)
    action = random.randint(0,3)
    if action == 0:
        keyboard.press("w")
    elif action == 1:
        keyboard.press("a")
    elif action == 2:
        keyboard.press("d")
    elif action == 3:
        keyboard.press("s")
    time.sleep(sleepy)
    # relase_all()bwsdwasdwsd
cv2.imshow("Fall", xd)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
print("DONE")
