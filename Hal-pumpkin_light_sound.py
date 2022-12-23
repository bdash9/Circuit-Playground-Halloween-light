import math
import os
import random
import time

from adafruit_circuitplayground.express import cpx
import audioio
import board
import digitalio

"""Blue--- CANDLE_COLOR = (0x00, 0xC0, 0xFF)"""
"""Red"""
CANDLE_COLOR = (0x80, 0x00, 0x00)
MIN_BRIGHTNESS = 64
MAX_BRIGHTNESS = 191

EFFECT_COLOR = (0xFF, 0x00, 0x00)
STEPS_BEFORE_EFFECT = 100

def split(first, second, offset):
    if offset != 0:
        mid = ((first + second + 1) / 2 + random.randint(-offset, offset))
        offset = int(offset / 2)
        split(first, mid, offset)
        split(mid, second, offset)
    else:
        level = math.pow(first / 255.0, 2.7) * 255.0 + 0.5
        cpx.pixels.fill((
            min(255, int(level * CANDLE_COLOR[0] / 256)),
            min(255, int(level * CANDLE_COLOR[1] / 256)),
            min(255, int(level * CANDLE_COLOR[2] / 256))
        ))
        cpx.pixels.show()

def colorShift(start, end, time):
    for i in range(1, time):
        j = time - i
        cpx.pixels.fill((
            min(255, int((start[0] * j + end[0] * i) / time)),
            min(255, int((start[1] * j + end[1] * i) / time)),
            min(255, int((start[2] * j + end[2] * i) / time))
        ))
        cpx.pixels.show()

cpx.pixels.brightness = 0.4
cpx.pixels.auto_write = False
cpx.pixels.fill((0, 0, 0))
cpx.pixels.show()

sounds = [f for f in os.listdir() if f.endswith('.wav')]

count = 0
prev = (MAX_BRIGHTNESS + MIN_BRIGHTNESS) / 2

while True:
    lvl = random.randint(MIN_BRIGHTNESS, MAX_BRIGHTNESS)
    split(prev, lvl, 32)
    prev = lvl
    count += 1
    if (count > STEPS_BEFORE_EFFECT):
        count = 0
        if cpx.switch:
            oldcolor = cpx.pixels[0]
            cpx.pixels.fill(EFFECT_COLOR)
            cpx.pixels.show()
            cpx.play_file(random.choice(sounds))
            colorShift(EFFECT_COLOR, oldcolor, 10)
