import cv2
from subprocess import check_output, STDOUT, CalledProcessError, call
cap = cv2.VideoCapture(0)
try:
    cam1 = check_output("lsof | grep AppleCamera", stderr=STDOUT, shell=True)
    returncode1 = 0
except CalledProcessError as ex:
    cam1 = ex.output
    returncode1 = ex.returncode
    if returncode1 != 1:
        raise
try:
    cam2 = check_output("lsof | grep iSight", stderr=STDOUT, shell=True)
    returncode2 = 0
except CalledProcessError as ex:
    cam2 = ex.output
    returncode2 = ex.returncode
    if returncode2 != 1:
        raise
try:
    cam3 = check_output("lsof | grep VDC", stderr=STDOUT, shell=True)
    returncode3 = 0
except CalledProcessError as ex:
    cam3 = ex.output
    returncode3 = ex.returncode
    if returncode3 != 1:
        raise
if cam1 == cam2:
    cmd = "lsof | grep VDC"
elif cam1 == cam3:
    cmd = "lsof | grep iSight"
elif cam2 == cam3:
    cmd = "lsof | grep AppleCamera"
settings = open("/Library/Spy Notify/settings.txt","w")
settings.write(cmd)
settings.close()
call("open -a Spy-Notify", shell=True)
exit()
