import cv2
import glob
import numpy as np

imageArray = glob.glob('images/*.jpg')
frame = 0
eframe_array = []


for i in imageArray:
    print(f'Enhancing {i}...')
    image = cv2.imread(i) 
  
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
    clahe = cv2.createCLAHE(clipLimit = 5) 
    final_img = clahe.apply(image_bw)
  
    _, ordinary_img = cv2.threshold(image_bw, 155, 255, cv2.THRESH_BINARY) 
  
    cv2.imwrite(f'enhanced/{frame}-enhanced.jpg', final_img)

    eframe_array.append(f'enhanced/{frame}-enhanced.jpg')

    
    frame += 1


overlay = cv2.imread('falseColourGK.png')
frame = 0

for i in eframe_array:
    print(f'Overlaying {i}...')
    image = cv2.imread(i)
    overlayed = cv2.addWeighted(image,0.4,overlay,0.1,1)
    
    cv2.imwrite(f'enhanced/{frame}-enhanced.jpg', overlayed)
    frame += 1
    


video_array = []
for filename in eframe_array:
    print(f'MP4-ing {filename}...')
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    video_array.append(img)

out = cv2.VideoWriter('final/final.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
for i in range(len(video_array)):
    out.write(video_array[i])
    
out.release()
