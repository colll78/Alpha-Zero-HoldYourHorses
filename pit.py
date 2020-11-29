from MCTS import MCTS
from HoldHorsesGame import HoldHorsesGame
from NNet import NNetWrapper as NNet
import numpy as np
from utils import *

boardWidth = 7
boardHeight = 6

def get_move(state):
    player = state.player
    board = state.board
    game = HoldHorsesGame(height=boardHeight, width=boardWidth, np_pieces=board)
    neural_net = NNet(game)
    neural_net.load_checkpoint("C:\\Users\\phili\\PycharmProjects\\AlphaZeroLite", 'best.pth.tar')
    args = dotdict({"numMCTSSims":200, 'cpuct':1.0})
    tree = MCTS(game)
    find_move = lambda x: np.argmax(tree.getActionProb(x,temp=0))
    action = find_move(self.game.getCanonicalForm(game._base_board, player))
    move = game._possible_moves[action]
    return move