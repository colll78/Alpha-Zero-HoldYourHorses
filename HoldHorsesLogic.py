import numpy as np
from collections import namedtuple

horseCoords = [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
appleCoords = (0, 0)
boardWidth = 7
boardHeight = 6

class Board():
    def __init__(self, board_height=boardWidth, board_width=boardHeight, np_pieces=None, player=1):
        self.game_over = False
        self.height = board_height or boardHeight
        self.width = board_width or boardWidth
        self.moves_remaining = 100
        self.winner = None
        self.player = player

        if np_pieces is not None:
            self.np_pieces = np_pieces
        else:
            self.np_pieces = np.zeros((boardWidth, boardHeight), dtype=int)
            self.np_pieces[appleCoords] = 2
            self.np_pieces[boardWidth - appleCoords[0] - 1, boardHeight - appleCoords[1] - 1] = -2

            for (x, y) in horseCoords:
                self.np_pieces[x, y] = 1
                self.np_pieces[boardWidth - x - 1, boardHeight - y - 1] = -1

    def with_np_pieces(self, np_pieces):
        if np_pieces is None:
            np_pieces = self.np_pieces
        return Board(self.height, self.width, np_pieces)

    def get_result(self):
        if  self.np_pieces[appleCoords] == 2 and self.np_pieces[boardWidth - appleCoords[0] - 1, boardHeight - appleCoords[1] - 1] != -2:
            self.game_over = True
            self.winner = 1
            # print("apple coords %s" % self.np_pieces[appleCoords])
            # print(self.np_pieces)
            # print("branch 0")
            return 1
        elif self.np_pieces[appleCoords] != 2 and self.np_pieces[boardWidth - appleCoords[0] - 1, boardHeight - appleCoords[1] - 1] == -2:
            self.game_over = True
            self.winner = -1
            #print('branch 1"')
            return -1
        elif self.np_pieces[boardWidth - appleCoords[0] - 1, boardHeight - appleCoords[1] - 1] == 2 and self.np_pieces[appleCoords] != -2:
            self.game_over = True
            self.winner = 1
            # print ("apple coords %s" % self.np_pieces[appleCoords])
            # print(self.np_pieces)
            # print("branch 2")
            return 1
        elif self.np_pieces[boardWidth - appleCoords[0] - 1, boardHeight - appleCoords[1] - 1] != 2 and self.np_pieces[appleCoords] == -2:
            self.game_over = True
            self.winner = -1
            #print("Branch 3")
            return -1
        elif self.moves_remaining <= 0:
            print("no moves")
            return 0.001
        return 0

    # def get_result(self):
    #     if self.game_over:
    #         if self.moves_remaining > 0:
    #             return self.winner
    #         else:
    #             return 0.001
    #     else:
    #         return False


    def get_legal_moves(self, color):
        direction = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1),
                     (-1, -2)]  # Possible (dx, dy) moves
        moves = []
        for xStart in range(self.width):  # Search board for player's pieces
            for yStart in range(self.height):
                if self.np_pieces[xStart, yStart] == color:  # Found a piece!
                    for (dx, dy) in direction:  # Check all potential move vectors
                        (xEnd, yEnd) = (xStart + dx, yStart + dy)
                        if xEnd >= 0 and xEnd < self.width and yEnd >= 0 and yEnd < self.height and not (
                                self.np_pieces[xEnd, yEnd] in [color, 2 * color]):
                            moves.append((xStart, yStart, xEnd,
                                          yEnd))  # If square is empty or occupied by the opponent, then we have a legal move.
        return moves

    def make_move(self, move, color):
        (xStart, yStart, xEnd, yEnd) = move
        self.np_pieces[xStart, yStart] = 0  # ... we remove the moving piece from its start position...
        self.np_pieces[xEnd, yEnd] = color  # ... and place it at the end position
        self.moves_remaining = self.moves_remaining - 1
        self.game_over = False
        self.winner = None
        self.curr_move = move
        self.player = -color
        #print(self.np_pieces)

        if self.np_pieces[xEnd, yEnd] == -2 * color or not (-color in self.np_pieces):
            self.game_over = True  # If the opponent lost the apple or all horses, the game is over...
            self.winner = color
        elif self.moves_remaining == 0:  # Otherwise, if there are no more moves left, the game is drawn
            self.game_over = True
            self.winner = 0

    def mirror(self):
        board = np.copy(self.np_pieces)
        mirrored_board = np.flip(np.flip(board, 1), 0)

        return Board(self.height, self.width, mirrored_board)
