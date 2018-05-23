'''
假设在爬楼梯，有n阶台阶需要爬，每次只能爬1到2步。求解爬到楼梯顶有多少种爬法。
本题的解其实是1个斐波那契数列。
n=1，有1种;
n=2，有两种;
n=3，可以从第1台阶跨2步到3，也可从第2台阶跨1步到3，因此有1+2=3种;
n=4，可以从第2台阶跨2步到4，也可从第3台阶跨1步到4，因此有2+3=5种..
显然当n>2时，dp[n]=dp[n-1]+dp[n-2],dp[n]表示n层楼梯有多少种爬法
本题时间复杂度为O(n)，可以使用常数项空间，运行时间32ms，击败100%用户。
'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2
        before , now = 1 , 2 # now表示当前楼梯数，before表示前一阶楼梯数
        for stair in range(2, n):
            before , now = now , before+now
        return now
