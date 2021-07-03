import random
import time
import cv2

# import pydirectinput
import keyboard

from matplotlib.pyplot import imshow

from captureWindow import captureWindow
from tmEnvironment import tmEnv


def test_run():
    # Wait for me to push B to start
    keyboard.wait('B')
    done = False
    score = 0
    env = tmEnv()
    env.reset()
    while not done:
        action=env.action_space.sample()
        state,reward,done,info = env.step(action)
        score+=reward
    print("SCORE:", score)
    cv2.imshow("Fall", state[0])
    cv2.waitKey(0) # waits until a key is pressed
    cv2.destroyAllWindows() # destroys the window showing image
    print("DONE")

test_run()

