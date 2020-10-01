#!/usr/bin/env python3

import notify2
from subprocess import check_output, STDOUT, CalledProcessError
import os
os.environ["PBR_VERSION"] = "4.0.2"
from tendo import singleton
me = singleton.SingleInstance()
notify2.init("Spy Notify")
while True:
    cmd = "fuser /dev/video0"
    try:
        usage = check_output(cmd, stderr=STDOUT, shell=True)
        returncode = 0
    except CalledProcessError as ex:
        usage = ex.output
        returncode = ex.returncode
        if returncode != 1:
            raise
    if returncode == 0:
        img_path = "/opt/Spy Notify/image1.ico"
        notify2.Notification("Webcam in Use", message="Your webcam is being used! Is this you?", icon=img_path).show()
        use = True
        while use == True:
            try:
                usage = check_output(cmd, stderr=STDOUT, shell=True)
                returncode = 0
            except CalledProcessError as ex:
                usage = ex.output
                returncode = ex.returncode
                if returncode != 1:
                    raise
            if returncode != 0:
                use = False
                break
