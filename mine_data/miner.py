from abc import ABC,abstractmethod
import requests
import os

try:
    from urlparse import urlparse
except ImportError:
    from six.moves.urllib.parse import urlparse


class Miner(ABC):
    def __init__(self,env):
        pass

    @abstractmethod
    def start_mining(self):
        raise NotImplementedError

    def download(self,data, save_dir = "./"):
        
        if not os.path.isdir(save_dir):
            os.mkdir(save_dir)

        if isinstance(data, str) or isinstance(data, bytes):
            res = requests.get(data)
            res.raise_for_status()
            outfile = save_dir + "/" + os.path.basename(urlparse(str(data)).path)
            outfile = outfile.replace("'","")
            playFile = open(outfile, 'wb')
            
            for chunk in res.iter_content(100000):
                playFile.write(chunk)
            playFile.close()

        elif isinstance(data, list):
            for i in data:
                self.download(i, save_dir)
        else:
            pass