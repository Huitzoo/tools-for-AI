from miner import Miner
from pexels_api import API

from miners.utils.dirs_tools import generate_paths

class MinerPexeles(Miner):
    SERVICE = "pexeles"

    def __init__(self,env):
        super().__init__(env)

        self.find = env["class"]["name"]
        self.pages = env["class"]["numberOfPages"]
        self.number_of_images = env["class"]["numberOfImages"]
        
        self.api_key = env["apiKeys"]["pexeles"]

        self.save_path = generate_paths(
            env["pathSaved"],
            self.SERVICE,
            self.find
        )
        
        
    def start_mining(self):
        
        api = API(self.api_key)
        for i in range(0,self.pages):
            api.search(
                self.find, 
                page=i, 
                results_per_page=self.number_of_images
            )
            
            photos = api.get_entries()
            for photo in photos:
                self.download(
                    photo.large,
                    save_dir=self.save_path
                )