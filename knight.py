def issafe(x,y,board):
    if x>=0 and y>=0 and x<n and y<n and board[x][y]==-1:
        return True
    return False
def printsol(board,n):
    for i in board:
        print(*i)
def ksol(n):
    board=[[-1 for i in range(n)]for j in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0]=0
    pos=1
    if(not ktsol(move_x,move_y,n,board,pos,0,0)):
        print("Not Exists")
    else:
        printsol(board,n)




def ktsol(move_x,move_y,n,board,pos,cur_x,cur_y):
    if pos==n**2:
        return True
    for i in range(8):
        nxt_x=cur_x+move_x[i]
        nxt_y=cur_y+move_y[i]
        if(issafe(nxt_x,nxt_y,board)):
            board[nxt_x][nxt_y]=pos
            if(ktsol(move_x,move_y,n,board,pos+1,nxt_x,nxt_y)):
                return True

            board[nxt_x][nxt_y]=-1
    return False


n=int(input("Enter the n value"))
ksol(n)
