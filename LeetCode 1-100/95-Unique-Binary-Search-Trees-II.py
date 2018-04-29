'''
本题在96题的基础上加大难度，对于给定的n，要求打印出全部异构的BST。
如:输入: 3
输出:[[1,null,3,2],[3,2,null,1],[3,1,null,null,2],[2,1,3],[1,null,2,null,3]]
其中列表的每一个列表元素用TreeNode的形式表示。
本题我在discuss中寻找了优秀的解题算法，它的思路大致如下:
递归求解，函数的参数为start，end。如果start==end(即节点的左子树或右子树为空)，那么就
返回None。接着从start到end遍历数n，l相当于96题中的左子树，r相当于右子树。
r嵌套在l中就表示96题的result[i]=左子树的个数*右子树的个数。分别对l与r用递归，则相当于
求出左右子树的所有情况。node就是根i，node的左子树是l，右子树是r，最后将node添入result。
本题运行时间68ms，击败90.04%用户。
'''
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.recursionTree(1,n+1)
    
    def recursionTree(self, start, end):
        if start == end: #左/右子树为空
            return None
        result = []
        for i in range(start, end):
            for l in self.recursionTree(start, i) or [None]: #递归左子树
                for r in self.recursionTree(i+1, end) or [None]: #递归右子树
                    node = TreeNode(i)
                    node.left , node.right = l , r
                    result.append(node)
        return result
