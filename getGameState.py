

def getGameState():
    path = r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\games\Trackmania"
    data = ";;"
    xd = []
    while(len(xd)!= 3):
        with open( path+'\gameState.txt','r') as reader:
            data = reader.read()
        xd = data.strip().split(";")
    
    # something went wrong while reading while, it was probably opened by the script at the same time
    speed = xd[0]
    time = xd[1]
    checkpoint = xd[2]
    try:
        s= int(speed)
        t = int(time)
        c = int(checkpoint)
    except ValueError:
        s = None
        t = None
    return s,t,c
