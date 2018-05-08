'''
本题要求给定一个字符串s和一个字符串t，在s中寻找包含t中所有元素的最小子串，若没有
则返回空串。并且要求时间复杂度为O(n)。我参考了discuss中的方法，并做了一些改进。
它的思想是。用[I,J]表示已求得的包含t中所有元素的子串，[i,j]表示当前窗口，并用[i,j]
不断更新[I,J]。用need字典保存 在s中需要t中元素各多少个(s中其余元素用负值表示)。
missing表示t中还有多少个元素没有被找到。
比如在示例中s='ADOBECODEBANC',t='ABC'。在开始循环前need={'A':1,'B':1,'C':1}。
遍历到A时，missing变成2，need['A']=0;接着need['D']=need['O']=-1...遍历到第一个
C后missing减为0，进入if not missing。这时J还等于0。因此[I,J]=[i,j]=[0,6](j
从1开始)。接着继续遍历直到再遇到A(可以将need['A']变为-1进入while)，此时说明可以
对[I,J]进行更新。如此进行直到遍历完s中的所有元素。
本题创建字典用时O(n)，查找字典元素用时O(1)，遍历s用时O(n)，因此总时间复杂度O(n)。
运行时间96ms，击败99%用户。
'''
from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need , missing = defaultdict(int) , len(t)# defaultdict可以为key设置默认值
        for _ in t:
            need[_] += 1
        i = I = J = 0
        for j , c in enumerate(s, 1): # j从1开始
            if need[c] > 0 : missing -= 1
            need[c] -= 1
            if not missing:
				#若t中元素的need值小于0，说明它多出现了，因此可以进入循环
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j-i <= J-I:
                    I , J = i , j
        return s[I:J]
