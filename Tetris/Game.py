from GUI.GameBoard import GameBoard
import numpy

# Game Loop:
# Collect input
# Update game state
# Alert GUI

class Game:
    def __init__(self):
        self.state = GameBoard() # TODO: Implement game board state

    def getState(self):
        return self.state

    # Adds piece to game board
    # Piece is array, x and y are where should go in board
    def addPiece(self, piece, x1, y1, x2, y2):
        # Check sizes
        if abs(x2 - x1) != len(piece) or abs(y2 - y1) != len(piece[0]):
            return False

        # TODO: add piece to game state, use array slicing
        return True

    def removePiece(self, piece, x1, y1, x2, y2):
        # Check sizes
        if abs(x2 - x1) != len(piece) or abs(y2 - y1) != len(piece[0]):
            return False

        # TODO: add zeroed piece to game state

    def rotatePiece(self, piece, direction):
        if direction == "left":
            numpy.rot90(piece)
        elif direction == "right":
            numpy.rot90(piece, k=-1)

    def shiftDownPiece(self, piece, x1, y1, x2, y2):
        if not self.removePiece(piece, x1, y1, x2, y2):
            return # TODO: Error message?

        if not self.addPiece(piece, x1, y1+1, x2, y2+1):
            return # TODO: Error message

    # Checks for full rows
    def updateGameBoard(self):
        self.state.remove_full_rows()
    

    