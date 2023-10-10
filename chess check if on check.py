import numpy as np
def king_is_in_check(chessboard : list[list[str]]) -> bool:
    
    row, column = np.where(np.array(chessboard) == '♔')  # locate where the king is, and save the coordinates in different variables.
     
    print("the row is" + str(row) )
    print("the column is" + str(column) )
    row=int(row)
    column=int(column)
    
    try:    #we put this first because a Pawn or a Knight cannot be blocked
        
             
            
        
        if chessboard[row-1][column+1]== '♟' or chessboard[row-1][column+1]== '♟': #check for the pawn
            return True
        if chessboard[row+2][column-1] == '♞'  or chessboard[row+2][column+1] == '♞': #below the king
            return True
        if  chessboard[row-2][column-1] == '♞' or chessboard[row-2][column+1] == '♞': #above the king
            return True
        if  chessboard[row-1][column+2] == '♞' or chessboard[row+1][column+2] == '♞': #on the right of the king
            return True
        if  chessboard[row-1][column-2] == '♞' or chessboard[row+1][column+2] == '♞': #on the left of the king
            return True
        
        
    except: 
        print("amongus")
        
    for x in range(8): # only one loop to check for a linear check and a diagonal check
                if chessboard[x][column] == '♜' or chessboard[x][column] == '♛' : return True
                if chessboard[row][x]== '♜' or chessboard[row][x] == '♛' : return True
    try:
        for x in range(8):
                    if chessboard[0][7]== '♝':     return True
                    if chessboard[row+x][column+x]== '♛' or chessboard[row+x][column+x]== '♝':    return True #diagonal

                    if chessboard[row+x][column-x]== '♛' or chessboard[row+x][column-x]== '♝':     return True

                    if chessboard[row-x][column+x]== '♛' or chessboard[row-x][column+x]== '♝':     return True

                    if chessboard[row-x][column-x]== '♛' or chessboard[row-x][column-x]== '♝':    return True        
    except: print(x)
              
    return False