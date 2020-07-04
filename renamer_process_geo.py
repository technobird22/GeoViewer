import os
import sys
import time
# import numpy as np
import cv2

first_img = 2

inputs = os.listdir()[first_img:]
# inputs = ["IMG_FD_010_IR105_20200628_014006.jpg"]
target_dir = "FD"

# output = ""
output_directory = "raw_frames/"

height, width, c = cv2.imread(inputs[first_img]).shape
fps = 24

# Current directory name
dir_name = os.path.basename(os.getcwd())

output = dir_name

if(dir_name != target_dir):
    print("[WARNING] Working directory '" + dir_name + "' is not the target directory. Continue? [y/n]")
    # choice = input()
    choice = 'y'
    while(choice != 'y' and choice != 'n'):
        print("[ERROR] Invalid choice. Please try again. Options: 'y' or 'n'")
    if(choice != 'y'):
        print("[STATUS] Aborting...")
        exit()
else:
    print("[OK] Working directory is target directory...")

print("[STATUS] ---Begin Renaming---")
start_time = time.time()

if(os.path.isdir(output_directory)):
    print("[WARNING] Output directory '" + output_directory + "' Already exists. Overwrite? [y/n]")
    choice = input()
    while(choice != 'y' and choice != 'n'):
        print("[ERROR] Invalid choice. Please try again. Options: 'y' or 'n'")
        choice = input()
    if(choice != 'y'):
        print("[STATUS] Aborting...")
        exit()
else:
    print("[OK] No output directory found.")
    print("[STATUS] Creating output directory...")
    try:
        os.mkdir(output_directory)
    except OSError:
        print("[ERROR] Creation of the directory '" + output_directory + "' failed")
    else:
        print("[OK] Successfully created the directory '" + output_directory + "'.")

cnt = 0.0
for img_path in inputs:
    print("[" + str(round(cnt/len(inputs)*100)) + "%] Performing CLAHE on: \"" + img_path + "\"")
    try:
        cnt += 1

        print("[STATUS] Loading image...")
        img = cv2.imread(img_path)
        print("[OK] Loaded image.")
        
        # Write to new location
        print("[STATUS] Writing image...")
        cv2.imwrite(output_directory + output + "_" + img_path, img)
        print("[OK] Successfully written image")

        if((cnt - 1) % 100 == 0):
            elapsed = round(time.time() - start_time, 1)
            cal_fps = round(elapsed/cnt, 4)
            estimated = round(cal_fps * (len(inputs) - cnt), 1)

            print("[STATUS] Time elapsed: " + str(elapsed) + " seconds. Calculation FPS: " + str(cal_fps) + ". Estimated remaining time: " + str(estimated) + "seconds. Frame " + str(cnt) + " (" + str(round((float(cnt)/len(inputs))*100)) + "%)")

            # Pause for CPU cooloff
            if(cnt >= 100):
                print("[STATUS] Pausing 1 second for CPU cooloff...")
                time.sleep(1)
    except:
        print("[ERROR] Failed on image '" + img_path + "' with message '" + str(sys.exc_info()[1]) + "'.")
        print("[STATUS] Aborting...")
        exit()

elapsed = round(time.time() - start_time, 1)
cal_fps = round(cnt/elapsed, 4)
estimated = round(cal_fps * (len(inputs) - cnt), 1)
print("[STATUS] Execution finished. Total time elapsed: " + str(elapsed) + " seconds. Processed " + str(cnt) + " frames. Calculation FPS: " + str(cal_fps) + ".")
print("[STATUS] ---DONE---")