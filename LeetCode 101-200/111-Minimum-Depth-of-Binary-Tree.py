'''
本题给定一个二叉树，要求返回根到叶子的最短距离，即树的最小深度。
本题可以用深度优先搜索，维护两个变量 depth和 minDepth。
depth代表根到当前节点的路径长度，minDepth代表遍历过的根-叶子节点的最短距离。
对左右子树分别递归，直到碰到叶子节点，返回minDepth即可。
本题时间复杂度为O(n),运行时间56ms，击败93%用户。
'''
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root : return 0
        depth , minDepth = 0 , float('inf')
        return self.recursionTree(root, depth, minDepth)
    
    def recursionTree(self, root, depth, minDepth):
        if not (root.left or root.right):
            return depth+1 if depth+1 < minDepth else minDepth
        if root.left: minDepth = self.recursionTree(root.left, depth+1, minDepth)
        if root.right: minDepth = self.recursionTree(root.right, depth+1, minDepth)
        return minDepth
