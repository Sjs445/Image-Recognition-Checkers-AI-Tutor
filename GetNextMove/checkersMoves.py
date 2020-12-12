# This function takes in a 2D array checkers state of red and white pieces
# and outputs the valid moves for the Red Player in a dictionary.

# The dictionary format is a key that reprents the position of the Red piece
# and its value being where it can move to.

# {'Row of Red Piece, Column of Red Piece': ['Row of space to move to, Column of space to move to']}
# Pieces can have at most 2 spaces to move.

"""*************NOTE***************
This file is for debugging functions
***********************************
"""

import numpy as np


def validCheckersMoves(board, to_move):
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
                                    spaceToMove = str(
                                        rowIndex-1)+str(',')+str(colIndex+1)
                                    valid_moves[piecePosition].append(
                                        spaceToMove)
                                elif board[rowIndex-1][colIndex+1] == 'W':
                                    #   If the space diagonal to the right is a White piece
                                    #   Check if there is a piece behind it
                                    if rowIndex-2 >= 0:
                                        if board[rowIndex-2][colIndex+2] == '0':
                                            spaceToMove = str(
                                                rowIndex-2)+str(',')+str(colIndex+2)
                                            valid_moves[piecePosition].append(
                                                spaceToMove)
                        #   If we are on the right side of the board
                        elif colIndex == 7:
                            #   Only check for values diagonal to the left
                            #   If there is an empty space
                            if rowIndex-1 >= 0:

                                if board[rowIndex-1][colIndex-1] == '0':
                                    #   Append the move to the dictionary of valid moves for that piece
                                    spaceToMove = str(
                                        rowIndex-1)+str(',')+str(colIndex-1)
                                    valid_moves[piecePosition].append(
                                        spaceToMove)
                                elif board[rowIndex-1][colIndex-1] == 'W':
                                    #   If the space diagonal to the left is a White piece
                                    #   Check if there is a piece behind it
                                    if rowIndex-2 >= 0:

                                        if board[rowIndex-2][colIndex-2] == '0':
                                            spaceToMove = str(
                                                rowIndex-2)+str(',')+str(colIndex-2)
                                            valid_moves[piecePosition].append(
                                                spaceToMove)
                        #   If we are in the middle of the board
                        elif rowIndex-1 >= 0:
                            #   Check for values diagonal to the left and right

                            #   Checking right

                            if board[rowIndex-1][colIndex+1] == '0':
                                   #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(
                                    rowIndex-1)+str(',')+str(colIndex+1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex-1][colIndex+1] == 'W':
                                   #   If the space diagonal to the right is a White piece
                                   #   Check if there is a piece behind it
                                if rowIndex-2 >= 0 and colIndex+2 <= 7:

                                    if board[rowIndex-2][colIndex+2] == '0':
                                        spaceToMove = str(
                                            rowIndex-2)+str(',')+str(colIndex+2)
                                        valid_moves[piecePosition].append(
                                            spaceToMove)

                            #   Checking left
                            if board[rowIndex-1][colIndex-1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(
                                    rowIndex-1)+str(',')+str(colIndex-1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex-1][colIndex-1] == 'W':
                                #   If the space diagonal to the left is a White piece
                                #   Check if there is a piece behind it
                                if rowIndex-2 >= 0 and colIndex-2 >= 0:
                                    if board[rowIndex-2][colIndex-2] == '0':
                                        spaceToMove = str(
                                            rowIndex-2)+str(',')+str(colIndex-2)
                                        valid_moves[piecePosition].append(
                                            spaceToMove)
    elif to_move == 'W':
            for rowIndex in range(len(board)):
                for colIndex in range(len(board)):
                    #   If we find a red piece in the board
                    if board[rowIndex][colIndex] == 'W':
                        #   Add the piece's position to the dictionary of valid moves
                        piecePosition = str(rowIndex)+','+str(colIndex)
                        valid_moves[piecePosition] = []

                        #   If we are on the left side of the board
                        if colIndex == 0 and rowIndex+1 <= 7:
                            #   Only check for values diagonal to the right
                            #   If there is an empty space
                            if board[rowIndex+1][colIndex+1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(
                                    rowIndex+1)+str(',')+str(colIndex+1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex+1][colIndex+1] == 'R':
                                #   If the space diagonal to the right is a red piece
                                #   Check if there is a piece behind it
                                if board[rowIndex+2][colIndex+2] == '0':
                                    spaceToMove = str(
                                        rowIndex+2)+str(',')+str(colIndex+2)
                                    valid_moves[piecePosition].append(
                                        spaceToMove)
                        #   If we are on the right side of the board
                        elif colIndex == 7 and rowIndex+1 <= 7:
                            #   Only check for values diagonal to the left
                            #   If there is an empty space
                            if board[rowIndex+1][colIndex-1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(
                                    rowIndex+1)+str(',')+str(colIndex-1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex+1][colIndex-1] == 'R':
                                #   If the space diagonal to the left is a White piece
                                #   Check if there is a piece behind it
                                if rowIndex+2 <= 7:
                                    if board[rowIndex+2][colIndex-2] == '0':
                                        spaceToMove = str(
                                            rowIndex+2)+str(',')+str(colIndex-2)
                                        valid_moves[piecePosition].append(
                                            spaceToMove)
                        #   If we are in the middle of the board
                        elif rowIndex+1 <= 7:
                            #   Check for values diagonal to the left and right

                            #   Checking left
                            if board[rowIndex+1][colIndex+1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(
                                    rowIndex+1)+str(',')+str(colIndex+1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex+1][colIndex+1] == 'R':
                                #   If the space diagonal to the right is a White piece
                                #   Check if there is a piece behind it
                                if rowIndex+2 <= 7 and colIndex+2 <= 7:
                                    if board[rowIndex+2][colIndex+2] == '0':
                                        spaceToMove = str(
                                            rowIndex+2)+str(',')+str(colIndex+2)
                                        valid_moves[piecePosition].append(
                                            spaceToMove)

                            #   Checking left
                            if board[rowIndex+1][colIndex-1] == '0':
                                #   Append the move to the dictionary of valid moves for that piece
                                spaceToMove = str(
                                    rowIndex+1)+str(',')+str(colIndex-1)
                                valid_moves[piecePosition].append(spaceToMove)
                            elif board[rowIndex+1][colIndex-1] == 'R':
                                #   If the space diagonal to the left is a White piece
                                #   Check if there is a piece behind it
                                if colIndex-2 >= 0 and rowIndex+2 <= 7:
                                    if board[rowIndex+2][colIndex-2] == '0':
                                        spaceToMove = str(
                                            rowIndex+2)+str(',')+str(colIndex-2)
                                        valid_moves[piecePosition].append(
                                            spaceToMove)

    return(valid_moves)


def result(board, move, to_move):
    """Return the state that results from making a move from a state."""
    piece = move[:3]
    boardLocation = move[4:]

    if piece not in moves:  # Check if piece is in moves
        return moves
    if boardLocation not in moves[piece]:  # check if move is in moves
        return moves    # If neither exist, move has no effect

        # Make copy of 2D array board
    board = list(map(list, board))

    print("Board before move")
    print(np.matrix(board))

       # Move piece to desired location and update previous location to '0'
    board[int(boardLocation[0])][int(boardLocation[2])] = to_move
    board[int(piece[0])][int(piece[2])] = '0'

       # Update board if it takes other players chip
       # If the column piece minus the column it is going to move is 1 or -1
       # we know there is a jump. Need to set that piece being taken as '0'
    if to_move == 'W':
        # If the rows subtracted together is 2 then we have a jump
        if int(boardLocation[0])-int(piece[0]) == 2:
            if int(boardLocation[2])-int(piece[2]) == -2:
                board[int(boardLocation[0])-1][int(boardLocation[2])+1] = '0'
            elif int(boardLocation[2])-int(piece[2]) == 2:
                board[int(boardLocation[0])-1][int(boardLocation[2])-1] = '0'
    elif to_move == 'R':
        # If the rows subtracted together is -2 then we have a jump
        if int(boardLocation[0])-int(piece[0]) == -2:
            # If the column of the jump location - the column of the original location is 2 we are jumping diagonally right
            if int(boardLocation[2])-int(piece[2]) == 2:
                board[int(boardLocation[0])+1][int(boardLocation[2])-1] = '0'
            elif int(boardLocation[2])-int(piece[2]) == -2:
                board[int(boardLocation[0])+1][int(boardLocation[2])+1] = '0'

    # moves = moves
    # moves[piece].remove(boardLocation)

    print("Board after move")
    print(np.matrix(board))

board = [
['0','R','0','R','0','R','0','R']
,['0','0','R','0','R','0','0','0']
,['0','0','0','0','0','0','0','0']
,['0','0','0','0','0','0','0','0']
,['0','0','0','0','0','W','0','W']
,['0','0','0','0','W','0','W','0']
,['0','R','0','W','0','0','0','R']
,['0','0','R','0','R','0','R','0']]



moves = validCheckersMoves(board=board, to_move='W')

print(moves)

result(board, '5,2 6,3', to_move='W')
