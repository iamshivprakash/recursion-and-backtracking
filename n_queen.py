def isItSafePlaceForTheQueen(chess,row,col):
    for i in range(row-1,-1,-1):
        if (chess[i][col]==1):
            # print(i,col,"False from 1")
            return False
    for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
        if (chess[i][j]==1):
            # print(i,j, "False from 2")
            return False
    for i,j in zip(range(row-1,-1),range(col+1)):
        if (chess[i][j]==1):
            # print(i,j,"False from 3")
            return False
    return True
    

def printNQueen(chess,row,asf):
    if row == len(chess):
        print(asf)
        return
    
    for col in range(len(chess)):
        print("row:",row,",","col:",col,chess)
        if(isItSafePlaceForTheQueen(chess,row,col)==True):
            chess[row][col]=1 
            printNQueen(chess,row+1,asf+str(row)+"-"+str(col)+", ")
            chess[row][col]=0
    
    

    
print(printNQueen([[0]*4]*4,0,""))
        
