from time import sleep
import os

def DoubleReset(Time=5,File="doublereset.txt"):
    try:
        a=open(File)
        Check=a.read().strip()
        a.close()
        if Check == '1':
            os.remove(File)
            return True
    except OSError:
        pass
    a=open(File,"w")
    a.write("1")
    a.close()
    sleep(Time)
    os.remove(File)
    return False

    