import os
import cv2
from copy import copy

from miner import Miner
from miners.utils.dirs_tools import generate_paths

class MinerVideos(Miner):
    SERVICE = "videos"

    def __init__(self,env):
        super().__init__(env)

        self.path_videos = env["videos"]["pathVideos"]

        self.saved_images_peer_frame = env["videos"]["savedImagesPeerFrame"]

        self.formats_videos = env["videos"]["formats"]

        self.save_path = env["pathSaved"]

    def start_mining(self):

        for video in os.listdir(self.path_videos):

            cant_support_format = False
            correct_format = ""
            
            for format in self.formats_videos:
                if format in video:
                    cant_support_format = False
                    correct_format = format
                    break
                else:
                    cant_support_format = True
            
            if cant_support_format:
                print("Can't support format.")
                continue

            capture = cv2.VideoCapture(self.path_videos+video)
            name_images = video.rstrip(correct_format)
            count = 0
            name = 0
            
            
            dir_path =  generate_paths(
                self.save_path,
                self.SERVICE,
                name_images
            )

            print(dir_path)
        
            while True:

                ret,frame = capture.read()
                
                if not ret:
                    break
                
                count += 1

                if count%self.saved_images_peer_frame == 0:
                    name += 1
                    cv2.imwrite(
                        f"{dir_path}{name_images}{name}.jpg",
                        frame
                    )    