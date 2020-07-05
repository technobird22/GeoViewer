import cv2

path = "NZ_area_test/"
img_name = "FD8_IMG_FD_125_IR105_20200704_210006.jpg"
img = cv2.imread(path + img_name, 1)

def parse_frame_name(input_name):
    # "FD8_IMG_FD_125_IR105_20200704_210006.jpg" to "125: 20200704 21:00:06" 
    # output_name = input_name[input_name.find("FD_"):].replace("FD_", "")
    output = input_name[:-6].split('_')

    num = output[3]
    date, time = output[5:7]

    # date = list(date)
    date = date[6:8] + "/" + date[4:6] + "/" + date[0:4]
    time = time[0:2] + ":" + time[2:5]

    output_name = output[3] + ": " + date + " @ " + time + " UTC"
    return (output_name, num)

def overlay_text(cur_frame):
    frame_time, frame_num = parse_name(cur_frame)

    print("[INFO] Overlaying text onto frame...")
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, "GK-2A Imagery", (20, 80), font, 5, (0, 255, 255), 5, cv2.LINE_AA)

    cv2.putText(img, "Animation", (20, 170), font, 6, (0, 165, 255), 5, cv2.LINE_AA)

    cv2.putText(img, "Time: ", (1650, 60), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(img, frame_time, (1580, 100), font, 3, (150, 150, 150), 3, cv2.LINE_AA)

    cv2.putText(img, "Processing: ", (20, 2120), font, 4, (255, 255, 255), 4, cv2.LINE_AA)

    cv2.putText(img, "Albert (Technobird22)", (20, 2180), font, 4, (0, 255, 0), 4, cv2.LINE_AA)

    cv2.putText(img, "Data size: 1.40 GB", (1710, 2078), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(img, "Frame count: 960 frames", (1540, 2128), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(img, "Data from: MouseBatteries", (1510, 2178), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

    cv2.putText(img, "Thanks :)", (2100, 2194), font, 1, (50, 50, 50), 1, cv2.LINE_AA)

print("-"*30)
print("---START---")

inp = "FD8_IMG_FD_125_IR105_20200704_210006.jpg"
print("Input name:", inp)
out = parse_frame_name(inp)[0]
print("Output name:", out)
num = parse_frame_name(inp)[1]
print("Frame number:", num)

print("---DONE---")
print("-"*30)
# Write final output image
cv2.imwrite(path + "text_" + img_name, img)