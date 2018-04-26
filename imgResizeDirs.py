#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 21:02:11 2018

@author: koichirosato
"""

import os
from PIL import Image
from os.path import join, getsize

for root, dirs, files in os.walk('/Users/koichirosato/Dropbox/自主防災会資料'):

    for f in files:

        ftitle, fext = os.path.splitext(f)

        if not f.startswith('.') and \
        getsize(join(root,f))>800000 and \
        (fext.find('.jpg') > -1 or fext.find('.JPG') > -1):
            
            img = Image.open(join(root,f))

            '''
            iPhone撮影の縦写真が横になってしまう現象への対応として、
            exif情報を取得して、維持するように改修
            でも、色空間がCMYKのファイルで実行するとエラーになる？
            /Users/koichirosato/Dropbox/自治会資料/⑥文化部/ナリア祭り/H28/模造紙印刷/素材
            抽選.jpg
            尚、py3exif2をインストールするのは難しくて断念（c++で実装されたexif2ライブラリのbind
            '''
            exif = img.info['exif']

            print(root +':' + f)
            img_resize = img.resize((int(img.width/2), int(img.height/2)))
            img_resize.save(join(root, ftitle + fext), exif=exif)