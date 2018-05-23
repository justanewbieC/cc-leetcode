'''
本题需要完成通配符的匹配。在通配符中'?'可以匹配任何单个字母，'*'匹配任何字母组成
的序列，包含空序列。本题我没有什么思路，于是借鉴了discuss中一个O(n*n)时间复杂度
的算法，该算法应用动态规划思想。dp初始状态：dp=[True]+[False]*len(s)，其中dp[0]
表示空串或s[:0]只匹配'*'，因此在每次循环中需要修改其值。dp[n]表示子串s[:n]匹配
p中的pattern(0,i)，因此初始全为False表示不匹配空的pattern。
用i循环p，在每次循环中，如果i不等于通配符'*'，那么逆序循环遍历dp(逆序是因为dp[n+1]
将用到dp[n]的结果。即只有在dp[n]匹配pattern(0,i-1)且(i为'?'或s[n]==i)时，
dp[n+1]才匹配到pattern(0,i)，dp[n+1]变为True;
如果i等于通配符'*'，那么只要dp[n-1]=True或dp[n]=[True](此时'*'匹配空串)，dp[n]
就为True。
将p遍历完后，返回dp[-1]即为所求。
'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]* length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (s[n] == i or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]
'''
'''
