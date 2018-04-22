'''
本题要求以中序的顺序遍历并保存二叉树。有递归和非递归两种实现。
先说非递归:
可以用一个栈来保存结点，如果结点存在，则入栈，并root=root.left。
如果不存在，则出栈，将其添加至结果列表中后，root=root.right。
时间复杂度为O(n)。
运行时间36ms,击败99.45%的用户。
'''
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeStack , result = [] , []
        while root or nodeStack:
            if root:
                nodeStack.append(root)
                root = root.left
            else:
                popRoot = nodeStack.pop()
                result.append(popRoot.val)
                root = popRoot.right
        return result
'''
递归:
递归左子树，直到左子树为空，将其元素加入结果列表后，递归其右子树。
运行时间同样为36ms。
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.recursionTraversal(root, result)
        return result
    
    def recursionTraversal(self, root, result):
        if root:
            self.recursionTraversal(root.left, result)
            result.append(root.val)
            self.recursionTraversal(root.right, result)
