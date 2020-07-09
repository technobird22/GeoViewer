import sys
import cv2

def clahe(in_img):
    return cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5)).apply(in_img)

def do_clahe_img(in_img):
    b_chn, g_chn, r_chn = cv2.split(in_img)
    return cv2.merge((clahe(b_chn), clahe(g_chn), clahe(r_chn)))

inputs = ["input.jpg"]

output = "clahe_"

cnt = 0.0

for img_path in inputs:
    print("[" + str(round(cnt/len(inputs)*100)) + "%] Performing CLAHE on: \"" + img_path + "\"")
    try:
        cnt += 1

        img = cv2.imread(img_path)
        out_img = do_clahe_img(img)

        cv2.imwrite(output + img_path, out_img)

    except:
        print("CRITICAL ERROR! Continuing to next file. Failed on image '" + img_path + "' \
            with message '" + str(sys.exc_info()[0]) + "';")

print("---DONE---")
