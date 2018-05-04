'''
本题为给定一个中序遍历和一个后序遍历,求出唯一的二叉树。
如中序:[9,3,15,20,7],后序:[9,15,7,20,3]
很显然后序遍历按从后往前的顺序依次为每一层右子树的根。
因此可以同样采用递归的方法，先递归右子树，再递归左子树。
本题时间复杂度为O(n)，运行时间56ms，击败99.46%用户。
'''
class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        dictInorder = {}
        for i, val in enumerate(inorder): #中序字典，方便查找
            dictInorder[val] = i
        start , end = 0 , len(postorder)
        return self.recursionTree(start, end, postorder, dictInorder)
    
    def recursionTree(self, start, end, postorder, dictInorder):
        if start == end:
            return None
        root = TreeNode(postorder.pop())#每次的后序遍历的最后一个元素为根
        rootNum = dictInorder[root.val]
        root.right = self.recursionTree(rootNum+1, end, postorder, dictInorder)
        root.left = self.recursionTree(start, rootNum, postorder, dictInorder)
        return root
