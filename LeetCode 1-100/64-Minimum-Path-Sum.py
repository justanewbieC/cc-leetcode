'''
本题给定一个grid二维数组,每个元素为那一点的值。要求从左上角选择一条路径到右下角，
并各点值相加最小。
本题是动态规划问题，可以直接在grid上进行操作。如果是第一行，则只能加它左边的元素；
如果是第一列，则只能加它上边的元素；否则加两者最小值。最后返回右下角元素。
本题用时56ms，击败95.57%用户。
'''
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid : return 0
        row , col = len(grid) , len(grid[0])
        for i in range(row):
            for j in range(col):
                if i == j == 0: continue #左上角元素不用操作
                elif i == 0 : grid[i][j] += grid[i][j-1]
                elif j == 0 : grid[i][j] += grid[i-1][j]
                else: grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
