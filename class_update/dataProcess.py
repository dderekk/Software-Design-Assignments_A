import pandas as pd
from blockControl import Blocks

class dataProcess:

    def __init__(self):
        self.name = None
        self.score = None

    def featchNewScore(self):
        data = pd.read_csv('climate.csv')

        self.name= data['name'].tolist()
        self.score = data['score'].tolist()

    def getTop10Data(self):
        self.featchNewScore()
        zipped = list(zip(self.name, self.score))

        sorted_data = sorted(zipped, key=lambda x: x[1], reverse=True)  # 从大到小排序
        return(sorted_data[:10])

    def getBlockData(self,block):
        #return the block diagram as → [0,0,0,1...]
        return block.background
