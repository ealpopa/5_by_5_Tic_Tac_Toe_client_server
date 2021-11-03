#!/usr/bin/python
import socket;
import sys;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0);
#host = '127.0.0.1';
port = 6000;
s.connect((sys.argv[1], port));

print('Please wait for other player');
print('Player X has first turn');

## receive player type info
playerType = s.recv(16).decode();
print(playerType);

tura = 0;
while True:
    #The game state is obtained from the server via the gameState variable
    #possible states: game over by request, tie, win, player turn
    gameState = s.recv(4).decode();
    
    #check if any of the two players have requested to end the game
    if gameState == 'finX':
        print('Player X has closed the game.');
        s.close();
        break;
    elif gameState == 'finO':
        print('Player O has closed the game.');
        s.close();
        break;

    #check if game if over due to tie
    elif gameState == 'tie':
        print('Game over: Tie');
        s.close();
        break;

    #check if game has been won by either player
    elif gameState == 'xWin':
        boardState = s.recv(133).decode();
        print(boardState);
        if playerType == 'You are player X':
            print ('You win!');
        elif playerType == 'You are player O':
            print ('You lose.');
        s.close();
        break;
    elif gameState == 'oWin':
        boardState = s.recv(133).decode();
        print(boardState);
        if playerType == 'You are player X':
            print ('You lose.');
        elif playerType == 'Esti jucatorul O':
            print ('You win!');
        s.close();
        break;

    #if game is not over due to any reason then gameState variable indicated the current player to make move
    elif gameState == 'xTur':
        boardState = s.recv(133).decode(); 	    
        print(boardState);
        move = input("Player X, insert a position (1-25) or 'q' to quit: ");
        s.send(move.encode());
        print('Wait for other player move');
        tura += 1;
    elif gameState == 'oTur':
        boardState = s.recv(133).decode();
        print(boardState);
        move = input("Player O, insert a position (1-25) or 'q' to quit: ");
        s.send(move.encode());
        print('Wait for other player move');
        tura += 1;    
s.close();


