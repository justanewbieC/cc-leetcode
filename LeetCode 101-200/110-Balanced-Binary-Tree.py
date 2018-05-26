'''
本题要求判断给定的二叉树是否是平衡二叉树。
平衡二叉树定义:在二叉树中，所有节点的左右子树高度相差小于等于1.
本题可以使用深度优先搜索。用leftDepth记录左子树高度;rightDepth记录右子树高度。
如果左右子树相差大于等于1，返回False;否则返回左右子树高度的最大值。
本题时间复杂度O(n)，运行时间60ms，击败100%用户。
'''
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root : return True
        depth = 0
        return True if self.recursionTree(root, depth) else False
        
    def recursionTree(self, root, depth):
        if root:
            leftDepth = self.recursionTree(root.left, depth+1)
            if not leftDepth: #左子树不满足平衡二叉树的条件
                return False
            else:
                rightDepth = self.recursionTree(root.right, depth+1)
                if not rightDepth: #右子树不满足平衡二叉树的条件
                    return False
                else:
                    return max(leftDepth, rightDepth) if abs(leftDepth-rightDepth) <=1 else False    
        else:
            return depth
