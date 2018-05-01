'''
本题要求判断两个二叉树是否为同一棵树(结构相同&值相同)
本题较为简单，用递归即可。
时间复杂度为O(n)，运行时间36ms，击败98.97%用户。
'''
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: #p,q同时为空
            return True
        if (p and not q) or (not p and q) or (p.val != q.val): #p,q一个为空，一个不为空或两个值不同
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
