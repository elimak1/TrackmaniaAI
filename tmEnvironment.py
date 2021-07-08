import gym
from gym.spaces import Discrete, Dict, MultiBinary, Box
import numpy as np
import os
import keyboard
import time
import timeit
import cv2
from captureWindow import captureWindow
from processImage import getMetaData, processImage

TOPSPEED = 1000
MAXHUNDREDS = 1000 #10 seconds
SLEEPY = 0.033

class tmEnv(gym.Env):
    def __init__(self):
        self.action_space = MultiBinary(4)
        self.observation_space = Dict({"speed":Discrete(TOPSPEED), "time":Discrete(MAXHUNDREDS), "pic":Box(0,256,shape=(600,800,3),dtype=int)})
        self.limit = 0
        self.start = timeit.default_timer()
        self.speed = 0

        
    def step(self,action):
        self.release_all()
        if(action[0]):
            keyboard.press("w")
        if(action[1]):
            keyboard.press("a")
        if(action[2]):
            keyboard.press("d")
        if(action[3]):
            keyboard.press("s")
        
        self.limit+=1
        
        
        img = captureWindow()
        img = processImage(img)
        
        

        # this for testing
        # img = processImage()

        start = timeit.default_timer()
        speed, hundreds = getMetaData(img, self.speed)
        self.speed = speed

        hundreds = (timeit.default_timer() - self.start)*100

        stop = timeit.default_timer()
        #print(stop-start)
        t = SLEEPY+stop-start
        if(t<0):
            t=0
        time.sleep(t)
        # Calculate reward
        reward = speed/TOPSPEED - hundreds/1000

        # Episode end
        done = False
        # limit to stop for testint purposes
        if(hundreds>MAXHUNDREDS or self.limit>50):
            done = True
            self.release_all()
        # also if finished
        info = {}
        return dict({"speed":speed, "time":hundreds, "pic":img}), reward,done,info

        

    def render(self):
        pass

    def reset(self):
        self.limit=0
        # restart race
        keyboard.press("l")
        keyboard.release("l")
        # wait for countdown timer
        time.sleep(2)
        self.start = timeit.default_timer()

    def release_all(self):
        keyboard.release("w")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("s")

