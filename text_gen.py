import cv2

text = "WARNING!"

path = "NZ_area_test/"
img_name = "FD8_IMG_FD_125_IR105_20200704_210006.jpg"
img = cv2.imread(path + img_name, 1)

font = cv2.FONT_HERSHEY_PLAIN

cv2.putText(img, "GK-2A Imagery", (20, 80), font, 5, (0, 255, 255), 5, cv2.LINE_AA)

cv2.putText(img, "Animation", (20, 170), font, 6, (0, 165, 255), 5, cv2.LINE_AA)

cv2.putText(img, "Current frame: ", (1650, 60), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
cv2.putText(img, "128: 20200704 21:30:06", (1580, 100), font, 3, (150, 150, 150), 3, cv2.LINE_AA)

cv2.putText(img, "Processing: ", (20, 2120), font, 4, (255, 255, 255), 4, cv2.LINE_AA)

cv2.putText(img, "Albert (Technobird22)", (20, 2180), font, 4, (0, 255, 0), 4, cv2.LINE_AA)

cv2.putText(img, "Data size: 1.40 GB", (1710, 2078), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

cv2.putText(img, "Frame count: 960 frames", (1540, 2128), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

cv2.putText(img, "Data from: MouseBatteries", (1510, 2178), font, 3, (100, 100, 100), 4, cv2.LINE_AA)

cv2.putText(img, "Thanks :)", (2100, 2194), font, 1, (50, 50, 50), 1, cv2.LINE_AA)

print("-"*30)
print("---DONE---")
# Write final output image
cv2.imwrite(path + "text_" + img_name, img)