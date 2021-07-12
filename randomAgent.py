import keyboard
from tmEnvironment import tmEnv


def test_run():
    # Wait for me to push B to start
    keyboard.wait('b')
    done = False
    score = 0
    env = tmEnv()
    env.reset()
    while not done:
        action=env.action_space.sample()
        # always go forward
        action[0] = 1
        state,reward,done,info = env.step(action)
        score+=reward
    print("SCORE:", score)
    print("DONE")

test_run()
