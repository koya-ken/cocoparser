import coco
from coco import Image, Annotation
import argparse
import numpy as np
import sys

def getargs():
    parser = argparse.ArgumentParser(description='Process some integers.')
    # http://ja.pymotw.com/2/argparse/
    parser.add_argument("inputfile", action="store")
    parser.add_argument('--image', action='store_true', default=False)
    parser.add_argument('--annotation', action='store_true', default=False)
    parser.add_argument('-o', dest='outputfile',
                        type=str, default='ids.txt')

    return parser.parse_args()


def main():
    args = getargs()
    outpath = args.outputfile if args.outputfile != '-' else sys.stdout.buffer

    if not (args.image or args.annotation):
        args.image = True

    with coco.coco(args.inputfile) as data:
        if args.image:
            np.savetxt(outpath, data.np_images[:, Image.ID], fmt='%d')
        elif args.annotation:
            np.savetxt(
                outpath, data.np_annotations[:, Annotation.ID], fmt='%d')


if __name__ == "__main__":
    main()
