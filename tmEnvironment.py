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
        self.finishcp = 0
        self.lastcp = -1

        
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

        speed, ms, checkpoint = getGameState()
        self.speed = speed
        self.time = ms

        stop = timeit.default_timer()
        t = SLEEPY+stop-start
        if(t<0):
            t=0
        #time.sleep(t)
        # Calculate reward
        #reward = 60*speed/TOPSPEED - ms/4000
        reward = 0
        reward += speed/100

        # reward reaching next checkpoint
        if(checkpoint != self.lastcp and ms>1000):
            reward+= 100*(MAXMS/ms)*(checkpoint+1)
            self.lastcp = checkpoint
            


        

        # Episode end
        done = False

        # Car stopped after beginning, usually means stuck
        """if(speed<2 and ms>1000):
            reward-=10000
            done= True
            self.release_all()"""

        if(ms>MAXMS or (ms>1000 and checkpoint==self.finishcp)):
            if(checkpoint==self.finishcp and ms>1000):
                reward +=10000
            done = True
            self.release_all()
        # also if finished
        info = {}
        self.score+=reward
        return self.state, reward,done,info

        

    def render(self):
        pass

    def reset(self):
        self.limit=0
        cv2.destroyAllWindows()
        print(self.score)
        self.score=0
        # restart race
        keyboard.press("l")
        keyboard.release("l")
        
        # wait for countdown timer
        time.sleep(1.7)
        # at the beginning checkpoints is the amount of cp in map
        # when reaching first checkpoint counter goes to 0 and finish is at
        # beginning -1
        _,_,self.lastcp = getGameState()
        self.finishcp-= self.lastcp-1
        self.start = timeit.default_timer()
        return self.state

    def release_all(self):
        keyboard.release("w")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("s")
