'''
本题要求给定一个二叉树，以自下而上，自左到右的顺序返回二叉树的所有节点。
如：二叉树[3,9,20,null,null,15,7]，是三层二叉树。则返回[[15,7],[9,20],[3]]。
本题可用递归的思路解决，维护一个表示树的层数的变量和保存结果的数组即可。
初始level=1，开始访问root，如果res的长度小于level，就说明当前level层是第一次访问，
则在res中insert一个数组，接着将root的值放入新建的数组中；接着判断root有无左右孩子，
并递归访问即可。
本题较简单，时间复杂度O(n)，运行时间40ms，击败100%用户。
'''
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = [] 
        if root : self.recursionTree(root, res, 1)
        return res
    
    def recursionTree(self, root, res, level):
        if len(res) < level:
            res.insert(0, [])
        res[-level].append(root.val)
        if root.left:
            self.recursionTree(root.left, res, level+1)
        if root.right:
            self.recursionTree(root.right, res, level+1)
