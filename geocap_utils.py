# Import libraries
import cv2

# Parse frame name to get time and frame number
def parse_frame_name(input_name):
    output = input_name[:-6].split('_')

    num = output[3]
    date, time = output[5:7]

    date = date[6:8] + "/" + date[4:6] + "/" + date[0:4]
    time = time[0:2] + ":" + time[2:5]

    output_name = date + " @ " + time + "UTC"
    return (output_name, num)

# Overlay information onto a frame
def overlay_info(inp_img, frame_name):
    print("[INFO] Overlaying text onto frame...")

    frame_time, frame_num = parse_frame_name(frame_name)

    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, "GK-2A Imagery", (20, 80), font, 5, (0, 255, 255), 5, cv2.LINE_AA)

    cv2.putText(img, "Animation", (20, 170), font, 6, (0, 165, 255), 5, cv2.LINE_AA)

    cv2.putText(img, "Capture Time: ", (1720, 60), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(img, frame_time, (1570, 110), font, 3, (150, 150, 150), 3, cv2.LINE_AA)

    cv2.putText(img, "Frame Number: ", (1690, 180), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(img, frame_num, (2070, 240), font, 4, (150, 150, 150), 4, cv2.LINE_AA)

    cv2.putText(img, "Processing: ", (20, 2120), font, 4, (255, 255, 255), 4, cv2.LINE_AA)

    cv2.putText(img, "Albert (Technobird22)", (20, 2180), font, 4, (0, 255, 0), 4, cv2.LINE_AA)

    cv2.putText(img, "Data size: 1.40 GB", (1710, 2078), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(img, "Frame count: 960 frames", (1540, 2128), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(img, "Data from: MouseBatteries", (1510, 2178), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(img, "Thanks :)", (2100, 2194), font, 1, (50, 50, 50), 1, cv2.LINE_AA)

    return(img)

# For testing the overlay code
def test_overlay():
    path = "NZ_area_test/"
    img_name = "FD8_IMG_FD_125_IR105_20200704_210006.jpg"
    img = cv2.imread(path + img_name, 1)

    print("-"*30)
    print("---START---")

    print("Input name:", img_name)
    out = parse_frame_name(img_name)[0]
    print("Output time:", out)
    num = parse_frame_name(img_name)[1]
    print("Frame number:", num)

    img = overlay_text(img, img_name)

    print("---DONE---")
    print("-"*30)

    # Write final output image
    cv2.imwrite(path + "text_" + img_name, img)