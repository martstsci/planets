#!/usr/bin/env python

import os
import sys
import string
import glob

import numpy as np
import matplotlib.pyplot as plt

from astropy.io.fits import getdata, writeto

if __name__ == '__main__':
    """ 
    >>> from astropy.io import fits
    >>> photofile = fits.open('jw10781001001_01101_00001_NIRISS_uncal.fits')
    >>> photofile.info()
    >>> photofile.info()
    Filename: jw10781001001_01101_00001_NIRISS_uncal.fits
    No.    Name      Ver    Type      Cards   Dimensions   Format
      0  PRIMARY       1 PrimaryHDU     199   ()      
      1  SCI           1 ImageHDU        13   (2048, 2048, 88, 1)   int16 (rescales to uint16)   
    >>> photodata = photofile[1].data
    >>> photodata[0].shape
        (88, 2048, 2048)
    >>> photodata[0][0].shape
        (2048, 2048)

    """

    #------------------------------------------------------------------------------------------------------------------

    directory = '/witserv/data18/martel/commissioning/1078/warm_dark/'
    os.chdir(directory)

    warm_dark = 'jw10781001001_01101_00001_NIRISS_uncal.fits'  # 25957, 90.3K

    #---

    X_box_s = 1       # start of box in X
    X_box_e = 2048    # end of box in X

    Y_box_s = 1      # start of box in Y
    Y_box_e = 2048   # end of box in Y

    star_X = 1       # coordinates of the reference pixels (corner for this)
    star_Y = 1

    #---

    plt.figure()

    minfig = 0         
    maxfig = 26000

    data, hdr = getdata(warm_dark, header = True)

    first_group = data[0][0]

    plt.imshow(first_group[Y_box_s:Y_box_e, X_box_s:X_box_e], cmap = 'gist_heat', vmin = minfig, vmax = maxfig, origin = 'bottom')
    plt.autoscale(False)

    plt.xticks([1, 1024, 2048], fontsize = 6)
    plt.yticks([1, 1024, 2048], fontsize = 6)

    #cbar = plt.colorbar(orientation = 'horizontal', ticks = [0, 5000, 10000, 15000])  # draw colorbar
    cbar = plt.colorbar(orientation = 'vertical') # draw colorbar
    cbar.ax.tick_params(labelsize=6)

    plt.title('Warm Dark (25957)', fontsize=8)

    plt.savefig('./warm_dark_1078.png', orientation = 'portrait', dpi=150)
    plt.close()


