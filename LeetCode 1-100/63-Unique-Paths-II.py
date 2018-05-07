'''
本题在上一题的基础上加大难度，机器人在行走的过程中可能会碰到障碍。用1表示该点是障碍。
遇到障碍则此条路不能再走下去。我沿用上一题的解法，只是多加了一些判断。
先将每个点的值设为0，并将左上角的值设为1，接着进入循环。
(1)如果这一点是障碍，或者它的上一点和左一点都是障碍，或者它是初始点，则continue。
(2)如果它的上一点是障碍或它处于第一行，则(i,j)+=(i,j-1)
(3)如果它的左一点是障碍或它处于第一列，则(i,j)+=(i-1,j)
(4)如果都不满足，则(i,j)+=(i,j-1)+(i-1,j)
本题时间，空间复杂度均为O(m*n)，运行时间40ms，击败96.54%用户。
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid: return 0
        m , n  = len(obstacleGrid) , len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] != 1 : dp[0][0] = 1
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j] == 1 or (obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1) \
                    or (i == j == 0): continue
                elif obstacleGrid[i-1][j] == 1 or i == 0: dp[i][j] += dp[i][j-1]
                elif obstacleGrid[i][j-1] == 1 or j == 0: dp[i][j] += dp[i-1][j]
                else: dp[i][j] += dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
