from miner import Miner
from miners.utils.dirs_tools import generate_paths
import os
from miners.utils.utils_pinterest import Pinterest_Helper

class MinerPinterest(Miner):
    SERVICE = "pinterest"

    def __init__(self,env):
        super().__init__(env)

        self.url = env["pinterest"]["url"]["name"]
        
        self.email = env["pinterest"]["userPinterest"]["email"]
        self.password = env["pinterest"]["userPinterest"]["pass"]
        self.find = env["class"]["name"]

        self.save_path = generate_paths(
            env["pathSaved"],
            self.SERVICE,
            self.find
        )
        
    def start_mining(self):

        ph = Pinterest_Helper(
            self.email,self.password
        )

        images = ph.runme(self.url)

        print(" Start download ...")
        
        
        if not os.path.isdir(self.save_path):
            print("Create folder for class: ",self.find)
            os.mkdir(self.save_path)

        self.download(images, self.save_path)
        print(" End, check your folder: ",self.save_path)
