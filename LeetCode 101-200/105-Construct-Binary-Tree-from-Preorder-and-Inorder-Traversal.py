'''
本题给出一个先序遍历和一个中序遍历，要求唯一的返回一棵二叉树。
如先序:[3,9,20,15,7];中序:[9,3,15,20,7]
很显然，根是先序遍历的第一个元素，根据根在中序中的位置，又可以把中序划分为左右两棵树。
如此这样递归的求解即可。但ac后发现效率并不高。
'''
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return []
        root = TreeNode(None)
        self.recursionTree(preorder, inorder, root)
        return root
        
    def recursionTree(self, preorder, inorder, root):
        root.val = preorder[0]
        rootNum = inorder.index(preorder[0]) #找出根在中序中的位置
        if rootNum != 0: #可以递归左子树的条件
            root.left = TreeNode(None)
            self.recursionTree(preorder[1:1+rootNum], inorder[:rootNum], root.left)
        if rootNum < len(preorder) - 1: #可以递归右子树的条件
            root.right = TreeNode(None)
            self.recursionTree(preorder[1+rootNum:], inorder[rootNum+1:], root.right)
'''
我在discuss中发现了一个优化的解法，思路基本相同，但他求解根位置的时候用了dict这一数据结构，
这样查找根的时间复杂度为O(1)，而不是列表的O(n)。而且这个算法还没有创建
TreeNode(None)的过程，没有对列表的切片。ac后发现速度提升4倍。
'''
class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    # 12:00
    def buildTree(self, preorder, inorder):
        dicinorder = {}
        for i,val in enumerate(inorder):
            dicinorder[val] = i
        start, end = 0, len(inorder)
        return self.helper(start, end, preorder, dicinorder)
    
    def helper(self, start, end, preorder, dicinorder):
        if start == end:
            return None
        root = TreeNode(preorder.pop(0))
        inorderIndex = dicinorder[root.val]
        root.left = self.helper(start, inorderIndex, preorder, dicinorder)
        root.right = self.helper(inorderIndex+1, end, preorder, dicinorder)
        return root
