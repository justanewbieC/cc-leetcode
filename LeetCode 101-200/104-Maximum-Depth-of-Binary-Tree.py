'''
本题要求求出二叉树的深度。
我借鉴了discuss中的一行代码的解决方案。
map函数为高阶函数，可接受函数作为参数。如map(f,list)表示list中的每个元素都完成一次f函数。
本题用了递归求解，时间复杂度为O(n)。
本题用时56ms，击败77.46%用户。
'''
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #遍历到了所有的叶子节点
        return 1 + max(map(self.maxDepth,(root.left,root.right))) if root else 0
