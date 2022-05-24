#!/usr/bin/env python

# Script written by Lorena Escudero (Department of Radiology, University of Cambridge)
# to compare two NIfTI files and compute the Dice Similary coefficient (DSC)
#                                                                                                                      

# Usage: python3 calculate_dice.py input_file1 input_file2

import os, sys
import numpy as np
import SimpleITK as sitk
#import matplotlib.pyplot as plt # OPTIONAL

# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    arguments  = sys.argv[1:]
    if (len(arguments)<2):
        sys.exit('Error: you need to provide two input files to compare!')

    input_file1 = arguments[0]
    input_file2 = arguments[1]

    # ATTN! Assuming provided input files are of NIfTI format 
    reader = sitk.ImageFileReader()
    reader.SetImageIO("NiftiImageIO")
    
    # OPT: Slice index to plot
    # slice_id = 29
    
    reader.SetFileName(input_file1)
    image_truth = reader.Execute()
    image_truth_arr = sitk.GetArrayFromImage(image_truth)
    
    # ATTN! Below is an example for two segmentation masks, kidney and tumour
    #image_truth_kidney = np.zeros(image_truth_arr.shape)
    #image_truth_kidney[image_truth_arr==1] = 1 
    
    #image_truth_tumour = np.zeros(image_truth_arr.shape)
    #image_truth_tumour[image_truth_arr==2] = 1 
    
    # OPT: Plotting one slice
    #curr_mask = image_truth_kidney[slice_id, :, :]
    #imgplot = plt.imshow(curr_mask, cmap='gray')
    #plt.show(block=True)
    
    reader.SetFileName(input_file2)
    image_seg = reader.Execute()
    image_seg_arr = sitk.GetArrayFromImage(image_seg)
    
    #image_seg_kidney = np.zeros(image_seg_arr.shape)
    #image_seg_kidney[image_seg_arr==1] = 1 
    
    #image_seg_tumour = np.zeros(image_seg_arr.shape)
    #image_seg_tumour[image_seg_arr==2] = 1 
    
    # OPT: Plotting one slice
    #curr_mask = image_seg_kidney[slice_id, :, :]
    #imgplot = plt.imshow(curr_mask, cmap='gray')
    #plt.show(block=True)
    
    
    mult_arr = np.multiply(image_truth_arr, image_seg_arr)
    #mult_arr_kidney  = np.multiply(image_truth_kidney, image_seg_kidney)
    #mult_arr_tumour = np.multiply(image_truth_tumour, image_seg_tumour)
    
    # OPT: Plotting one slice
    #curr_mask = mult_arr_kidney[slice_id, :, :]
    #imgplot = plt.imshow(curr_mask, cmap='gray')
    #plt.show(block=True)
    
    dice = np.sum(mult_arr)*2.0 / (np.sum(image_seg_arr) + np.sum(image_truth_arr))
    #dice_kidney = np.sum(mult_arr_kidney)*2.0 / (np.sum(image_seg_kidney) + np.sum(image_truth_kidney))
    #dice_tumour = np.sum(mult_arr_tumour)*2.0 / (np.sum(image_seg_tumour) + np.sum(image_truth_tumour))
    
    print('Dice coeffficient: %s' % (dice))
    #print('Dice coeffficient for kidney %s ' % (dice_kidney))
    #print('Dice coeffficient for tumour %s ' % (dice_tumour))
    
