# Import libraries
import cv2

# Perform CLAHE on an image
def clahe(in_img):
    clip_limit = 2.0
    grid_size = (2, 2)

    print("[STATUS] Converting image to grayscale...")
    out_img = cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)
    print("[OK] Successfully converted to a grayscale image.")

    print("[STATUS] Performing CLAHE with clip limit " + str(clip_limit) + " and grid size "\
         + str(grid_size) + ".")
    out_img = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size).apply(out_img)
    print("[OK] Successfully performed CLAHE on the image.")

    print("[STATUS] Converting image to colour...")
    out_img = cv2.cvtColor(out_img, cv2.COLOR_GRAY2BGR)
    print("[OK] Successfully converted to a colour image.")

    return out_img

# Parse frame name to get time and frame number
def parse_frame_name(input_name):

    print("[INFO] Parsing frame name '" + input_name + "'...")
    output = input_name[:-6].split('_')

    ####################################################
    # If file name contains "FD*_" at the front, enable:
    # output = output[1:]
    ####################################################

    num = output[2]
    date, time = output[4:6]

    date = date[6:8] + "/" + date[4:6] + "/" + date[0:4]
    time = time[0:2] + ":" + time[2:5]

    output_name = date + " @ " + time + "UTC"
    return (output_name, num)

# Overlay information onto a frame
def overlay_info(inp_img, frame_name, data_size, frame_cnt):
    print("[INFO] Overlaying text onto frame...")

    frame_time, frame_num = parse_frame_name(frame_name)

    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(inp_img, "GK-2A Imagery", (20, 80), font, 5, (0, 255, 255), 5, cv2.LINE_AA)

    cv2.putText(inp_img, "Animation", (20, 170), font, 6, (0, 165, 255), 5, cv2.LINE_AA)

    cv2.putText(inp_img, "Capture Time: ", (1720, 60), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(inp_img, frame_time, (1570, 110), font, 3, (150, 150, 150), 3, cv2.LINE_AA)

    cv2.putText(inp_img, "Frame Number: ", (1690, 180), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(inp_img, frame_num, (2070, 240), font, 4, (150, 150, 150), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Processing: ", (20, 2120), font, 4, (255, 255, 255), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Albert (Technobird22)", (20, 2180), font, 4, (0, 255, 0), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Data size: " + str(round(data_size, 2)) + " GB", (1710, 2078), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Frame count: " + str(frame_cnt) + " frames", (1540, 2128), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Data from: MouseBatteries", (1510, 2178), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Thanks ;)", (2100, 2194), font, 1, (50, 50, 50), 1, cv2.LINE_AA)

    return inp_img

# For testing the overlay code
def test_overlay():
    path = "everything/"
    img_name = "FD8_IMG_FD_001_IR105_20200704_001006.jpg"
    img = cv2.imread(path + img_name, 1)

    print("-"*30)
    print("---START---")

    print("Input name:", img_name)
    out = parse_frame_name(img_name)[0]
    print("Output time:", out)
    num = parse_frame_name(img_name)[1]
    print("Frame number:", num)

    # Apply overlay
    print("[INFO] Applying overlay to image...")
    img = overlay_info(img, img_name, 1.2345678, 123)

    # Write final output image
    print("[INFO] Writing final output to image...")
    cv2.imwrite(path + "overlay_TEST_" + img_name, img)
    print("---DONE---")
    print("-"*30)

# ---FOR DEBUGGING:---
# test_overlay()
