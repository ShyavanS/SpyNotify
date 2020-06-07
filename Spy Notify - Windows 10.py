from win10toast import ToastNotifier
import cv2
import os
os.environ["PBR_VERSION"] = "4.0.2"
from tendo import singleton
me = singleton.SingleInstance()
while True:
    notify = ToastNotifier()
    cap = cv2.VideoCapture(0)
    if cap.read() == (False, None):
        var = True
    else:
        var = False
    cap.release()
    if var != False:
        notify.show_toast("Webcam in Use","Your webcam is being used! Is this you?",icon_path="image1.ico",duration=10)
        use = True
        while use == True:
            cap = cv2.VideoCapture(0)
            if cap.read() != (False, None):
                use = False
                break