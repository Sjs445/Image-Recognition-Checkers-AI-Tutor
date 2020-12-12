import logging
import azure.functions as func
from . import imageRec
from .GameOfCheckers import GameOfCheckers
from .games import alpha_beta_cutoff_search



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    base64Image = req_body.get('imageBytes')
    detectedState = imageRec.DetectImage(base64Image)

    checkers = GameOfCheckers(detectedState)

    suggestedMove = alpha_beta_cutoff_search(checkers.initial, checkers, 4, cutoff_test=None, eval_fn=eval_fn)

    return func.HttpResponse(
            suggestedMove,
            status_code=200)

    # if not imageBytes:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         imageBytes = req_body.get('bytes')

    # if imageBytes:
    #     return func.HttpResponse(f"Image Bytes: {imageBytes}")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass image bytes in the body of the request as json.",
    #          status_code=200
    #     )



def eval_fn(state):
        redPiece = 0
        bluePiece = 0

        for row in state.board:
            for piece in row:
                if piece == 'R':
                    redPiece+=1
                elif piece == 'B':
                    bluePiece+=1
        
        if state.to_move == 'R':
            return(redPiece-bluePiece)
        else:
            return(bluePiece-redPiece)