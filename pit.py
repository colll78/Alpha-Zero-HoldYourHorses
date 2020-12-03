from MCTS import MCTS
from HoldHorsesGame import HoldHorsesGame
from NNet import NNetWrapper as NNet
import numpy as np
import Arena
from utils import *

boardWidth = 7
boardHeight = 6

class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a] != 1:
            a = np.random.randint(self.game.getActionSize())
        return a

def display(game, board, curPlayer):
    #print("display")
    print()
    print("Arena Game Display:")
    print("Current player: ", curPlayer)
    print(board.np_pieces)

g = HoldHorsesGame(7, 6)
random_player = RandomPlayer(g).play

nn_args = dotdict({'numMCTSSims': 15,
                   'cpuct':1.0})
neural_net = NNet(g)
neural_net.load_checkpoint(folder='C:\\Users\\phili\\PycharmProjects\\AlphaZeroLite\\src3\\temp\\', filename='temp.pth.ckpt')
mc_tree = MCTS(g, neural_net, nn_args)
neural_player = lambda x: np.argmax(mc_tree.getActionProb(x, temp=0))
arena = Arena.Arena(neural_player, random_player, g, display)
arena.playGames(2, verbose=True)



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