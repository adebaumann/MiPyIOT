from time import sleep
import os


def DoubleReset(Time=5, File="doublereset.txt"):
    """Use this at the beginning of the file.
    DoubleReset(Time=5,File="doublereset.txt")
    Determines, if the board had two successive resets in the last <n> seconds.
    This is done by writing a file in <File> and deleting it after <n> seconds.
    If the file is already there, the reset was doubled."""
    try:
        a = open(File)
        Check = a.read().strip()
        a.close()
        a = open(File, "w")
        a.write(str(int(Check) + 1))
        a.close()
        sleep(Time)
        os.remove(File)
        return int(Check) + 1
    except OSError:
        pass
    a = open(File, "w")
    a.write("1")
    a.close()
    sleep(Time)
    os.remove(File)
    return False
