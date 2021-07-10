

def getGameState(prev):
    path = r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\games\Trackmania"
    data = ";;"
    with open( path+'\gameState.txt','r') as reader:
        data = reader.read()
    
    xd = data.strip().split(";")
    # something went wrong while reading while, it was probably opened by the script at the same time
    if(len(xd)!= 3):
        return prev
    speed = xd[0]
    time = xd[1]
    finished = xd[2]
    if(finished == "False"):
        f = False
    else:
        f = True
    try:
        s= int(speed)
        t = int(time)
    except ValueError:
        s = None
        t = None
    return s,t,f
