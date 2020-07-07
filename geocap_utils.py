# Import libraries
import cv2

# Parse frame name to get time and frame number
def parse_frame_name(input_name):
    print("[INFO] Parsing frame name '" + input_name + "'...")
    output = input_name[:-6].split('_')

    num = output[3]
    date, time = output[5:7]

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

    cv2.putText(inp_img, "Data size: " + str(round(data_size)) + " GB", (1710, 2078), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Frame count: " + str(frame_cnt) + " frames", (1540, 2128), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Data from: MouseBatteries", (1510, 2178), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(inp_img, "Thanks ;)", (2100, 2194), font, 1, (50, 50, 50), 1, cv2.LINE_AA)

    return(inp_img)

# For testing the overlay code
def test_overlay():
    path = "everything/"
    img_name = "FD0_IMG_FD_123_IR105_56783412_123400.jpg"
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
    cv2.imwrite(path + "text_" + img_name, img)
    print("---DONE---")
    print("-"*30)

# ---FOR DEBUGGING:---
#   test_overlay()