'''
本题给定一个数，要求用最少的perfect square(1,4,9,16,...)相加组成这个数，并返回
所用perfect square的个数。本题是一个动态规划问题，且可以用广度优先搜索解决。先求
不大于n的平方根的最大数(int(math.sqrt(n))，再用i从这个数到1遍历，将n-(i*i)添入
一个队列中，同时维护一个count(表示用了几个数)。如此不断向队列中添加元素，遍历完成后
再从队列中取队首继续遍历，直到遇到n-i*i=0，返回count+1即可。
本题时间复杂度为O(n*n)，且运行时间非常长，效率非常低。其原因在于向队列中添加了很多
不必要的元素。例如在i的值比较小的时候，得到perfect square的路径则不可能出自于它，
因此将它加入队列是没有必要的。因此我加入了一个判断:
if numSum - (i**2) > 2*(i**2):
	break
这样加入后，运行速度提升了十几倍。

'''
import math
from collections import deque
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 : return 0
        #用deque可以方便实现queue数据结构。第二个参数为用perfect square的次数
        squareQueue = deque([[n, 0]]) 
        while squareQueue:
            numSum , count = squareQueue.popleft()
            for i in range(int(math.sqrt(numSum)), 0, -1):
                if numSum - (i**2) != 0:
                    squareQueue.append([numSum-(i**2), count+1])
                else:
                    return count+1
