import requests
try:
    from urlparse import urlparse
except ImportError:
    from six.moves.urllib.parse import urlparse

import os
import json 
import time
import shutil

def clean_image_that_dont_have_coords():
    path = "./dataset/img/"
    count = 1
    for folder in os.listdir(path):
        for txt in os.listdir(path+folder):
            if ".txt" in txt:
                name_file = path+folder+"/"+txt
                with open(name_file,"r") as f:
                    if len(f.readlines()) == 0:
                        os.remove(name_file)
                        name_file = name_file.replace("txt","jpg")
                        os.remove(name_file)
                        print("Image delete: ",count," ",name_file)
                        count += 1

def clean_images_without_labels():
    path = "./dataset/img/"
    for folder in os.listdir(path):
        current_folder = path+folder
        for jpg in os.listdir(current_folder):
            if ".jpg" in jpg:
                name_image = current_folder+"/"+jpg
                if not os.path.isfile(name_image.replace("jpg","txt")):
                    os.remove(name_image)
                    print("Delete: ",name_image)

def move_data():
    path = "./dataset/img/"
    move_images = "./dataset/images"
    move_labes = "./dataset/labels"


    for folder in os.listdir(path):
        
        for file_name in os.listdir(path+folder):
            if file_name == "images_list.txt":
                continue
            
            path_file = path+folder+"/"+file_name

            if ".txt" in path_file:
                shutil.move(path_file, move_labes)
            else:
                shutil.move(path_file, move_images)



def how_images_of_classes_have():
    path = "./dataset/img/"
    classses_dict = {
        "0":0,
        "1":0,
        "2":0,
        "3":0
    }
    for folder in os.listdir(path):
        for txt in os.listdir(path+folder):
            if ".txt" in txt:
                name_file = path+folder+"/"+txt
                with open(name_file,"r") as f:
                    for lines in f.readlines():
                        classes = str(lines.replace("\n","")[0])
                        if not "/" in classes:
                            classses_dict[classes] += 1
    
    print(classses_dict)


def move_data_t():
    move_images = "./dataset/montes/filterData/t/"
    move_labels = "./dataset/montes/filterData/t_labels/"
    labels = "./dataset/montes/filterData/labels/"
              
    for img in os.listdir(move_images):
        txt = img.replace(".jpg",".txt")

        path_file = labels+txt
        print(path_file)
        shutil.move(path_file,move_labels)
        

#clean_image_that_dont_have_coords()
#clean_images_without_labels()
#how_images_of_classes_have()
move_data_t()