#!/usr/bin/env python

import argparse
import os
import glob
import shutil

from shutil import copy

from subprocess import call

from jwst import datamodels
from jwst.pipeline import Detector1Pipeline

if __name__ == '__main__':
    """
    Script to process _uncal.fits through the Stage 1 pipeline.

    Process the CV3 internal flat fields for 1078 by manually
    specifying the superdark and superbias reference files, which were
    already grabbed from the CRDS directory.

    The processed data will go into the stage1/ subdirectory.

    """

    parser = argparse.ArgumentParser(description = 'Process NIRISS exposures through Stage 1 (class Detector1Pipeline).', add_help = True)

    parser.add_argument('-d', '--dr', '--directory', default = '/witserv/data18/martel/commissioning/1078/lamps_CV3/', dest = 'dir', type = str, action = 'store', help = "Directory of the _uncal.fits exposures.")  
    parser.add_argument('-c', '--cw', '--calwebb',   default = 'calwebb_detector1_1078_lamps_CV3.cfg', dest = 'calw', type = str, action = 'store', help = "calwebb_detector1 file to use.")  
   
    inputs = parser.parse_args()
    dir_exp = inputs.dir
    calwebb = inputs.calw

    #---

    results_dir = os.path.join(dir_exp, 'stage1')

    if os.path.exists(results_dir): shutil.rmtree(results_dir)
    os.mkdir(results_dir)

    #---

    all_uncal = sorted(glob.glob(os.path.join(dir_exp, '*_uncal.fits')))

    for f in all_uncal:

      print ("*****************************************************")
      print (f)

      modf = datamodels.open(f)

      result = Detector1Pipeline.call(modf, config_file = calwebb, save_results = True, save_calibrated_ramp = True, output_dir = results_dir)   

      # Note: save_results saves the _rateints and _rate files while
      #       save_calibrated_ramp (also specified in the
      #       calwebb_detector1.cfg file) saves the intermediate files
      #       (_ramp). If these are not specified, then no files will
      #       be produced.
      #
      # For save_results = True, save_calibrated_ramp = True, the intermediate and final files are: 
      #
      #      *_NIRISS_ramp.fits, *_NIRISS_rateints.fits, *_NIRISS_rate.fits (final)
      #
      #  Filename: jw00666001001_01101_00001_NIRISS_ramp.fits
      #  No.    Name      Ver    Type      Cards   Dimensions   Format
      #    0  PRIMARY       1 PrimaryHDU     222   ()      

      #    1  SCI           1 ImageHDU        12   (2048, 2048, 108, 1)   float32   
      #    2  PIXELDQ       1 ImageHDU        11   (2048, 2048)   int32 (rescales to uint32)   
      #    3  GROUPDQ       1 ImageHDU        11   (2048, 2048, 108, 1)   uint8   
      #    4  ERR           1 ImageHDU        11   (2048, 2048, 108, 1)   float32   
      #    5  ASDF          1 BinTableHDU     11   1R x 1C   [3844B]   
      #
      #  Filename: jw00666001001_01101_00001_NIRISS_rateints.fits
      #  No.    Name      Ver    Type      Cards   Dimensions   Format
      #    0  PRIMARY       1 PrimaryHDU     225   ()      
      #    1  SCI           1 ImageHDU        11   (2048, 2048, 1)   float32   
      #    2  ERR           1 ImageHDU        11   (2048, 2048, 1)   float32   
      #    3  DQ            1 ImageHDU        12   (2048, 2048, 1)   int32 (rescales to uint32)   
      #    4  INT_TIMES     1 BinTableHDU     24   0R x 7C   [J, D, D, D, D, D, D]   
      #    5  VAR_POISSON   1 ImageHDU        10   (2048, 2048, 1)   float32   
      #    6  VAR_RNOISE    1 ImageHDU        10   (2048, 2048, 1)   float32   
      #    7  ASDF          1 BinTableHDU     11   1R x 1C   [4614B]   
      #
      #  Filename: jw00666001001_01101_00001_NIRISS_rate.fits
      #  No.    Name      Ver    Type      Cards   Dimensions   Format
      #    0  PRIMARY       1 PrimaryHDU     225   ()      
      #    1  SCI           1 ImageHDU        10   (2048, 2048)   float32   
      #    2  ERR           1 ImageHDU        10   (2048, 2048)   float32   
      #    3  DQ            1 ImageHDU        11   (2048, 2048)   int32 (rescales to uint32)   
      #    4  VAR_POISSON   1 ImageHDU         9   (2048, 2048)   float32   
      #    5  VAR_RNOISE    1 ImageHDU         9   (2048, 2048)   float32   
      #    6  ASDF          1 BinTableHDU     11   1R x 1C   [4029B]   




    


