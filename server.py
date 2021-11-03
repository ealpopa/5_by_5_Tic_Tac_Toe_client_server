#!/usr/bin/python
import socket;

poz = {'1': ' ', '2': ' ', '3':' ', '4':' ', '5':' ',
       '6': ' ', '7': ' ', '8':' ', '9':' ', '10':' ',
       '11': ' ', '12': ' ', '13':' ', '14':' ', '15':' ',
       '16': ' ', '17': ' ', '18':' ', '19':' ', '20':' ',
       '21': ' ', '22': ' ', '23':' ', '24':' ', '25':' '};

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0);

host = '127.0.0.1';
port = 6000;

s.bind((host, port));
s.listen(2);

print('Server started. Waiting for the two players to join.');

boardString = '''
+-+-+-+-+-+
|{}|{}|{}|{}|{}|
+-+-+-+-+-+
|{}|{}|{}|{}|{}|
+-+-+-+-+-+
|{}|{}|{}|{}|{}|
+-+-+-+-+-+
|{}|{}|{}|{}|{}|
+-+-+-+-+-+
|{}|{}|{}|{}|{}|
+-+-+-+-+-+
'''

def sendBoardToOnePlayer(client):
    client.send(boardString.format(poz['1'], poz['2'], poz['3'], poz['4'], poz['5'],
                                   poz['6'], poz['7'], poz['8'], poz['9'], poz['10'],
                                   poz['11'], poz['12'], poz['13'], poz['14'], poz['15'],
                                   poz['16'], poz['17'], poz['18'], poz['19'], poz['20'],
                                   poz['21'], poz['22'], poz['23'], poz['24'], poz['25']).encode());

def broadcastBoard(client1, client2):
    sendBoardToOnePlayer(client1);
    sendBoardToOnePlayer(client2);

def checkForWin():
    ##Horizontal win
    if poz['1'] == poz['2'] == poz['3'] == poz['4'] == poz['5'] == 'X':
        return 'xWin';
    elif poz['1'] == poz['2'] == poz['3'] == poz['4'] == poz['5'] == 'O':
        return 'oWin';
    elif poz['6'] == poz['7'] == poz['8'] == poz['9'] == poz['10'] == 'X':
        return 'xWin';
    elif poz['6'] == poz['7'] == poz['8'] == poz['9'] == poz['10'] == 'O':
        return 'oWin';
    elif poz['11'] == poz['12'] == poz['13'] == poz['14'] == poz['15'] == 'X':
        return 'xWin';
    elif poz['11'] == poz['12'] == poz['13'] == poz['14'] == poz['15'] == 'O':
        return 'oWin';
    elif poz['16'] == poz['17'] == poz['18'] == poz['19'] == poz['20'] == 'X':
        return 'xWin';
    elif poz['16'] == poz['17'] == poz['18'] == poz['19'] == poz['20'] == 'O':
        return 'oWin';
    elif poz['21'] == poz['22'] == poz['23'] == poz['24'] == poz['25'] == 'X':
        return 'xWin';
    elif poz['21'] == poz['22'] == poz['23'] == poz['24'] == poz['25'] == 'O':
        return 'oWin';
        
    ##Vertical win
    elif poz['1'] == poz['6'] == poz['11'] == poz['16'] == poz['21'] == 'X':
        return 'xWin';
    elif poz['1'] == poz['6'] == poz['11'] == poz['16'] == poz['21'] == 'O':
        return 'oWin';
    elif poz['2'] == poz['7'] == poz['12'] == poz['17'] == poz['22'] == 'X':
        return 'xWin';
    elif poz['2'] == poz['7'] == poz['12'] == poz['17'] == poz['22'] ==  'O':
        return 'oWin';
    elif poz['3'] == poz['8'] == poz['13'] == poz['18'] == poz['23'] == 'X':
        return 'xWin';
    elif poz['3'] == poz['8'] == poz['13'] == poz['18'] == poz['23'] == 'O':
        return 'oWin';
    elif poz['4'] == poz['9'] == poz['14'] == poz['19'] == poz['24'] == 'X':
        return 'xWin';
    elif poz['4'] == poz['9'] == poz['14'] == poz['19'] == poz['24'] == 'O':
        return 'oWin';
    elif poz['5'] == poz['10'] == poz['15'] == poz['20'] == poz['25'] == 'X':
        return 'xWin';
    elif poz['5'] == poz['10'] == poz['15'] == poz['20'] == poz['25'] == 'O':
        return 'oWin';
        
        ##Diagonal win
    elif poz['1'] == poz['7'] == poz['13'] == poz['19'] == poz['25'] == 'X':
        return 'xWin';
    elif poz['1'] == poz['7'] == poz['13'] == poz['19'] == poz['25'] == 'O':
        return 'oWin';
    elif poz['2'] == poz['7'] == poz['12'] == poz['17'] == poz['22'] == 'X':
        return 'xWin';
    elif poz['5'] == poz['9'] == poz['13'] == poz['17'] == poz['21'] ==  'O':
        return 'oWin';
    elif poz['5'] == poz['9'] == poz['13'] == poz['17'] == poz['21'] == 'X':
        return 'xWin';
        
    ##Nobody wins
    else: return False;

def validMove(move):
    if move.isdigit() and int(move) > 0 and int(move) < 26 and poz[move] == ' ':
        return True;
    else:
        return False;

#the two client connections
xClient, addr1 = s.accept();
oClient, addr2 = s.accept();

print('Jucatorul X s-a conectat de la : ', addr1);
print('Jucatorul O s-a conectat de la : ', addr2);

#Inform players of allocated symbol
xClient.send('Esti jucatorul X'.encode());
oClient.send('Esti jucatorul O'.encode());

def oPlay():
    oClient.send('oTur'.encode());
    sendBoardToOnePlayer(oClient);
    move = oClient.recv(2).decode();
    if move == 'q':
        print ('Player O closed the game.');
        oClient.send('finO'.encode());
        xClient.send('finO'.encode());
        s.close();
    elif validMove(move):
        print ('Player O submited position ',move);
        poz[move] = 'O';
    elif not validMove(move):
        print ('Player O submited position ',move);
        oPlay();

def xPlay():
    xClient.send('xTur'.encode());
    sendBoardToOnePlayer(xClient);
    move = xClient.recv(2).decode();
    if move == 'q':
        print ('Player X closed the game.');
        oClient.send('finX'.encode());
        xClient.send('finX'.encode());
        s.close();
    if validMove(move):
        poz[move] = 'X';
        print ('Player X submited position ', move);
    elif not validMove(move):
        print ('Player X submited position ', move);
        xPlay();

turn = 0;
while turn < 25:
    #display game table status on the server console
    print(boardString.format(poz['1'], poz['2'], poz['3'], poz['4'], poz['5'],
                             poz['6'], poz['7'], poz['8'], poz['9'], poz['10'],
                             poz['11'], poz['12'], poz['13'], poz['14'], poz['15'],
                             poz['16'], poz['17'], poz['18'], poz['19'], poz['20'],
                             poz['21'], poz['22'], poz['23'], poz['24'], poz['25']));
    gameStatus = checkForWin();
    if gameStatus == 'xWin':
        print("Player X won.");
        oClient.send('xWin'.encode());
        xClient.send('xWin'.encode());
        broadcastBoard(xClient, oClient);
        break;
    elif gameStatus == 'oWin':
        print("Player O won.");
        oClient.send('oWin'.encode());
        xClient.send('oWin'.encode());
        broadcastBoard(xClient, oClient);
        break;
    player = [xPlay, oPlay];
    idx = turn % 2;
    player[idx]();
    
    #check for tie
    if turn == 24:
        gameStatus = checkForWin();
        if not gameStatus:
            oClient.send('tie'.encode());
            xClient.send('tie'.encode());
            print('Game over: Tie');
        elif gameStatus == 'xWin':
            oClient.send('xWin'.encode());
            xClient.send('xWin'.encode());
            print('Player X won');
        elif gameStatus == 'oWin':
            oClient.send('oWin'.encode());
            xClient.send('oWin'.encode());
            print('Player O won');
    turn += 1;
s.close();
