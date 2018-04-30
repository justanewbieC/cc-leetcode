'''
本题同样是n皇后问题。思路与上一题一样，只需维护一个result即可。
本题运行时间为52ms，击败96.91%用户。
'''
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.nQueens([], n, [], [])
        
    def nQueens(self, A, n, xy_dif, xy_sum, cur=0):
        if cur == n:
            return 1
        result = 0
        for col in range(n):
            if col not in A and cur-col not in xy_dif and cur+col not in xy_sum:
                result += self.nQueens(A+[col], n, xy_dif+[cur-col], xy_sum+[cur+col], cur+1)
        return result
