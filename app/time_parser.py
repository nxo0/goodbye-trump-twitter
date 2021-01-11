#from enum import IntEnum, auto

#class TimeName(IntEnum):
#    DAY = auto()
#    HOUR = auto()
#    MIN = auto()
#    SEC = auto()
#
#day = TimeName.DAY
#hour = TimeName.hour
#time_names = {'d': day,
#        'day': day,
#        'days': day,
#        }
#
#
#def parser(time):
#    tn = time_names.get(time)
#    if tn is None:
#        raise


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
