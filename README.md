# Image Recognition Checkers AI Tutor (Back-End)

A full stack mobile app that allows users to take a picture of a checkerboard state, send the photo to our backend server, and get a response as the next best move to make.

## Technologies

The back-end runs off of [Azure Functions.](https://azure.microsoft.com/en-us/services/functions/)

The AI and game structure was built using [Aima Python](https://github.com/aimacode/aima-python) classes.

The image detection was done with [OpenCV.](https://opencv.org/)

## How it works

The back-end receives an HTTP POST request with a JSON object containing the base64 string of the checkerboard image. 

JSON Object Structure 

```
{
  'imageBytes': 'base64String'
}
```

The image is processed with openCV and a game state is generated in a 2D array data structure.

Example Game State

```
[
['0','B','0','B','0','B','0','B'],
['B','0','B','0','B','0','B','0'],
['0','0','0','B','0','B','0','B'],
['0','0','B','0','0','0','0','0'],
['0','0','0','R','0','0','0','0'],
['R','0','0','0','R','0','R','0'],
['0','R','0','R','0','R','0','R'],
['R','0','R','0','R','0','R','0']
]
````

The 2D array structure is sent to the GameOfCheckers class we made and calls the alpha beta cutoff search algorithm. This algorithm uses a minimax like method with alpha beta pruning, but is given a depth limit and an evaluation function.

Our evaluation function is simple and gives a strength to a given move by checking ```players total game pieces - the opponents game pieces```.

The algorithm finally will return a response to the front-end suggesting the best move like so  ```(row of piece to move, column of piece to move) (row of WHERE to move piece to, column of WHERE to move piece to)```

Example: ```(2,3) (1, 2)```

## Collaborators

Shane Spangenberg

Brandon Tomich

Peyman Dinani
