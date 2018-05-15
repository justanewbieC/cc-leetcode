'''
本题给定一个二维矩阵.二维数组的元素由0和1组成.要求找出1组成的最大正方形,返回其面积.
本题应用动态规划思想.先将输入的字符串数组变成一个二维数组.用两层for循环遍历dp数组.
如果dp[i][j]==1，则将它左上，上和左的三个dp取最小值加1赋给它(例如:如果它的左上，
左，上元素均为1，则可将dp[i][j]更新到2，说明此点可以构成2*2的矩形)。以此下去返回
二维数组中的最大值即为正方形最大边长。
本题时间复杂度为O(n*n)，运行时间84ms。
'''
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix : return 0
        m , n = len(matrix) , len(matrix[0])
        #构造dp二维数组
        dp = [[1 if matrix[i][j] == '1' else 0 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return max(max(subdp) for subdp in dp)**2
