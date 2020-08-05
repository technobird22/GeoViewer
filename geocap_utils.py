"""Import libraries"""
import json
import cv2

def load_json(tmp_file_path):
    """Load a JSON file"""
    # load json file from file system
    print("[INFO] loading JSON file from '" + tmp_file_path + "'...")
    with open(tmp_file_path) as json_file:
        data = json.load(json_file)
    print("[OK] Successfully loaded JSON file from '" + tmp_file_path + "'!")

    return data

def clahe(in_img):
    """Perform CLAHE on an image"""
    print("[STATUS] Performing CLAHE on image...")

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

    print("[OK] Successfully performed CLAHE on the image.")
    return out_img

def parse_frame_name(input_name):
    """Parse frame name to get time and frame number"""
    print("[INFO] Parsing frame name '" + input_name + "'...")
    output = input_name[:-6].split('_')

    ####################################################
    # If file name contains "FD*_" at the front, enable:
    # output = output[1:]
    ####################################################

    frame_num = output[2]
    date, time = output[4:6]

    date = date[6:8] + "/" + date[4:6] + "/" + date[0:4]
    time = time[0:2] + ":" + time[2:5]

    output_name = date + " @ " + time + "UTC"
    return (output_name, frame_num)

def overlay_info(inp_img, frame_name):
    """Overlay information onto a frame"""
    print("[INFO] Overlaying text onto frame...")

    frame_time, frame_num = parse_frame_name(frame_name)

    font = cv2.FONT_HERSHEY_PLAIN

    # Big title
    cv2.putText(inp_img, "GK-2A Imagery", (20, 80), font, 5, (0, 255, 255), 5, cv2.LINE_AA)
    cv2.putText(inp_img, "Animation", (20, 170), font, 6, (0, 165, 255), 5, cv2.LINE_AA)

    # Capture time
    cv2.putText(inp_img, "Capture Time: ", (1720, 60), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(inp_img, frame_time, (1570, 110), font, 3, (150, 150, 150), 3, cv2.LINE_AA)

    # Frame number
    cv2.putText(inp_img, "Frame Number: ", (1690, 170), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(inp_img, frame_num, (2070, 230), font, 4, (150, 150, 150), 4, cv2.LINE_AA)

    # Credits
    cv2.putText(inp_img, "Processing: ", (10, 1970), font, 4, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(inp_img, "GeoCapture", (5, 2030), font, 5, (0, 165, 255), 6, cv2.LINE_AA)
    cv2.putText(inp_img, "By Albert (Technobird22)", (10, 2073), font, 2.5, (0, 255, 255), 3,\
         cv2.LINE_AA)
    cv2.putText(inp_img, "github.com/technobird22/geocapture", (10, 2105), font, 2,\
         (150, 150, 150), 2, cv2.LINE_AA)
    cv2.putText(inp_img, "PERSON RUNNING S/W", (20, 2180), font, 4, (0, 255, 0), 4, cv2.LINE_AA)

    # Load JSON for overlay data
    data_info = load_json("config/data.json")
    print("GOT DATA: ", data_info)
    print("DEBUG: ", str(round(data_info["data_size"], 2)))

    # Source data information
    cv2.putText(inp_img, "Data size: " + data_info["data_size"] + " GB",\
        (1650, 2078), font, 3, (150, 150, 150), 4, cv2.LINE_AA)
    cv2.putText(inp_img, "Frame count: " + data_info["frame_count"],\
        (1540, 2128), font, 3, (150, 150, 150), 4, cv2.LINE_AA)

    # cv2.putText(inp_img, "Data from: " + str(data_info["data_source"]), (1510, 2178), font, 3,\
    cv2.putText(inp_img, "Data from: " + data_info["data_source"], (1420, 2178), font, 3,\
        (150, 150, 150), 4, cv2.LINE_AA)
    # Shh... This line doesn't exist...
    cv2.putText(inp_img, "Easter Egg ;)", (2100, 2194), font, 1, (50, 50, 50), 1, cv2.LINE_AA)

    return inp_img

def test_overlay():
    """For testing the overlay code"""

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
    img = overlay_info(img, img_name)

    # Write final output image
    print("[INFO] Writing final output to image...")
    cv2.imwrite(path + "overlay_TEST_" + img_name, img)
    print("---DONE---")
    print("-"*30)

# ---FOR DEBUGGING:---
# test_overlay()

# Headers at the start of program
HEADER = """\
    ┌────────────────────────────────────────────────────────┐
    │                       GeoCapture                       │
    │  Automatic processing of geostationary satellite data  │
    │                      Version  1.0                      │
    ├────────────────────────────────────────────────────────┤
    │             Made by Albert  (Technobird22)             │
    ├────────────────────────────────────────────────────────┤
    │   GitHub: https://github.com/technobird22/geocapture   │
    └────────────────────────────────────────────────────────┘
"""
BASIC_HEADER = """\
    o--------------------------------------------------------o
    |                       GeoCapture                       |
    |  Automatic processing of geostationary satellite data  |
    |                      Version  1.0                      |
    o--------------------------------------------------------o
    |             Made by Albert  (Technobird22)             |
    o--------------------------------------------------------o
    |   GitHub: https://github.com/technobird22/geocapture   |
    o--------------------------------------------------------o
"""
VERY_BASIC_HEADER = """\
    --------------------------------------------------------
                           GeoCapture                       
      Automatic processing of geostationary satellite data  
                          Version  1.0                    
    --------------------------------------------------------
                 Made by Albert  (Technobird22)             
    --------------------------------------------------------
       GitHub: https://github.com/technobird22/geocapture   
    --------------------------------------------------------
"""