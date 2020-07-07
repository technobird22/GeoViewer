import argparse
from PIL import Image
from PIL import ImageFilter

sharpenAmount = 2

parser = argparse.ArgumentParser(description='Arguments')
parser.add_argument('input', metavar='i', type=str, help='What file(s) to apply sharpening to.')

args = parser.parse_args()

sharpened = Image.open(f'{args.input}')

for i in range(sharpenAmount):
    sharpened = sharpened.filter(ImageFilter.SHARPEN)

sharpened.save('cat.png')
