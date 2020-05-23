## code to find out the minimum cost it can take to reach to the top

# Each stair is associated with a cost
## On a staircase, the i-th step has some non-negative cost
#cost[i] assigned (0 indexed).
#Once you pay the cost, you can either climb one or two steps.
#You need to find minimum cost to reach the top of the floor,
#and you can either start from the step with index 0, or the step with index 1.

def minCostClimbingStairs(cost, n):
    for i in range(2,n):
        cost[i]=cost[i]+ min(cost[i-2], cost[i-1])
    return min(cost[n-2],cost[n-1])

## test the code with main function

if __name__ == "__main__":
    a = [16,10,19,12,18]
    n=len(a)
    print(minCostClimbingStairs(a,n))


    
