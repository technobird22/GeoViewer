from PIL import Image
from PIL import ImageFilter

sharpenAmount = 2
output_header = "sharpened_"

for cur_file in inputs:
    sharpened = Image.open(f'{cur_file}')

    for i in range(sharpenAmount):
        sharpened = sharpened.filter(ImageFilter.SHARPEN)

    sharpened.save(output_header + cur_file + '.png')
