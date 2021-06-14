import os
from sys import argv

import numpy as np
import toml
import cv2 


def filter1(file:np.array,classe_dont_want:str)-> bool:
    """[summary]
    Give me all data of one data, and try to that other data only have 0 objects in the image
    """
    
    if classe_dont_want in file[:,0] or "4" in file[:,0]:
        return True
    return False

def filter2(file:np.array):
    if file.shape[1] == 1280 and file.shape[0] ==720:
        return True
    return False

def check_filter(file:np.array,filter:int,file_name:str) -> bool:
    if filter == 1:
        return filter1(file[:,0:1],"2")
    elif filter == 2:
        file_name = file_name.rstrip(".txt").replace("labels","images") + ".jpg"
        print(file_name)
        img = cv2.imread(file_name)
        return filter2(img)

def read_and_filter_file(env:dict):
    paths = env["paths"]
    
    if not os.path.isdir(paths["PATH_FILTER_LABELS"]):
        os.mkdir(paths["PATH_FILTER_LABELS"])
    if not os.path.isdir(paths["PATH_FILTER_IMAGES"]):
        os.mkdir(paths["PATH_FILTER_IMAGES"])

    labels_path = paths["PATH_LABELS"]
    images_path = paths["PATH_IMAGES"]
    label_filter_path = paths["PATH_FILTER_LABELS"]
    images_filter_path = paths["PATH_FILTER_IMAGES"]
    count = 0

    for file_sys in os.listdir(labels_path):
        file_name = labels_path+file_sys
        with open(file_name,"r") as file:
            lines = np.array([line.rstrip("\n").split(" ") for line in file.readlines()])
            
            if lines.shape[0] == 0:
                continue

            if check_filter(lines,env["filter"],file_name):
                os.rename(file_name,label_filter_path+file_sys)
                file_sys = file_sys.rstrip(".txt")
                file_sys += ".jpg"
                os.rename(images_path+file_sys,images_filter_path+file_sys)
                count += 1
        
def complete_paths(env:dict,project:str) -> dict:
    paths = {}
    for key_path,path in env["paths"].items():
        paths[key_path] = path.format(project)
    env["paths"] = paths

    return env

if __name__ == "__main__":
    env = toml.load("./filter.toml")
    project = argv[1]
    env = complete_paths(env,project)
    read_and_filter_file(env)
