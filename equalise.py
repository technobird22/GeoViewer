import os
import sys
import numpy as np
import cv2

def clahe(in_img):
    return cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5)).apply(in_img)

def do_clahe_img(img):
    b_chn, g_chn, r_chn = cv2.split(img)
    return cv2.merge((clahe(b_chn), clahe(g_chn), clahe(r_chn)))

# if(len(sys.argv) == 1):
#     print("Error: No input files")
#     exit()

# inputs = sys.argv[1:]
inputs = os.listdir()
# inputs = ["IMG_4379.jpg"]

output = "clahe/"
# output = "clahe_"

cnt = 0.0

for img_path in inputs:
    print("[" + str(round(cnt/len(inputs)*100)) + "%] Performing CLAHE on: \"" + img_path + "\"")
    try:
        cnt += 1
        
        img = cv2.imread(img_path)
        out_img = do_clahe_img(img)

        # cv2.imwrite(img_path, out_img)
        # cv2.imwrite("chain_" + img_path, out_img)
        cv2.imwrite(output + img_path, out_img)
    except:
        print("CRITICAL ERROR! Continuing to next file. Failed on image '" + img_path + "' with message '" + str(sys.exc_info()[0]) + "';")

print("---DONE---")