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
    parser.add_argument("inputfiles", nargs=2)
    return parser.parse_args()


def main():
    args = getargs()
    with coco.coco(args.inputfiles[0]) as c1, coco.coco(args.inputfiles[1]) as c2:
        duplicate_image_ids = c1.get_intersection_imageid(c2)
        duplicate_annotation_ids = c1.get_intersection_annotationid(c2)
        union_image_ids = c1.get_union_imageid(c2)
        union_annotation_ids = c1.get_union_annotationid(c2)

        print('duplicate image count:', len(duplicate_image_ids))
        print('union image count:', len(union_image_ids))
        print('duplicate annotation count:', len(duplicate_annotation_ids))
        print('union annotation count:', len(union_annotation_ids))

if __name__ == "__main__":
    main()
