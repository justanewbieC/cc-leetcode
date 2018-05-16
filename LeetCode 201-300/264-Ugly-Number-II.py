'''
本题给定一个数n,要求返回第n大的Ugly Number.Ugly Number与2,3,5有关,
因此可以在2,3,5的基础上每次更新一个最小值.想到这里后我便没了思路.最终借鉴了
discuss中的算法.首先在ugly数组中添加1.i2,i3,i5表示2,3,5应分别与ugly中的第几个
数相乘.如min(2*ugly[i2],3*ugly[i3],5*ugly[i5])=2*ugly[i2]，这时应将i2+1。
意味着下一个最小的数不可能是再拿2*ugly[i2]和其他数比较，应该用2*ugly[i2+1]与其他
数比较。并将这个min值添入ugly数组，如此更新下去，直至找到第n大ugly number。
此算法需要额外注意 u2，u3，u5中有时会有同样小的值，对于相等的值，相应的i应分别加1.
本题时间复杂度为O(n)，运行时间152ms。
'''
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2 , i3 , i5 = 0 , 0 , 0
        while n > 1:
            u2, u3 , u5 = 2*ugly[i2] , 3*ugly[i3] , 5*ugly[i5] 
            uglyMin = min(u2, u3, u5) #当前最小的数
            if uglyMin == u2:
                i2 += 1
            if uglyMin == u3:
                i3 += 1
            if uglyMin == u5:
                i5 += 1
            ugly.append(uglyMin)
            n -= 1
        return ugly[-1]
