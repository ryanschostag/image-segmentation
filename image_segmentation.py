#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:42:36 2019

@author: Ryan Schostag
"""

from skimage.io import imread
from skimage.color import rgb2gray
from skimage import filters
from os import chdir, path
from glob import glob


class ImageMatrix(object):
    """
    Converts image to numpy matrix
    
    Dependencies: 
        
        Scipy
        Python 3.x
        
    """
    def __init__(self, image=None, mode='RGB'):
        super().__init__()
        self.image = image
        self.mode = mode
        self.images = []
        self.directory = None
        
    def __call__(self):
        self.image_to_matrix()
    
    def to_matrix(self):
        """
        Converts the image to matrix
        """
        self.image = imread(
            fname=self.image,
            mode=self.mode
        )
            
    def to_gray(self):
        """
        Converts the image to grayscale
        """
        self.image = rgb2gray(self.image)
            
    def shape(self, image_matrix):
        return image_matrix.shape
            
    def threshold(self, image_matrix):
        return filters.threshold_otsu(image_matrix)
        
    def glob_images(self):
        if self.directory is not None and path.exists(self.directory):
            chdir(self.directory)
        
        self.images.extend(list(glob('**/*.jp*g', recursive=True)))
        self.images.extend(list(glob('**/*.png', recursive=True)))
        self.images.extend(list(glob('**/*.gif', recursive=True)))
    
    def is_image(self):
        pass


