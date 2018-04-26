#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:53:38 2018

@author: koichirosato
"""

import numpy as np
import matplotlib.pyplot as plt
def manderblot(h, w, maxit = 20):
    """ Returns an image of the Mandelbrot fractal of size(h, w). """
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    
    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime==maxit)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

plt.imshow(manderblot(500, 500))
plt.show
    