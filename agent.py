from stable_baselines3 import PPO
from stable_baselines3 import A2C
import stable_baselines3
import os
from tmEnvironment import tmEnv
import keyboard

def createModel():
    log_path = os.path.join("training", "logs")
    env = tmEnv()
    model = PPO("CnnPolicy",env,verbose=1,tensorboard_log=log_path, learning_rate=0.0001)
    return model

def createA2CModel():
    log_path = os.path.join("training", "logs")
    env = tmEnv()
    model = A2C("CnnPolicy",env,verbose=1,tensorboard_log=log_path, learning_rate=0.00005)
    return model

def saveModel(model,name):
    modelPath = os.path.join("training","savedModels",name)
    model.save(modelPath)

def loadPPOModel(name,env):
    modelPath = os.path.join("training","savedModels",name)
    return PPO.load(modelPath,env)
    
def loadA2CModel(name,env):
    modelPath = os.path.join("training","savedModels",name)
    return A2C.load(modelPath,env)

env = tmEnv()
model = loadA2CModel("A2C10k_customTrack1",env)
print("Model ready!")
keyboard.wait('b')
model = model.learn(total_timesteps=40000)
saveModel(model, "A2C40k_customTrack1")