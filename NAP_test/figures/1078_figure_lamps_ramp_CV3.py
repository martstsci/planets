#!/usr/bin/env python

import os
import sys
import string
import glob

from jwst.datamodels import RampModel

import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

if __name__ == '__main__':
    """
    Make figures of the mean of the appropriate group of the
    integrations of the lamp-on ramp cube collected at the cold
    plateau in CV3.

    """

    #------------------------------------------------------------------------------------------------------------------

    directory = '/witserv/data18/martel/commissioning/1078/lamps_CV3/stage1/'
    os.chdir(directory)

    flat1_5 = 'jw10782001001_01102_00001_NIRISS_ramp.fits'  # 35495, FLAT1/5
    flat2_5 = 'jw10782001001_01101_00001_NIRISS_ramp.fits'  # 35423, FLAT2/5
    line1_5 = 'jw10782001001_01103_00001_NIRISS_ramp.fits'  # 35496, LINE1/5
    line2_5 = 'jw10782001001_01103_00001_NIRISS_ramp.fits'  # 35498, LINE2/5

    #---

    X_box_s = 1       # start of box in X as seen in DS9
    X_box_e = 2048    # end of box in X

    Y_box_s = 1       # start of box in Y
    Y_box_e = 2048    # end of box in Y

    star_X = 1        # coordinates of the reference pixels (corner for this)
    star_Y = 1

    #---
    # Flat 1/5

    plt.figure()

    plt.subplots_adjust(hspace = 0.3)

    plt.subplot(2,2,1) 

    minfig = 0         
    maxfig = 11000

    all_data = RampModel(flat1_5).data

    data_cube = all_data[:, :, :,:][:, 4]     # Grab the fifth group of all the integrations and stack in a cube. (NINTS, NROWS, NCOLS)
    data      = np.mean(data_cube, axis = 0)   # mean along the vertical axis, works too if only one integration

    plt.imshow(data[Y_box_s-1:Y_box_e, X_box_s-1:X_box_e], cmap = 'gist_heat', vmin = minfig, vmax = maxfig, origin = 'bottom')
    plt.autoscale(False)

    plt.xticks([1, 1024, 2048], fontsize = 6)
    plt.yticks([1, 1024, 2048], fontsize = 6)

    cbar = plt.colorbar(orientation = 'vertical') # draw colorbar
    cbar.ax.tick_params(labelsize=6)

    plt.title('FLAT1/5 (35495)', fontsize=8)

    #---
    # Flat 2/5

    plt.subplot(2,2,2) 

    minfig = 0         # Lamp
    maxfig = 11000

    all_data = RampModel(flat2_5).data

    data_cube = all_data[:, :, :,:][:, 4] 
    data      = np.mean(data_cube, axis = 0)   

    plt.imshow(data[Y_box_s-1:Y_box_e, X_box_s-1:X_box_e], cmap = 'gist_heat', vmin = minfig, vmax = maxfig, origin = 'bottom')
    plt.autoscale(False)

    plt.xticks([1, 1024, 2048], fontsize = 6)
    plt.yticks([1, 1024, 2048], fontsize = 6)

    cbar = plt.colorbar(orientation = 'vertical') # draw colorbar
    cbar.ax.tick_params(labelsize=6)

    plt.title('FLAT2/5 (35423)', fontsize=8)

    #---
    # Line 1/5

    plt.subplot(2,2,3) 

    minfig = 0         
    maxfig = 11000

    all_data = RampModel(line1_5).data

    data_cube = all_data[:, :, :,:][:, 7]      # Grab the 8th group.
    data      = np.mean(data_cube, axis = 0)   

    plt.imshow(data[Y_box_s-1:Y_box_e, X_box_s-1:X_box_e], cmap = 'gist_heat', vmin = minfig, vmax = maxfig, origin = 'bottom')
    plt.autoscale(False)

    plt.xticks([1, 1024, 2048], fontsize = 6)
    plt.yticks([1, 1024, 2048], fontsize = 6)

    cbar = plt.colorbar(orientation = 'vertical') # draw colorbar
    cbar.ax.tick_params(labelsize=6)

    plt.title('LINE1/5 (35496)', fontsize=8)

    #---
    # Line 2/5

    plt.subplot(2,2,4) 

    minfig = 0         
    maxfig = 11000

    all_data = RampModel(line2_5).data

    data_cube = all_data[:, :, :,:][:, 7] 
    data      = np.mean(data_cube, axis = 0)   

    plt.imshow(data[Y_box_s-1:Y_box_e, X_box_s-1:X_box_e], cmap = 'gist_heat', vmin = minfig, vmax = maxfig, origin = 'bottom')
    plt.autoscale(False)

    plt.xticks([1, 1024, 2048], fontsize = 6)
    plt.yticks([1, 1024, 2048], fontsize = 6)

    cbar = plt.colorbar(orientation = 'vertical') # draw colorbar
    cbar.ax.tick_params(labelsize=6)

    plt.title('LINE2/5 (35498)', fontsize=8)

    plt.savefig('./1078_figure_lamps_ramp_CV3.png', orientation = 'portrait', dpi=150)
    plt.close()


