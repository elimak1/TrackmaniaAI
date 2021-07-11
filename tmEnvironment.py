import gym
from gym.spaces import Discrete, Dict, MultiBinary, Box
import numpy as np
import os
import keyboard
import time
import timeit
import cv2
from captureWindow import captureWindow
from processImage import processImage
from getGameState import getGameState

TOPSPEED = 1000
MAXMS = 20000 #20 seconds
SLEEPY = 0.033

class tmEnv(gym.Env):
    def __init__(self):
        self.action_space = MultiBinary(4)
        # self.observation_space = Dict({"speed":Discrete(TOPSPEED), "time":Discrete(MAXMS), "pic":Box(0,256,shape=(600,800,3),dtype=int)})
        self.observation_space = Box(0,255,shape=(300,400,3),dtype=np.uint8)
        self.time = 0
        self.speed = 0
        img = captureWindow()
        self.state = processImage(img)
        self.score = 0

        
    def step(self,action):
        if(action[0]):
            keyboard.press("w")
        else:
            keyboard.release("w")
        if(action[1]):
            keyboard.press("a")
        else:
            keyboard.release("a")
        if(action[2]):
            keyboard.press("d")
        else:
            keyboard.release("d")
        if(action[3]):
            keyboard.press("s")
        else:
            keyboard.release("s")
        
        start = timeit.default_timer()
        img = captureWindow()
        self.state = processImage(img)

        speed, ms, finish = getGameState((self.speed,self.time,False))
        self.speed = speed
        self.time = ms

        stop = timeit.default_timer()
        t = SLEEPY+stop-start
        if(t<0):
            t=0
        #time.sleep(t)
        # Calculate reward
        reward = 40*speed/TOPSPEED - ms/2000

        self.score+=reward

        # Episode end
        done = False

        if(ms>MAXMS or (ms>0 and finish)):
            if(finish):
                reward +=1000

            done = True
            self.release_all()
        # also if finished
        info = {}
        # state = Dict({"speed":Discrete(speed), "time":Discrete(ms), "pic":Box(img,dtype=int)})
        return self.state, reward,done,info

        

    def render(self):
        pass

    def reset(self):
        self.limit=0
        print(self.score)
        self.score=0
        # restart race
        keyboard.press("l")
        keyboard.release("l")
        # wait for countdown timer
        time.sleep(1.5)
        self.start = timeit.default_timer()
        return self.state

    def release_all(self):
        keyboard.release("w")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("s")
