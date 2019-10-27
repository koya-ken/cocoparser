import coco
from coco import Image, ImageId, AnnotationId
import argparse
import time
import numpy as np


def getargs():
    parser = argparse.ArgumentParser(description='Process some integers.')
    # http://ja.pymotw.com/2/argparse/
    parser.add_argument("inputfiles", nargs=2)
    parser.add_argument('--image', action='store_true', default=False)
    parser.add_argument('--annotation', action='store_true', default=False)
    parser.add_argument('-o', dest='outputfile',
                        type=str, default='intersection.json')

    return parser.parse_args()


def main():
    args = getargs()

    if not (args.image or args.annotation):
        args.image = True
    id_txt = args.inputfiles[1]
    ids = np.loadtxt(fname=id_txt, dtype="int")
    begin_time = int(round(time.time() * 1000))
    with coco.coco(args.inputfiles[0]) as data:
        end_time = int(round(time.time() * 1000))
        print(f'finish load {end_time-begin_time} ms', flush=True)
        filtered_ids = ids
        print('begin filter')
        begin_time = int(round(time.time() * 1000))
        if args.image:
            filtered_ids = ImageId(filtered_ids)
        else:
            filtered_ids = AnnotationId(filtered_ids)
        c2 = data & filtered_ids
        end_time = int(round(time.time() * 1000))
        print(f'finish filter {end_time-begin_time} ms', flush=True)
        c2.save(args.outputfile)


if __name__ == "__main__":
    main()
