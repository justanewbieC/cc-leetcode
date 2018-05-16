'''
本题要求判断给定的一个数是否为Ugly Number。Ugly Number是一个正数，且其素因子只能
包括2,3,5。显然如果一个数是Ugly Number，那么它一定可以分解为只有2,3,5三个因子的
乘积的形式。如8=2*2*2,12=2*2*3.因此可以利用这一点来判断此数是否为Ugly Number。
本题运行时间52ms，击败100%用户。
'''
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 : return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num = num // i
        #如果最后num变为1，则说明num可完全由若干个2,3,5相乘得到，故num为Ugly Number
        return num == 1 
