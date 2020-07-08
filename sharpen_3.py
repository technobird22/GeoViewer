from PIL import Image
from PIL import ImageFilter

sharpenAmount = 2
output_header = "sharpened_"

inputs = ['test_fd.png']

for cur_file in inputs:
    try:
        sharpened = Image.open(f'{cur_file}')
    except:
        print("[ERROR] Image '" + cur_file + "' couldn't be opened! Cause: '" + str(sys.exc_info()[0]) + "'.\n\
        Skipping to next image...")
        continue

    for i in range(sharpenAmount):
        sharpened = sharpened.filter(ImageFilter.SHARPEN)

    sharpened.save(output_header + cur_file + '.png')
