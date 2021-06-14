from miner import Miner
import requests
from miners.utils.dirs_tools import generate_paths

class MinerUnplash(Miner):
    WEBSITE = "https://www.unsplash.com/napi/search/photos?query="
    SERVICE = "unplash"

    def __init__(self,env):
        super().__init__(env)
        self.name = env["class"]["name"]
        
        self.find = env["class"]["find"]
        self.pages = env["class"]["numberOfPages"]
        self.size_image = env["img"]["sizeImage"]

        self.save_path = generate_paths(
            env["pathSaved"],
            self.SERVICE,
            self.find
        )
        
        self.url = f"{self.WEBSITE}{self.find}&per_page=50&page={0}&xp=feedback-loop-v2%3Aexperiment"
        
    def start_mining(self):
        
    
        for page in range(0,self.pages):
            session = requests.Session()
            search_url = self.url.format(page)
            response = session.get(search_url)
            
            if response.status_code == 200 :
                results = response.json()['results']

                for result in results:
                    if self.size_image in result['urls']:                    
                        self.download(result['urls'][self.size_image],save_dir=self.save_path)

                    else:
                        self.download(result['urls']["raw"],save_dir=self.save_path)
