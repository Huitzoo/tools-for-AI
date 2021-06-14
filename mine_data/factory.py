from miners.videos import MinerVideos
from miners.google import MinerGoogle
from miners.unplash import MinerUnplash
from miners.pexeles import MinerPexeles
from miners.pixabay import MinerPixabay
from miners.pinterest import MinerPinterest

from miner import Miner

class FactoryMinner():
    def factory(self,miner,env) -> Miner:
        if miner == "google":
            return MinerGoogle(env)
        if miner == "unplash":
            return MinerUnplash(env)
        if miner == "pexeles":
            return MinerPexeles(env)
        if miner == "pixabay":
            return MinerPixabay(env)
        if miner == "pinterest":
            return MinerPinterest(env)
        if miner == "videos":
            return MinerVideos(env)
        else:
            raise Exception("Miner doesn't support")


