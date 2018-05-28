'''
本题要求将二叉树反转。即将二叉树的左右子树互换。
本题比较简单，可用递归的方法。若递归到的节点有左子树或右子树，则利用python元组
的特性，将left,right互换。后继续递归其左右子树并返回节点。
本题时间复杂度O(n)，运行时间36ms，击败99%用户。
'''
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        return self.recursionTree(root)
    
    def recursionTree(self, root):
        if root.left or root.right:
            root.left , root.right = root.right , root.left
        if root.left : self.recursionTree(root.left)
        if root.right : self.recursionTree(root.right)
        return root
