## You are given coins of different denominations and a total amount of money amount.
##Write a function to compute the fewest number of coins that you need to make up that amount.
##If that amount of money cannot be made up by any combination of the coins, return -1.

## this is bottom-up approach, where we are saving the data for each value untill we reach the final value to save on the calculation
## this is DP case with memory


import sys

def coinChange(coins,value):
    return coinChangeBottomUpWithMemorization(coins,value)

def coinChangeBottomUpWithMemorization(coins, value):
    if(value<0):
        return -1
    if(value==0):
        return 0
    if(len(coins) <1):
        return -1


    memory=[0 for k in range(value+1)] ## adding 1 for using case of 0
    
    memory[0]=0 ## for base case
    m=len(coins)

    ##initialize the memory to maximum value
    for i in range(1, value+1):
        memory[i]=sys.maxsize


    for j in range(1,value+1):
        for c in range(m):
            if(coins[c] <=j and j>0):
                minimum=memory[j-coins[c]]
                if(minimum!=sys.maxsize and memory[j] > minimum+1 ):    ## check if the value is not the default value and the current count is actually min
                    memory[j]=minimum+1



    return memory[value]


### test with the main code

if __name__ == "__main__":
    a=[10,4,27,5,11]
    print("the value returned is : " ,  coinChange(a, 23))
    
    
    
