#!/usr/bin/env python

import os
import sys
import string
import glob

from jwst.datamodels import ImageModel

import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

if __name__ == '__main__':
    """
    Make figures of the lamp-on rate images collected at the cold
    plateau in OTIS.

    """

    #------------------------------------------------------------------------------------------------------------------

    directory = '/witserv/data18/martel/commissioning/1078/lamps_OTIS/'
    os.chdir(directory)

    line2_5_NISRAPID = '/witserv/data18/martel/commissioning/1078/lamps_OTIS/NISRAPID/lamp/stage1/jw00305001001_02102_00001_nis_rate_bkgsub.fits'  # 4788, LINE2/5, NISRAPID
    line2_5_NIS      = '/witserv/data18/martel/commissioning/1078/lamps_OTIS/NIS/stage1/jw00305001001_02103_00001_nis_rate.fits'                   # 4791, LINE2/5, NIS

    #---

    X_box_s = 1       # start of box in X as seen in DS9
    X_box_e = 2048    # end of box in X

    Y_box_s = 1       # start of box in Y
    Y_box_e = 2048    # end of box in Y

    star_X = 1        # coordinates of the reference pixels (corner for this)
    star_Y = 1

    #---
    # Line 2/5, 4788, NISRAPID

    plt.figure()

    plt.subplots_adjust(hspace = 0.5)

    plt.subplot(1,2,1) 

    minfig = 0         
    maxfig = 160

    data = ImageModel(line2_5_NISRAPID).data

    plt.imshow(data[Y_box_s-1:Y_box_e, X_box_s-1:X_box_e], cmap = 'gist_heat', vmin = minfig, vmax = maxfig, origin = 'bottom')
    plt.autoscale(False)

    plt.xticks([1, 1024, 2048], fontsize = 6)
    plt.yticks([1, 1024, 2048], fontsize = 6)

    cbar = plt.colorbar(orientation = 'horizontal', fraction = 0.05, pad = 0.07) 
    cbar.ax.tick_params(labelsize=6)

    plt.title('LINE2/5 (4788; NISRAPID)', fontsize=8)

    #---
    # Line 2/5, 4791, NIS

    plt.subplot(1,2,2) 

    minfig = 0         # Lamp
    maxfig = 160

    data = ImageModel(line2_5_NIS).data

    plt.imshow(data[Y_box_s-1:Y_box_e, X_box_s-1:X_box_e], cmap = 'gist_heat', vmin = minfig, vmax = maxfig, origin = 'bottom')
    plt.autoscale(False)

    plt.xticks([1, 1024, 2048], fontsize = 6)
    plt.yticks([1, 1024, 2048], fontsize = 6)

    cbar = plt.colorbar(orientation = 'horizontal', fraction = 0.05, pad = 0.07) 
    cbar.ax.tick_params(labelsize=6)

    plt.title('LINE2/5 (4791; NIS)', fontsize=8)

    plt.savefig('./1078_figure_lamps_rate_OTIS.png', orientation = 'portrait', dpi=150)
    plt.close()


