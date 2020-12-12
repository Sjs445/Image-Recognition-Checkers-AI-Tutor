from games import *
from .GameOfCheckers import GameOfCheckers

# YOUR CODE GOES HERE

checkers = GameOfCheckers(board=[
['0','B','0','B','0','B','0','B'],
['B','0','B','0','B','0','B','0'],
['0','0','0','B','0','B','0','B'],
['0','0','B','0','0','0','0','0'],
['0','0','0','R','0','0','0','0'],
['R','0','0','0','R','0','R','0'],
['0','R','0','R','0','R','0','R'],
['R','0','R','0','R','0','R','0']
])

def eval_fn(state):
        redPiece = 0
        whitePiece = 0

        for row in state.board:
            for piece in row:
                if piece == 'R':
                    redPiece+=1
                elif piece == 'B':
                    whitePiece+=1
        
        if state.to_move == 'R':
            return(redPiece-whitePiece)
        else:
            return(whitePiece-redPiece)


if __name__ == "__main__":
    # utility = checkers.play_game(alpha_beta_player, query_player) # computer moves first 
    # print(utility)
    # if utility == 0:
    #     print("Tie game")
    # if (utility < 0):
    #     print("MIN won the game")
    # else:
    #     print("MAX won the game")
    print(alpha_beta_cutoff_search(checkers.initial, checkers, cutoff_test=None, eval_fn=eval_fn))