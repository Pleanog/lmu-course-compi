from typing import List, Union, Tuple

def queens(n:int, k:int, board:List[List[bool]])->Tuple[bool, Union[None, List[List[bool]]]]:
    ''' The backtracking algorithm for finding solutions to the n-Queens problem, 
        where k is the starting rank of the first queen. Returns True (and the solution board) 
        if a solution can be / was found, else False & None. '''
    if k >= n:
        return True
    for i in range(0,n):
        board[i][k] = True
        if not any(board[i][j] for j in range(0,k))                     \
        and not any(board[i-j][k-j] for j in range(1, min(k,i)+1))      \
        and not any(board[i+j][k-j] for j in range(1, min(k,n-i-1)+1))  \
        and queens(n, k+1, board):
            return True
        board[i][k] = False
    return False
        
if __name__ == "__main__":
    n = 100
    k = 4
    empty_board = [[False for _ in range(n)] for _ in range(n)]
    print(queens(n, k, empty_board))