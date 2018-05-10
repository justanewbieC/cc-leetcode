'''
本题在上一题的基础上加大难度，要求打印出所有分割的情况。如:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:["cats and dog","cat sand dog"]
我首先想到了递归的方法，用i去依次遍历s，如果s[:i+1]在wordDict里面，那么就递归
地遍历s[i+1:]，并保存s[:i+1]；直到s[i+1:]为空，用' '.join即可。
但这样的方法在处理形如(s='aaaaa...',wordDict=['a','aa','aaa'..]时会显得力不从心。
于是我借鉴了discuss中的方法。它在递归中维护了一个memo字典，它循环遍历wordDict中
的单词，如果s是以这一单词开头，则递归s[len(word:):]，直到s为空。将单词加入res中，
并且memo[s]=res，将它记录下来，以备以后用到；返回res并用resultOfTheRest接受它。
将当前的word与resultOfTheRest中的元素用空格相连存入res并再加入memo后，返回res。
如此这般递归地返回到初始的调用。这个算法的关键就是memo字典，避免了很多不必要的遍历。
本题运行时间48ms，击败95.77%用户。
'''
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
