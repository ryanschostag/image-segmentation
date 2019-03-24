# -*- coding: utf-8 -*-

import image_segmentation as ims
from pprint import pprint
  

def main():
    image_file = 'small/test/ADE_val_00000037.jpg'
    i = ims.ImageMatrix()
    i.image = image_file
    i.to_matrix()
    i.to_gray()
    print(f'shape: {i.shape(i.image)}')
    print(f'threshold: {i.threshold(i.image)}')
    pprint(i.image)


if __name__ == "__main__":
    main()
