from Coach import Coach
from HoldHorsesGame import HoldHorsesGame as Game
from NNet import NNetWrapper as nn
from utils import *
import sys
sys.setrecursionlimit(30000)

args = dotdict({
    'generator_id': 'machine_1',
    'numIters': 100,
    'numEps': 5,
    'tempThreshold': 15,
    'updateThreshold': 0.5,
    'maxlenOfQueue': 200,
    'arenaCompare': 3,
    #'numMCTSSims': 100,
    'numMCTSSims': 3,
    'cpuct': 1,
    'checkpoint': 'C:\\Users\\phili\\PycharmProjects\\AlphaZeroLite\\src3\\temp\\',
    'load_model': False,
    'load_folder_file': ('C:\\Users\\phili\\PycharmProjects\\AlphaZeroLite\\src3\\temp', 'best.pth.tar'),
    'numItersForTrainExamplesHistory': 200,
    #'numItersForTrainExamplesHistory': 20,
})

if __name__ == "__main__" :
    print((sys.getrecursionlimit()))
    g = Game()
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()
