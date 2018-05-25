'''
本题给定一个完全二叉树,求二叉树节点的个数.
本题可以将所有元素遍历一遍,遍历的次数即为二叉树节点的个数,但时间复杂度将为O(n),很差。
效率更高的做法是二分法，思路如下:
假定二叉树可以这样表示[[1],[2,3],[4,5,6]]，则此二叉树第三层有三个元素。
getDepth方法分别求根节点左子树的最左孩子节点和右子树的最左孩子节点。
(1)显然如果leftDepth = rightDepth，则说明它的左子树是满二叉树。可直接将根和左子
树(2**leftDepth)加入结果中，继续递归根的右子树.
(2)如果leftDepth != rightDepth，则说明它的右子树是满二叉树，深度为总深度减1.
可直接将根和右子树(2**rightDepth)加入结果中，继续递归根的左子树.
本算法时间复杂度为O(lgn*lgn)，运行时间88ms，击败100%用户。
'''
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left) #左子树的最左孩子节点
        rightDepth = self.getDepth(root.right) #右子树的最左孩子节点
        if leftDepth == rightDepth: #左子树是满二叉树
            return pow(2, leftDepth) + self.countNodes(root.right)
        else: #右子树是满二叉树
            return pow(2, rightDepth) + self.countNodes(root.left)
    
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
