import gc
from ColorSplash import *

class Global(object):
    def __init__(self):
        Blackxxx = '\033[30;1m'
        Redxxxxx = '\033[31;1m'
        Greenxxx = '\033[32;1m'
        Yellowxx = '\033[33;1m'
        Bluexxxx = '\033[34;1m'
        Magentax = '\033[35;1m'
        Cyanxxxx = '\033[36;1m'

Whitexxx = '\033[37;1m'
BBlackxx = '\033[30;2m'
BRedxxxx = '\033[31;2m'
BGreenxx = '\033[32;2m'
BYellowx = '\033[33;2m'
BBluexxx = '\033[34;2m'
BMagenta = '\033[35;2m'
BCyanxxx = '\033[36;2m'
BWhitexx = '\033[36;2m'

lib = [Blackxxx, Redxxxxx, Greenxxx, Yellowxx, Bluexxxx, Magentax, Cyanxxxx, Whitexxx, BBlackxx, BRedxxxx, BGreenxx, BYellowx, BBluexxx, BMagenta, BCyanxxx, BWhitexx]

num = "1234567890"

global x
x = 0

#while True:
#    for i in range(0, len(num)):
#        if x == len(lib):
##            x = 0
#            gc.collect()
#        print(lib[x] + num[i], end='')
#        x += 1

print(Global.Blackxxx)
