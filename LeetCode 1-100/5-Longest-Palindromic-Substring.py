'''
本题要求求出一个字符串中的最长回文子串。我首先很自然地想到用个n²的循环就可以
解决此题，但是在测试大点的数据时，运算就会超时。因此我借鉴了discuss中的方法。
观察字符串可以发现，增加遍历字符串的指针i(i+=1)，回文子串的长度只能增加1或2。
如对于'babad' 当i=0时，最大回文串为'b'；i+1后回文串不变；再加1后，回文串变为
'bab'，长度增加2。
因此最大回文串长度(maxLen)初始为1，start初始值为0；移动指针i，如果可构成回文串，
那么就更新maxLen和start；否则不更新。最后返回(start,start+maxLen)。
本题时间复杂度O(n),运行时间76ms，击败98.55%用户。
'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) in [0, 1] : return s
        maxLen , start = 1 , 0
        for i in range(len(s)):
            if i-maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                start = i-maxLen-1
                maxLen += 2
                continue
            if i-maxLen >=0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                start = i-maxLen
                maxLen += 1
        return s[start:start+maxLen]
