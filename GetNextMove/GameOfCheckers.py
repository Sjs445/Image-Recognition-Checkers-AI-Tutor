from .games import *
# from games import *
import numpy as np

class GameOfCheckers(Game):
    def __init__(self, board=None):
        """Initialize the GameState"""
        self.initial = GameState(to_move='R', utility=0, board=board, moves = self.get_moves_for_player(board, to_move='R'))
 
    def actions(self, state: GameState):
        """Return a dictionary of the allowable moves at this point."""
        return(self.get_moves_for_player(state.board, state.to_move))
        

    def get_moves_for_player(self, board, to_move):
        """Takes in board and player and returns all possible moves for the given player"""

        valid_moves = {}

        if to_move == 'R':
            for rowIndex in range(len(board)):
                for colIndex in range(len(board)):
                    #   If we find a red piece in the board
                    if board[rowIndex][colIndex] == 'R':
                        #   Add the piece's position to the dictionary of valid moves
                        piecePosition = str(rowIndex)+','+str(colIndex)
                        valid_moves[piecePosition] = []

                        #   If we are on the left side of the board
                        if colIndex == 0:
                            #   Only check for values diagonal to the right
                            #   If there is an empty space
                            if rowIndex-1 >= 0:

                                if board[rowIndex-1][colIndex+1] == '0':
                                    #   Append the move to the dictionary of valid moves for that piece
                                    spaceToMove = str(rowIndex-1)+str(',')+str(colIndex+1)
                                    valid_moves[piecePosition].append(spaceToMove)
                                elif board[rowIndex-1][colIndex+1] == 'B':
                                    #   If the space diagonal to the right is a White piece
                                    #   Check if there is a piece behind it
                                    if rowIndex-2 >= 0:
                                        if board[rowIndex-2][colIndex+2] == '0':
                                            spaceToMove = str(rowIndex-2)+str(',')+str(colIndex+2)
                                            valid_moves[piecePosition].append(spaceToMove)
                        #   If we are on the right side of the board
                        elif colIndex == 7:
                            #   Only check for values diagonal to the left
                            #   If there is an empty space
                            if rowIndex-1 >=0:

                                if board[rowIndex-1][colIndex-1] == '0':
                                    #   Append the move to the dictionary of valid moves for that piece
                                    spaceToMove = str(rowIndex-1)+str(',')+str(colIndex-1)
                                    valid_moves[piecePosition].append(spaceToMove)
                                elif board[rowIndex-1][colIndex-1] == 'B':
                                    #   If the space diagonal to the left is a White piece
                                    #   Check if there is a piece behind it
                                    if rowIndex-2 >= 0:

                                        if board[rowIndex-2][colIndex-2] == '0':
                                            spaceToMove = str(rowIndex-2)+str(',')+str(colIndex-2)
                                            valid_moves[piecePosition].append(spaceToMove)
                        #   If we are in the middle of the board
                        elif rowIndex-1 >=0:
                            #   Check for values diagonal to the left and right

                            #   Checking right

                            if board[rowIndex-1][colIndex+1] == '0':
                                    #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(rowIndex-1)+str(',')+str(colIndex+1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex-1][colIndex+1] == 'B':
                                    #   If the space diagonal to the right is a White piece
                                    #   Check if there is a piece behind it
                                if rowIndex-2>=0 and colIndex+2 <= 7:
                                            
                                    if board[rowIndex-2][colIndex+2] == '0':
                                        spaceToMove = str(rowIndex-2)+str(',')+str(colIndex+2)
                                        valid_moves[piecePosition].append(spaceToMove)
                            
                            #   Checking left
                            if board[rowIndex-1][colIndex-1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(rowIndex-1)+str(',')+str(colIndex-1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex-1][colIndex-1] == 'B':
                                #   If the space diagonal to the left is a White piece
                                #   Check if there is a piece behind it
                                if rowIndex-2 >= 0 and colIndex-2 >= 0:
                                    if board[rowIndex-2][colIndex-2] == '0':
                                        spaceToMove = str(rowIndex-2)+str(',')+str(colIndex-2)
                                        valid_moves[piecePosition].append(spaceToMove)
        elif to_move == 'B':
            for rowIndex in range(len(board)):
                for colIndex in range(len(board)):
                    #   If we find a red piece in the board
                    if board[rowIndex][colIndex] == 'B':
                        #   Add the piece's position to the dictionary of valid moves
                        piecePosition = str(rowIndex)+','+str(colIndex)
                        valid_moves[piecePosition] = []

                        #   If we are on the left side of the board
                        if colIndex == 0 and rowIndex+1 <= 7:
                            #   Only check for values diagonal to the right
                            #   If there is an empty space
                            if board[rowIndex+1][colIndex+1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(rowIndex+1)+str(',')+str(colIndex+1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex+1][colIndex+1] == 'R':
                                #   If the space diagonal to the right is a red piece
                                #   Check if there is a piece behind it
                                if board[rowIndex+2][colIndex+2] == '0':
                                    spaceToMove = str(rowIndex+2)+str(',')+str(colIndex+2)
                                    valid_moves[piecePosition].append(spaceToMove)
                        #   If we are on the right side of the board
                        elif colIndex == 7 and rowIndex+1 <= 7:
                            #   Only check for values diagonal to the left
                            #   If there is an empty space
                            if board[rowIndex+1][colIndex-1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(rowIndex+1)+str(',')+str(colIndex-1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex+1][colIndex-1] == 'R':
                                #   If the space diagonal to the left is a White piece
                                #   Check if there is a piece behind it
                                if rowIndex+2 <= 7:
                                    if board[rowIndex+2][colIndex-2] == '0':
                                        spaceToMove = str(rowIndex+2)+str(',')+str(colIndex-2)
                                        valid_moves[piecePosition].append(spaceToMove)
                        #   If we are in the middle of the board
                        elif rowIndex+1 <= 7:
                            #   Check for values diagonal to the left and right

                            #   Checking left
                            if board[rowIndex+1][colIndex+1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(rowIndex+1)+str(',')+str(colIndex+1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex+1][colIndex+1] == 'R':
                                #   If the space diagonal to the right is a White piece
                                #   Check if there is a piece behind it
                                if rowIndex+2 <= 7 and colIndex+2 <=7:
                                    if board[rowIndex+2][colIndex+2] == '0':
                                        spaceToMove = str(rowIndex+2)+str(',')+str(colIndex+2)
                                        valid_moves[piecePosition].append(spaceToMove)
                            
                            #   Checking left
                            if board[rowIndex+1][colIndex-1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(rowIndex+1)+str(',')+str(colIndex-1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex+1][colIndex-1] == 'R':
                                #   If the space diagonal to the left is a White piece
                                #   Check if there is a piece behind it
                                if colIndex-2 >= 0 and rowIndex+2 <= 7:
                                    if board[rowIndex+2][colIndex-2] == '0':
                                        spaceToMove = str(rowIndex+2)+str(',')+str(colIndex-2)
                                        valid_moves[piecePosition].append(spaceToMove)
        # print("Valid moves for "+to_move)
        # print(valid_moves)
        return(valid_moves)
 
    def result(self, state: GameState, move):
        """Return the state that results from making a move from a state.
            A valid move example is `2,3 3,4`
            where 2,3 is the position of the piece and 3,4 is the position is going to """

        piece = move[:3]    # Original Piece location
        boardLocation = move[4:]    # Where the piece is being moved to

        if piece not in state.moves: # Check if piece is in moves
            return state 
        if boardLocation not in state.moves[piece]: # check if move is in moves
            return state    # If neither exist, move has no effect

        # Make copy of 2D array board
        board = list(map(list, state.board))

        # Move piece to desired location and update previous location to '0'
        board[int(boardLocation[0])][int(boardLocation[2])] = state.to_move
        board[int(piece[0])][int(piece[2])] = '0'

        # Update board if it takes other players chip
        # If the row piece minus the row it is going to move is 2 or -2
        # we know there is a jump. Need to set that piece being taken as '0'
        if state.to_move == 'B':
            # If the rows subtracted together is 2 then we have a jump
            if int(boardLocation[0])-int(piece[0]) == 2:
                if int(boardLocation[2])-int(piece[2]) == -2:
                    board[int(boardLocation[0])-1][int(boardLocation[2])+1] = '0'
            elif int(boardLocation[2])-int(piece[2]) == 2:
                board[int(boardLocation[0])-1][int(boardLocation[2])-1] = '0'
        elif state.to_move == 'R':
            # If the rows subtracted together is -2 then we have a jump
            if int(boardLocation[0])-int(piece[0]) == -2:
            # If the column of the jump location - the column of the original location is 2 we are jumping diagonally right
                if int(boardLocation[2])-int(piece[2]) == 2:
                    board[int(boardLocation[0])+1][int(boardLocation[2])-1] = '0'
                elif int(boardLocation[2])-int(piece[2]) == -2:
                    board[int(boardLocation[0])+1][int(boardLocation[2])+1] = '0'

        # Make a copy of the moves and remove the move
        moves = state.moves
        moves[piece].remove(boardLocation)

        # Debugging
        # print("Board after move "+str(move))
        # print(np.matrix(board))
        # input()

        to_move_old = state.to_move
        to_move = ('B' if state.to_move == 'R' else 'R')
        
        return GameState(to_move = to_move, utility = self.compute_utility(board, state.to_move, self.get_moves_for_player(board, to_move_old)), 
                         board = board, moves = self.get_moves_for_player(board, to_move))
        
    def compute_utility(self, board, player, moves):
        # If there are still moves left
        for pieces in moves:
            if len(moves[pieces]) > 0:
                return 0

        # Check who has the most game pieces left
        redGamePieces = self.compute_piece_count(board, 'R')
        whiteGamePieces = self.compute_piece_count(board, 'B')

        
        if redGamePieces > whiteGamePieces:
            return +1
        elif whiteGamePieces > redGamePieces:
            return -1
        else:
            return 0

    def compute_piece_count(self, board, player):
        pieceCount = 0

        for rows in board:
            for piece in rows:
                if player == piece:
                    pieceCount+=1
        return(pieceCount)

    def utility(self, state: GameState, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'R' else -state.utility
 
    def terminal_test(self, state: GameState):
        """Return True if there are no more moves left or utility value is 1/-1"""
        if state.utility != 0:
            return True

        for pieces in state.moves:
            if len(state.moves[pieces]) != 0:
                return False

        return True
    
    def display(self, state):
        """Print or otherwise display the state."""
        print("Board: ")
        print(np.matrix(state.board))
    
    def play_game(self, *players):
        """Play an n-person, move-alternating game."""
        state = self.initial
        while True:
            for player in players:
                self.display(state)
                move = player(self, state)
                print(move)
                state = self.result(state, move)
                if self.terminal_test(state):
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))
