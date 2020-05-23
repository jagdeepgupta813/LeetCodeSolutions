##  Find minimum path sum, starting from 0,0 to the last corner element 

#Given a m x n grid filled with non-negative numbers, 
#find a path from top left to bottom right which minimizes the sum of all numbers along its path.

##Note: You can only move either down or right at any point in time.


def minPathSum(path):
    if(path is None or len(path)<1):
        return 0
    m =len(path)
    n=len(path[0])
    minimum=0

    for x in range(0,m):
        for y in range(0,n):
            if(x>0 and y>0):
                minimum=min(path[x-1][y], path[x][y-1])

            elif(x>0):
                minimum=path[x-1][y]

            elif(y>0):
                minimum=path[x][y-1]

            path[x][y]=path[x][y] + minimum

    return path[m-1][n-1]


if __name__=="__main__":
    a=[[1,2,3],
       [3,4,5],
       [4,6,9],
       [1,4,7] ]
    print(minPathSum(a))
