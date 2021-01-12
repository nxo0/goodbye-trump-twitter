from gbtrump.logger import Logger

def timestr2sec(time):
    te = time.endswith
    if te("d"):
        return 60 * 60 * 24 * int(time[:-1])
    elif te("h"):
        return 60 * 60 * int(time[:-1])
    elif te("m"):
        return 60 * int(time[:-1])
    elif te("s"):
        return int(time[:-1])
    else:
        Logger.error("not match time." + time)
