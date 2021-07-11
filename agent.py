from stable_baselines3 import PPO
import stable_baselines3
import os
from tmEnvironment import tmEnv
import keyboard

def createModel():
    log_path = os.path.join("training", "logs")
    env = tmEnv()
    model = PPO("CnnPolicy",env,verbose=1,tensorboard_log=log_path)
    return model

def train(model, timesteps):
    model.learn(total_timesteps=timesteps)
    return model

def saveModel(model,name):
    modelPath = os.path.join("training","savedModels",name)
    model.save(modelPath)

def loadPPOModel(name,env):
    modelPath = os.path.join("training","savedModels",name)
    return PPO.load(modelPath,env)

model = createModel()
print("Model ready!")
keyboard.wait('b')
model = train(model,10000)
saveModel(model, "PPO_10k_training1")