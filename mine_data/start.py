import toml
from factory import FactoryMinner


config = toml.load("./configs/minersConf.toml")

miner = FactoryMinner().factory(config["miner"],config)
miner.start_mining()