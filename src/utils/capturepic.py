#!/usr/bin/env python
# encoding: utf-8
from PIL import ImageGrab

def capture_screen(name):
    pic = ImageGrab.grab()
    pic.save(name+'.jpg')