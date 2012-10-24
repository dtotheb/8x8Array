#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight
import LetterArrays

grid = EightByEight(address=0x70)

def drawFrame(frame, grid, dur=0):
    for pix in frame:
        grid.setPixel(pix[0],pix[1])
        time.sleep(dur)


word = LetterArrays.wordForOutput
#loop through the letters
while (True):
    for letter in word:
        if letter in LetterArrays.CHARS:
            c = LetterArrays.CHARS[letter]
            c = LetterArrays.CHARS[letter]
            drawFrame(c, grid)
            time.sleep(0.5)
            grid.clear()

    reload(LetterArrays)
    word = LetterArrays.wordForOutput
