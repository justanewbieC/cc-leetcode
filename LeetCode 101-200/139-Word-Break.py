'''
本题给定一个不为空的字符串和一个包含若干单词的字符串列表。判断字符串是否可以被分割
为字符串列表中的字符(一个或多个)。列表中的单词可重复使用多次且列表中无重复单词。
本题是一道动态规划问题，应用动态规划思想，用ok[i]来记录s[:i]是否可以分割为列表中
的单词。采用set(words)可以使查找单词的时间复杂度降为O(1)。word_max_len记录了
列表中单词的最大长度，以此可以减少不必要的遍历。
本题的时间复杂度为O(n²)，运行时间36ms，击败100%用户。
'''
def wordBreak(self, s, words):
    ok, words_set, word_max_len = [True], set(words), len(max(words, key=len)) if words else 0
    for i in range(1, len(s) + 1):
		#因为bool类型是不可迭代对象，因此在后面加","，让它变成一个元组。
        ok += any(ok[j] and s[j:i] in words_set for j in range(max(0, i - word_max_len), i)),
    return ok[-1]
  
'''
本题在discuss中还有一个更一般化的解法。用列表d表示s[:i+1]是否可被分割，并将d的初始值
全部设为false。s[:i+1]可行的条件是这个单词在字符串s中的起始位置也是True，或它是
第一个True。如"leetcode":d[3]=True，因为它是第一个True；d[7]=True是因为d[3]也是True。
''' 
def wordBreak(self, s, words):
    d = [False] * len(s)    
    for i in range(len(s)):
        for w in words:
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
    return d[-1]
