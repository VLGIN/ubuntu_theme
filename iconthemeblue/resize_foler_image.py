import argparse
from PIL import Image
import PIL
import os

ap = argparse.ArgumentParser()

ap.add_argument('-s', '--source', required=True,
                help="source directory")

ap.add_argument('-d', '--destination', required=True,
                help="destination directory")

ap.add_argument('-sh', '--shape', required=True,
                help="shape of image")


args = ap.parse_args()


if __name__ == "__main__":
    list_dir = os.listdir(args.source)
    shape = int(args.shape)
    for item in list_dir:
        image = Image.open(args.source + "/" + item)
        resized_image = image.resize((shape, shape))
        resized_image.save(args.destination + "/" + item)