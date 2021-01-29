


def print_board(board,n):
    for i in board:
        for j in i:
            print(j ,end=" ")
        print()
#this function simply prints the board
def change_cell(board,x,y,turn):
    if turn == 1:
        board[x][y]='X'
    else:
        board[x][y]='O'
#in this function we change the vlaue in the given location
#if it's players turn the value changes to X and otherwise to O
def board_full(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j]==' ':
                return 0
#this function checks if the board is full or not
def xwon(board):

    if board[0][0]==board[0][1]==board[0][2]=='X':
        return 1
    if board[1][0]==board[1][1]==board[1][2]=='X':
        return 1
    if board[2][0]==board[2][1]==board[2][2]=='X':
        return 1
    if board[0][1]==board[1][1]==board[2][1]=='X':
        return 1
    if board[0][2]==board[1][2]==board[2][2]=='X':
        return 1
    if board[0][0]==board[1][0]==board[2][0]=='X':
        return 1
    if board[0][0]==board[1][1]==board[2][2]=='X':
        return 1
    if board[0][2]==board[1][1]==board[2][0]=='X':
        return 1
    return 0
#this function checks if player has won the game
#it does this task by checking every way that a player can win
def owon(board):
    if board[0][0] == board[0][1] == board[0][2] == 'O':
        return 1
    if board[1][0] == board[1][1] == board[1][2] == 'O':
        return 1
    if board[2][0] == board[2][1] == board[2][2] == 'O':
        return 1
    if board[0][1] == board[1][1] == board[2][1] == 'O':
        return 1
    if board[0][2] == board[1][2] == board[2][2] == 'O':
        return 1
    if board[0][0] == board[1][0] == board[2][0] == 'O':
        return 1
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        return 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        return 1
    return 0
#this function checks if computer has won the game
def evalx(board,n):
    xval=0
    cnt=0
    for i in range(n):
        if cnt==3:
            xval+=1
        cnt=0
        for j in range(n):
            if (board[i][j]==' ' or board[i][j]=='X'):
                cnt+=1
    if cnt==3:
        xval+=1
    cnt = 0
    for i in range(n):
        if cnt == 3:
            xval += 1
        cnt = 0
        for j in range(n):
            if (board[j][i] == ' ' or board[j][i] == 'X'):
                cnt += 1
    if cnt==3:
        xval+=1
    if (board[0][0] ==' ' or board[0][0]=='X'):
        if (board[1][1] == ' ' or board[1][1] == 'X'):
            if (board[2][2] == ' ' or board[2][2] == 'X'):
                xval+=1
    if (board[0][2] ==' ' or board[0][2]=='X'):
        if (board[1][1] == ' ' or board[1][1] == 'X'):
            if (board[2][0] == ' ' or board[2][0] == 'X'):
                xval+=1
    return xval
#this function calculates the evaluation function for x player.
#it checks for every row , column , and diagonal the x player can make a line and win the game
def makesame(board,secboard,n):
    for i in range(n):
        for j in range(n):
            secboard[i][j]=board[i][j]
#this function makes the secboard equal to the board
def evalo(board,n):
    oval=0
    cnt=0
    for i in range(n):
        if cnt==3:
            oval+=1
        cnt=0
        for j in range(n):
            if board[i][j]==' ' or board[i][j]=='O':
                cnt+=1
    if cnt == 3:
        oval+=1
    cnt = 0
    for i in range(n):
        if cnt == 3:
            oval += 1
        cnt = 0
        for j in range(n):
            if board[j][i] == ' ' or board[j][i] == 'O':
                cnt += 1
    if cnt==3:
        oval+=1
    if board[0][0] ==' ' or board[0][0]=='O':
        if board[1][1] == ' ' or board[1][1] == 'O':
            if board[2][2] == ' ' or board[2][2] == 'O':
                oval+=1
    if board[0][2] ==' ' or board[0][2]=='O':
        if board[1][1] == ' ' or board[1][1] == 'O':
            if board[2][0] == ' ' or board[2][0] == 'O':
                oval+=1
    return oval
#this function calculates the evaluation function for o player.
#it checks for every row , column , and diagonal the o player can make a line and win the game
def main():
    n=3
    xval=0
    oval=0
    board = [[' ' for i in range(n)] for j in range(n)]
    turn=1
    while(board_full(board,n)==0):#
      if turn==1:#players turn
        print("please enter your desired cells")
        x = int(input())
        y = int(input())
        change_cell(board,x,y,turn)
        print_board(board,n)
        if(xwon(board)==1):
            print("player 1 won the game")
            print_board(board,n)
            break
        turn = turn - 1
       # break
      if turn==0 :# computers turn
          check=evalx(board,n)-evalo(board,n)
          tmp = [[' ' for i in range(n)] for j in range(n)]
          makesame(board,tmp,n)
          print_board(tmp,n)
          won = 0
          for i in range(n):
              if won == 1:
                  break
              for j in range(n):
                  if board[i][j]==' ':
                      tmp_board = [[' ' for i in range(n)] for j in range(n)]
                      makesame(board,tmp_board,n)
                      change_cell(tmp_board,i,j,turn)
                      if (owon(tmp_board)==1):
                          makesame(board, tmp, n)
                          makesame(tmp_board, tmp, n)
                          won+=1
                          break
                      check_tmp=(evalx(tmp_board,n)-evalo(tmp_board,n))
                      if check_tmp<check:
                          check=check_tmp
#here we check for the best move computer can make by checking difference of evaluation functions
                          makesame(board,tmp,n)
                          makesame(tmp_board,tmp,n)
                          break
                      elif check==evalx(board,n)-evalo(board,n) and check_tmp==0:
                          makesame(board, tmp, n)
                          makesame(tmp_board, tmp, n)
          if won==0:
              for i in range(n):
                  for j in range(n):
                      if tmp[i][j]==' ':
                          tmpp_board = [[' ' for i in range(n)] for j in range(n)]
                          makesame(tmp_board, tmpp_board, n)
                          change_cell(tmpp_board, i, j, 1)
                          if(xwon(tmpp_board)==1):
                              makesame(board,tmp,n)
                              tmp[i][j]='O'
#here we check if the player can win in the next move even though we picked the best move
#if so , we will change the value in the position it can win the game into o
          makesame(tmp,board,n)
          if owon(board)==1:
              print("computer won the game")
              print_board(board,n)
              break
      print_board(board,n)
      print("this is the dif:",evalx(board,n) - evalo(board,n))
      turn=turn+1
    if xwon(board)==0 and owon(board)==0:
        print("its a draw")
main()