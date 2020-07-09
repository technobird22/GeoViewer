import argparse
import cv2
from PIL import Image
from PIL import ImageFilter

sharpenAmount = 1

parser = argparse.ArgumentParser(description='Arguments')
parser.add_argument('input', metavar='i', type=str, help='What file(s) to apply sharpening to.')

args = parser.parse_args()

inputFile = (args.input)

image = cv2.imread(inputFile, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH | cv2.IMREAD_UNCHANGED)

image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=2)
semi_final = clahe.apply(image_bw)

_, ordinary_img = cv2.threshold(image_bw, 155, 255, cv2.THRESH_BINARY)

cv2.imwrite(f'{inputFile}-enhanced.png', semi_final)

sharpened = Image.open(f'{inputFile}-enhanced.png')

for i in range(sharpenAmount):
    sharpened = sharpened.filter(ImageFilter.SHARPEN)

sharpened.show()
