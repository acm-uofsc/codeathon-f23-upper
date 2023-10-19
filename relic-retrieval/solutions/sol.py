""" Solution for Relic Retrieval"""

def solution():
    """ Solution for Relic Retrieval """

    # Read in input
    m, n = list(map(int, input().split()))
    labyrinth = []
    for _ in range(m):
        row = list(map(int, input().split()))
        labyrinth.append(row)

    # initialize dp
    dp = [[float("inf") for _ in range(n+1)] for _ in range(m+1)]
    dp[m-1][n] = 1
    dp[m][n-1] = 1

    # start in bottom right, traverse backwards using the minimum damage paths
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            current_min_stamina = min(dp[i+1][j], dp[i][j+1])

            # if the left term is negative, that means the health we received is enough
            # to get us to the end coming in with only 1 health
            dp[i][j] = max(current_min_stamina - labyrinth[i][j], 1)

    return dp[0][0]


if __name__ == "__main__":
    print(solution())
