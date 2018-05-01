'''
本题要求对于给定的二叉树，判断它是否是BST。
通过BST定义可知，如果二叉树是BST，则其中序遍历后的结果为一个升序序列。
因此可以用非递归的方式中序遍历二叉树，res数组存放遍历过得结果。
如果root.val>res[-1]，就将此元素添加至res，否则返回True。
本题时间复杂度为O(n)，运行时间52ms，击败100%用户。
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        treeStack , res = [] , []
        while root or treeStack:
            if root:
                treeStack.append(root) #如果结点存在，则将其先入栈
                root = root.left
            else:
                root = treeStack.pop() #如果结点不存在，则将栈顶元素弹出
                if res:
                    if root.val > res[-1]: res.append(root.val) #判断是否满足BST的定义
                    else: return False
                else: res.append(root.val)
                root = root.right
        return True
