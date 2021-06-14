#Chace objects in a range of colors


import cv2
import os
import numpy as np
from copy import deepcopy
path = "./dataset/u/"

colors = [
    (218, 247, 166),
    (232, 255, 0),
    (255, 89, 0),
    (16, 229, 74),
    (200, 229, 16),
    (167, 16, 229),
    (16, 135, 229 ),
    (70, 194, 178),
    (212, 228, 13),
    (246, 0, 0),
    (117, 110, 98),
]

for file in os.listdir(path):
    print(file)
    if ".jpg" in file: 
        img_path = path+file
        txt_path = img_path.replace(".jpg",".txt")

        img = cv2.imread(img_path)        
        count = 0

        with open(txt_path,"r") as f:
            lines = f.readlines()
            dh, dw, _ = img.shape
            aux = deepcopy(img)

            x, y, w, h = [float(element) for element in lines[0].replace("\n","").split(" ")[1:]]

            l = int((x - w / 2) * dw)
            r = int((x + w / 2) * dw)
            t = int((y - h / 2) * dh)
            b = int((y + h / 2) * dh)
            if l < 0:
                l = 0
            if r > dw - 1:
                r = dw - 1
            if t < 0:
                t = 0
            if b > dh - 1:
                b = dh - 1
            
            cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)

            crop_img = img[t:b, l:r]

            brown_lo=np.array([6,6,6])
            brown_hi=np.array([35,35,35])

            
            mask=cv2.inRange(crop_img,brown_lo,brown_hi)
            
            for color in colors:
                crop_img = deepcopy(crop_img)
                crop_img[mask>0]=color
                
                aux[t:b,l:r] = crop_img

                #cv2.imshow("cropped", aux)
                #cv2.waitKey(0)
                
                img_path_aux = img_path.replace(".jpg","_img{0}.jpg".format(count))
                
                cv2.imwrite(
                    img_path_aux,aux
                )
                with open(txt_path.replace(".txt","_img{0}.txt".format(count)),"w") as f:
                    f.writelines(lines)
                count += 1
                