'''
本题给定一个由列表组成的三角形列表，即每个列表均比它的上一个列表长度长1。要求从上到
下找出一条值相加最短的路径，要求最好只使用O(n)的额外空间。
应用动态规划思想，发现每一行除了最左和最右的两个元素，其余元素均可由上一行的两个元素
访问到，因此可以求得这两个元素的最小值，然后通过这个值来访问本行。如此更新到最后一行。
找最后一行的最小值即可。
本题时间复杂度O(n²)，且没有用额外的空间。运行时间44ms，击败97.45%用户。
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0: #仅可由上一行的第一个元素访问到
					triangle[i][j] += triangle[i-1][j] 
                elif j == len(triangle[i])-1 : #仅可由上一行最后一个元素访问到
					triangle[i][j] += triangle[i-1][j-1]
                else: 
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
