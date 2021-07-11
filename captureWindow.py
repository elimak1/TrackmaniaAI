import numpy as np
import mss
import mss.tools


def captureWindow():
    with mss.mss() as sct:
    # Get information of monitor 2
        monitor_number = 2
        mon = sct.monitors[monitor_number]

        # The screen part to capture
        monitor = {
            "top": mon["top"] + 30,
            "left": mon["left"] + 0,  
            "width": 800,
            "height": 600,
            "mon": monitor_number,
        }
        # Grab the data
        im = sct.grab(monitor)
    return numpy_flip(im)

def numpy_flip(im):
    """ Most efficient Numpy version as of now. """
    frame = np.array(im, dtype=np.uint8)
    return np.flip(frame[:, :, :3], 2)