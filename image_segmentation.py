#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:42:36 2019

@author: Ryan Schostag
"""

from skimage.io import imread
from skimage import filters
from pprint import pprint


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
        
    def __call__(self):
        self.image_to_matrix()
    
    def image_to_matrix(self):
        """
        Converts the image to matrix
        """
        self.images.append(
            imread(
                fname=self.image,
                mode=self.mode
            )
        )
            
    def shape(self, image_matrix):
        return image_matrix.shape
            
    def threshold(self, image_matrix):
        return filters.threshold_otsu(image_matrix)
        
    def glob_images(self):
        pass
    
    def is_image(self):
        pass


