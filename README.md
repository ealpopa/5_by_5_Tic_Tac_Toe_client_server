# 5_by_5_Tic_Tac_Toe_client_server
5_by_5_Tic_Tac_Toe_client_server

This is a very simple and rudimentary 5 x 5 Tic Tac Toe game using sockets.

How to launch the game:
1. Launch server.py. Ex: ./server.py
2. Each client is launched. Ex: ./client.py 127.0.0.1

####

Play instructions:
Game board is a 5 x 5 as diplayed below

+--+--+--+--+--+
| 1| 2| 3| 4| 5|
+--+--+--+--+--+
| 6| 7| 8| 9|10|
+--+--+--+--+--+
|11|12|13|14|15|
+--+--+--+--+--+
|16|17|18|19|20|
+--+--+--+--+--+
|21|22|23|24|25|
+--+--+--+--+--+

PlayerX will make the first move. The first customer to connect to the customer will be assigned
as Player X.
Each player indicates the position he marks by sending the number assigned to that position
according to the numbering mentioned above.
The player can only enter numbers between 1-25.
If the player enters the letter 'q', the game will end.
If all 25 positions have been completed and there is no winner, then it is a draw.

####

Client.py implementation
The client connects to the server via TCP.
There are three main state variables:
- PlayerType - variable that waits 16 bytes ('You are player X')
- GameState - variable waiting 4 bytes ('xTur', 'oTur', 'finX', 'finO', 'xWin', 'oWin', tie
- table state - variable that expects a maximum of 133 bytes (text representation of the table)

The client makes decisions and follows the game loop according to the values ​​of the three state variables.
The loop checks whether the game has ended as a result of a player's order to complete, draw or win.
If these 3 closing sessions have not been fulfilled, it is checked whose turn it is (player X or player O).

###

Server.py implementation
The server waits and accepts 2 connections.
The table positions and the values ​​stored on them are implemented using the dictionary data structure
Functions have been defined to fulfill the main roles, minimizing code redundancy
checkForWin checks if 5 consecutive diagonal, vertical and horizontal positions contain the same symbol
broadcastBoard sends the status of the board to the two players
validMove verifies the correctness of the position sent by the players
oPlay and xPlay are the two functions that, in 0 loop, lead to the development of the game
The game loop runs on 25 iterations, after each iteration it is checked if
there is a winner.
The server sends predefined messages (xWin, oWin, finX, finO, draw, xTurn, oTurn) to control
the logical development of the session.

###
Messages used
xTur - signals to the client application that it is time to take the position it wants from the keyboard
to move Player X
oTur - ditto for Player O
xWin - signals that player X has won and triggers the sending of announcement messages and the closing of the session
oWin - ditto for Player O
finX - signals to the client application that Player X has logged out. triggers logout and announcement message
finO - ditto for Player O
tie - signals to client applications that the game has ended as a result of occupying all positions, without a winner.
