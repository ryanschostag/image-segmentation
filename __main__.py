# -*- coding: utf-8 -*-

import image_segmentation as ims
  

def main():
    out_csv = 'output.csv'
    i = ims.Image(output_csv=out_csv)
    i.collect()

if __name__ == "__main__":
    main()
