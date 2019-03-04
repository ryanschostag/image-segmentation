# -*- coding: utf-8 -*-

import image_segmentation as ims
from pprint import pprint
  

def main():
    image_file = 'small/test/ADE_val_00000037.jpg'
    i = ims.ImageMatrix()
    i.image = image_file
    i.image_to_matrix()
    for img in i.images:
        print(f'shape: {i.shape(img)}')
        print(f'threshold: {i.threshold(img)}')
        '''
        Example:

        shape: (397, 283, 3)
        /home/john/.local/share/virtualenvs/image-segmentation-zuN9SAIO/lib/python3.6/site-packages/skimage/filters/thresholding.py:278: UserWarning: threshold_otsu is expected to work correctly only for grayscale images; image shape (397, 283, 3) looks like an RGB image
          warn(msg.format(image.shape))
        threshold: 106
        '''
        pprint(img)
    

if __name__ == "__main__":
    main()
