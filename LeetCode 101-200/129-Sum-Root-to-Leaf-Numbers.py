'''
本题给定一棵二叉树包含数字0-9.每一个根到叶子的路径都可以表示一个数字。比如根到叶子
的路径为1->2->3，就代表数字123.要求找到所有路径，并求得路径所表示的数字之和。
本题显然是一个深度优先搜索，可以采用递归的方法解决。
维护一个nodeSum代表当前路径的数字，pathSum代表路径数字总和。
在每次递归中，先更新nodeSum的值，即nodeSum = nodeSum* 10 +root.val
如果递归到的节点没有孩子节点，则表明它是叶子节点。将其nodeSum的值加到pathSum中，
返回pathSum即可。如此递归根的左右子树即可完成本题。
本题时间复杂度为O(n)，运行时间40ms，击败97%用户。 
'''
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeSum , pathSum = 0 , 0
        return self.recursionTree(root, nodeSum, pathSum)
        
    def recursionTree(self, root, nodeSum, pathSum):
        if root:
            nodeSum = nodeSum* 10 + root.val 
            if not (root.left or root.right):
                return pathSum + nodeSum
            return self.recursionTree(root.left, nodeSum, pathSum) + self.recursionTree(root.right, nodeSum, pathSum)
        else: return pathSum
