'''
本题给定一个BST，并给出这个BST中的两个节点，要求求出这两个节点的最小祖先。
因为BST有这样一个重要性质:左子树的值<根节点的值<右子树的值.
所以可以采用递归的方法:如果p或q的值等于root，或者pq的值一个比root大一个比root小，
则直接返回root；如果两个都比root小，则递归其左子树；如果两个都比root大，则递归其
右子树。
本题时间复杂度O(lgn)，运行时间111ms，击败97.93%用户。
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root : return None
        return self.recursionAncestor(root, p ,q)
        
    def recursionAncestor(self, root, p, q):
        if p == root : return p
        if q == root : return q
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val): return root
        elif p.val < root.val and q.val < root.val : return self.recursionAncestor(root.left, p ,q)
        else : return self.recursionAncestor(root.right, p, q)
