from Coach import Coach
from HoldHorsesGame import HoldHorsesGame as Game
from NNet import NNetWrapper as nn
from utils import *

args = dotdict({
    'generator_id': 'machine_1',
    'numIters': 100,
    'numEps': 5,
    'tempThreshold': 15,
    'updateThreshold': 0.5,
    'maxlenOfQueue': 200,
    'arenaCompare': 10,
    'numMCTSSims': 100,
    'cpuct': 1,
    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('C:\\Users\\phili\\PycharmProjects\\AlphaZeroLite', 'best.pth.tar'),
    'numItersForTrainExamplesHistory': 200,
})

if __name__ == "__main__" :
    g = Game()
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()
