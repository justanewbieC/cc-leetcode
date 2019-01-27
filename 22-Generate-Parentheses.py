'''
本题给定一个整数n，要求返回包含n对合法的圆括号的所有方案。如给定整数3，
则应返回集合：["((()))","(()())","(())()","()(())","()()()"]。
本题需要用到回溯法(我认为是类似于树的搜索)，因此我想到了递归。递归函数的
参数中有一个absNum表示的是当前字符串中左右括号数量的差值，如'(()'：左
括号比右括号多1个，则absNum为1.当absNum大于0时，每次递归，string可以
加'('，也可以加')'。而当absNum等于0时，则只能添加'('。最后当n=0时，便可
将string加入List中。
本题用时36ms，击败100%用户
'''
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        if n == 1: return ['()']
        stack = []
        self.recursionGenerate('', n, 0, stack)
        return stack
    
    def recursionGenerate(self, string, n, absNum, stack):#absNum为左右括号数量的差值
        if n == 0:
            string += (')'*absNum)
            stack.append(string)
        else:
            if absNum > 0:
                self.recursionGenerate(string+'(', n-1, absNum+1, stack)
                self.recursionGenerate(string+')', n, absNum-1, stack)
            else:
                self.recursionGenerate(string+'(', n-1, absNum+1, stack)
