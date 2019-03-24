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
import magic as fmagic
import csv


class Matrix(object):
    """
    Converts image to numpy matrix
    
    Dependencies: 
        
        Scipy
        Python 3.x
        
    """
    img_dir = None
    output_csv=None
    image = None
    images = []
    data = {
        'image': None,
        'shape': None,
        'threshold': None,
        'matrix_rgb': None,
        'matrix_gray': None,
    }
    
    def __init__(self, image=None, img_dir=None):
        super().__init__()
        self.image_file = image
        self.image_rgb = None
        self.image_gray = None
        self.mode = 'RGB'
        self.img_dir = img_dir
    
    @property
    def threshold(self):
        return filters.threshold_otsu(self.image_gray)
    
    def is_image(self):
        allowed_mime_types = ('image/jpeg','image/png')
        f_type = fmagic.Magic(mime=True, uncompress=True)
        t = f_type.from_file(self.image)
        return t in allowed_mime_types
        
    def collect(self):
        if self.img_dir is not None and path.exists(self.img_dir):
            chdir(self.img_dir)

        types = ('jp*g', 'png')
        for img_type in types: 
            self.images.extend(glob('**/*' + img_type + '*', recursive=True))
    
    def image_to_matrices(self):
        """
        Converts the image to matrix
        """
        self.image_rgb = imread(
            fname=self.image,
            mode=self.mode
        )
        self.image_gray = rgb2gray(self.image_rgb)


class CSV(Matrix):
    def __init__(self, image=self.image_file, img_dir=self.img_dir, output_csv):
        super().__init__()
        self.output_csv = output_csv

    def row(self):
        self.data = {
            'image': self.image_file,
            'shape': self.image_gray.shape,
            'threshold': self.threshold,
            'matrix_rgb': self.image_rgb,
            'matrix_gray': self.image_gray,
        }

    def to_csv(self):
        f = open(self.output_csv, mode='a')
        fieldnames = list(self.data.keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(self.data)
        f.close()


class Image(CSV):
    def __init__(self, image=None, img_dir=None, output_csv=None):
        super().__init__()
        self.output_file_check()
        
    def output_file_check(self):
        if self.output_csv is None:
            raise ValueError('Output file not provided.')

