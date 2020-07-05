import cv2

path = "NZ_area_test/"
img_name = "FD8_IMG_FD_125_IR105_20200704_210006.jpg"
img = cv2.imread(path + img_name, 1)

text = "GK-2A Imagery"
font = cv2.FONT_HERSHEY_PLAIN
font_size = 5
font_weight = 5
colour = (0, 255, 255)
textsize = cv2.getTextSize(text, font, font_size, font_weight)[0]
coords = (20, 80)
cv2.putText(img, text, coords, font, font_size, colour, font_weight, cv2.LINE_AA)

text = "Animation"
font = cv2.FONT_HERSHEY_PLAIN
font_size = 6
font_weight = 5
colour = (0, 165, 255)
textsize = cv2.getTextSize(text, font, font_size, font_weight)[0]
coords = (20, 170)
cv2.putText(img, text, coords, font, font_size, colour, font_weight, cv2.LINE_AA)

text = "Current frame: "
font = cv2.FONT_HERSHEY_PLAIN
font_size = 4
font_weight = 4
colour = (0, 255, 255)
textsize = cv2.getTextSize(text, font, font_size, font_weight)[0]
# coords = textsize
coords = (1650, 60)
cv2.putText(img, text, coords, font, font_size, colour, font_weight, cv2.LINE_AA)

text = "Processing: "
font = cv2.FONT_HERSHEY_PLAIN
font_size = 4
font_weight = 4
colour = (255, 255, 255)
coords = (20, 2120)
cv2.putText(img, text, coords, font, font_size, colour, font_weight, cv2.LINE_AA)

text = "Albert (Technobird22)"
font = cv2.FONT_HERSHEY_PLAIN
font_size = 4
font_weight = 4
colour = (0, 255, 0)
textsize = cv2.getTextSize(text, font, font_size, font_weight)[0]
# coords = textsize
coords = (20, 2180)
cv2.putText(img, text, coords, font, font_size, colour, font_weight, cv2.LINE_AA)

text = "Data size: 1.40 GB"
font = cv2.FONT_HERSHEY_PLAIN
font_size = 3
font_weight = 4
colour = (100, 100, 100)
coords = (1710, 2078)
cv2.putText(img, text, coords, font, font_size, colour, font_weight, cv2.LINE_AA)

text = "Frame count: 960 frames"
font = cv2.FONT_HERSHEY_PLAIN
font_size = 3
font_weight = 4
colour = (100, 100, 100)
coords = (1540, 2128)
cv2.putText(img, text, coords, font, font_size, colour, font_weight, cv2.LINE_AA)

# Write final output image
cv2.imwrite(path + "text_" + img_name, img)