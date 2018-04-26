#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 21:02:11 2018

@author: koichirosato
"""

import os
import glob
from PIL import Image
from os.path import getsize

files = glob.glob('/Users/koichirosato/Documents/img/org/*.jpg')

for f in files:

    if getsize(f)>1000000:

        img = Image.open(f)
        img_resize = img.resize((int(img.width/2), int(img.height/2)))
        ftitle, fext = os.path.splitext(f)
        img_resize.save(ftitle + '_harf' + fext)


