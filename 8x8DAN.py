#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight
import LetterArrays

grid = EightByEight(address=0x70)

print "Press CTRL+Z to exit"

#loop through the letters
while (True):
    for letter in LetterArrays.wordForOutput:
        c = LetterArrays.letterDict[letter]
        for p in c:
            grid.setPixel(p[0], p[1])
            time.sleep(0.005)
        time.sleep(0.5)
        grid.clear()

    reload(LetterArrays)
