'''
本题要求先序遍历树的元素并保存入一个数组，尽量采用迭代的方法解决。
因此可以维护一个treeStack列表用于当做节点栈。先将根节点放入栈中。
在循环中，先将栈顶元素弹出并放入result数组中，然后依次压入右孩子、左孩子。
本题时间复杂度为O(n)，运行时间36ms，击败98.84%用户。
'''
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        treeStack , result = [] , []
        if root : treeStack.append(root)
        while treeStack:
            root = treeStack.pop()
            result.append(root.val)
            if root.right: treeStack.append(root.right)
            if root.left: treeStack.append(root.left)
        return result
