from miner import Miner
import requests
from miners.utils.dirs_tools import generate_paths


class MinerPixabay(Miner):
    WEBSITE = "https://pixabay.com/api/"
    SERVICE = "pixabay"

    def __init__(self,env):
        super().__init__(env)
        
        self.find = env["class"]["name"]
        self.number_of_pages = env["class"]["numberOfPages"]
        self.number_of_images = env["class"]["numberOfImages"]
        self.api_key = env["apiKeys"]["pixabay"]
        
        self.save_path = generate_paths(
            env["pathSaved"],
            self.SERVICE,
            self.find
        )
        
    def start_mining(self):
        payload = {
            "key":self.api_key,
            "page": 0,
            "per_page": self.number_of_images,
            "q":self.find,
            "image_type":"photo"
        }
        for i in range(0,self.number_of_pages):
            payload["page"] = i 
            response = requests.get(self.WEBSITE,params=payload)
            print(response)
            if response.status_code == 200:
                results = response.json()["hits"]
                for result in results:
                    self.download(result["largeImageURL"],save_dir=self.save_path)
