'''
给定一个表达式，表达式由数字和符号(+,-,*,/)组成。要求将表达式的值计算出来。
如:["2", "1", "+", "3", "*"]。则可计算得:(2+1)*3=9，输出9即可。
本题可以运用栈这一数据结构。遍历token字符串，如果是数字则将其加入tokenStack栈;
每一个操作符对应栈中的两个元素。碰到操作符则弹出栈顶的两个元素进行计算，并将
计算结果加入tokenStack。遍历完成后，tokenStack中必然只剩下一个数，该数
即为所求。
本题时间复杂度为O(n)，运行时间44ms，击败97.97%用户。
'''
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        tokenStack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit(): #数字(包含负数)
                tokenStack.append(int(token)) #将其变成int型
            else:
                second , first = tokenStack.pop() , tokenStack.pop()
                if token == '+' : tokenStack.append(first+second)
                elif token == '-' : tokenStack.append(first-second)
                elif token == '*' : tokenStack.append(first*second)
                else : tokenStack.append(int(first/second))
        return tokenStack[0]
