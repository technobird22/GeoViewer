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
# Write final output image
cv2.imwrite(path + "text_" + img_name, img)