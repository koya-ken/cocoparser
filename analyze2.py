import coco
from coco import Annotation,Image
import argparse
import collections
# import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import os


def getargs():
    parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('-i', dest='inputfile', type=str, required=True)
    # http://ja.pymotw.com/2/argparse/
    parser.add_argument("inputfile", action="store")
    return parser.parse_args()


def main():
    args = getargs()
    with coco.coco(args.inputfile) as data:
        image_ids = data.np_images[:, Image.ID]
        annotation_ids = data.np_annotations[:, Annotation.ID]
        annotated_images = set(data.np_annotations[:, Annotation.IMAGE_ID])
        image_widths = data.np_images[:, Image.WIDTH]
        image_heights = data.np_images[:, Image.HEIGHT]
        print('image count:', len(image_ids))
        print('annotated image count:', len(annotated_images))
        print('annotation count:', len(annotation_ids))
        print('image id max:', max(image_ids))
        print('annotation id max:', max(annotation_ids))
        print('image width max:', max(image_widths))
        print('image height max:', max(image_heights))
        print('image width min:', min(image_widths))
        print('image height min:', min(image_heights))
        print('image width ave:', np.mean(image_widths))
        print('image height ave:', np.mean(image_heights))

if __name__ == "__main__":
    main()
