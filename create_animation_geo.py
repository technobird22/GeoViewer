import os
import sys
import time
import numpy
import PIL
from PIL import Image
import cv2

import geocap_utils

# [STATUS] Execution finished. Total time elapsed: 124.5 seconds. Processed 844.0 frames. Calculation FPS: 0.1475.
# [STATUS] ---DONE---
frame_path = "everything/"
target_dir = "compilation"

output_header = "fast_" + frame_path[:-1] + "_"

first_img = 0

fps = 24

# Current directory name
dir_name = os.path.basename(os.getcwd())

# Prewrite checks
if(dir_name != target_dir):
    print("[WARNING] Working directory '" + dir_name + "' is not the target directory. Continue? [y/n]")
    choice = input()
    while(choice != 'y' and choice != 'n'):
        print("[ERROR] Invalid choice. Please try again. Options: 'y' or 'n'")
    if(choice != 'y'):
        print("[STATUS] Aborting...")
        exit()
else:
    print("[OK] Working directory is correct target directory")

if(os.path.isfile(output_header + dir_name + ".mp4")):
    print("[WARNING] Output file '" + (output_header + dir_name + ".mp4") + "' Already exists. Overwrite? [y/n]")
    # choice = input()
    choice = 'y'
    while(choice != 'y' and choice != 'n'):
        print("[ERROR] Invalid choice. Please try again. Options: 'y' or 'n'")
        choice = input()
    if(choice != 'y'):
        print("[STATUS] Aborting...")
        exit()
else:
    print("[OK] Output file '" + (output_header + dir_name + ".mp4") + "' does NOT exist.")
print("[STATUS] Safe to write file")

# print("[STATUS] Continuing...")

if(os.path.isdir(frame_path)):
    print("[OK] Found processed frames.")

    print("[STATUS] Loading processed frames...")
    inputs = os.listdir(frame_path)[first_img:-1]
    print("[OK] Successfully loaded processed frames")
    
    for img_path in inputs:
        print("[STATUS] Got image: '" + str(img_path) + "'.")

    print("[STATUS] Getting frame dimensions...")
    cur_img = frame_path + inputs[first_img]
    print("[STATUS] Loading image '" + cur_img + "'.")
    img = cv2.imread(cur_img)
    height, width, c = img.shape
    print("[OK] Got frame dimensions")

else:
    print("[ERROR] Processed frames not found")
    print("[STATUS] Please generate processed frames!")
    print("[STATUS] Aborting...")
    exit()

# Start processing
print("[STATUS] ---Begin Processing---")
start_time = time.time()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_header + dir_name + ".mp4", fourcc, fps, (round(width),round(height)))

cnt = 0.0
for img_name in inputs:
    img_path = frame_path + img_name
    print("[" + str(round(cnt/len(inputs)*100)) + "%] Processing frame: \"" + img_path + "\"")
    try:
        cnt += 1

        print("[STATUS] Loading image...")
        img = cv2.imread(img_path)
        # img = cv2.cvtColor(numpy.array(PIL.Image.open(img_path)), cv2.COLOR_RGB2BGR)
        print("[OK] Loaded image.")

        # Add overlay
        img = geocap_utils.overlay_info(img, img_name)

        # Write to video
        print("[STATUS] Writing to animation frame...")
        out.write(img)
        print("[OK] Successfully written image to frame")

    except:
        print("[ERROR] Failed on image '" + img_path + "' with message '" + str(sys.exc_info()[1]) + "'.")
        print("[STATUS] Aborting...")
        exit()

print("[STATUS] Releasing output stream")
try:
    out.release()
    print("[OK] Successfully released output stream")
except:
    print("[ERROR] Failed with message '" + str(sys.exc_info()[0]) + "'.\n")

elapsed = round(time.time() - start_time, 2)
cal_fps = cal_fps = round(elapsed/cnt, 4)

print("[STATUS] Execution finished. Total time elapsed: " + str(elapsed) + " seconds. Processed " + str(cnt) + " frames. Calculation FPS: " + str(cal_fps) + ".")
print("[STATUS] ---DONE---")