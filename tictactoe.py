"""
Tic Tac Toe Player
"""

from copy import deepcopy
from json.encoder import INFINITY
import math
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    playerx=0
    playero=0
    for rows in range(len(board)):
        for cols in range(len(board[0])):
            if board[rows][cols]== X:
                playerx+=1
            elif board[rows][cols]==O:
                playero+=1
    if playerx==playero:
        return X
    else:
        return O

    
    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions=set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]==EMPTY:
                possibleActions.add((row,col))
    return possibleActions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x,y)=action
    if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
        raise IndexError
    
    newboard=deepcopy(board)
    newboard[x][y]=player(board)
    return newboard
    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRows(board,X) or checkColumn(board,X) or checkTopDiagonal(board,X) or checkBottomDiagonal(board,X):
        return X
    elif checkRows(board,O) or checkColumn(board,O) or checkTopDiagonal(board,O) or checkBottomDiagonal(board,O):
        return O
    else:
        return None

    raise NotImplementedError

def checkRows(board,player):
    count=0
    for rows in range(len(board)):
       count=0
       for col in range(len(board[0])):
            if board[rows][col]==player:
                count+=1
            if count==len(board[0]):
                return True
    return False
        
def checkBottomDiagonal(board,player):
    count=0
    for i in range(len(board)):
            if board[i][len(board)-i-1]==player:
                 count+=1
            if count==len(board[0]):
                return True 
    return False            
    
    

def checkTopDiagonal(board,player):
       count=0
       for i in range(len(board)):
              if board[i][i]==player:
                     count+=1
              if count==len(board[0]):
                    return True 
       return False

def checkColumn(board,player):
    count=0
    for cols in range(len(board[0])):
            count=0
            for rows in range(len(board)):
                if board[rows][cols]==player:
                        count+=1
                if count==len(board[0]):
                    return True
    return False
                        
       



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptycount=0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y]==EMPTY:
                emptycount+=1
    if emptycount==0 or winner(board):
         return True
    else:
         return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)==X:
        action=[]
        for act in actions(board):
            action.append([MIN_Value(result(board,act)),act])
        return sorted(action,key=lambda x: x[0],reverse=True)[0][1]
    elif player(board)==O:
        action=[]
        for act in actions(board):
            action.append([MAX_Value(result(board,act)),act])
        return sorted(action,key=lambda x:x[0])[0][1]

    
    raise NotImplementedError
def MAX_Value(state):
    if terminal(state):
        return utility(state)
    v=-math.inf
    for action in actions(state):
        v=max(v,MIN_Value(result(state,action)))
    return v

def MIN_Value(state):
    if terminal(state):
        return utility(state)
    v=math.inf
    for action in actions(state):
        v=min(v,MAX_Value(result(state,action)))
    return v