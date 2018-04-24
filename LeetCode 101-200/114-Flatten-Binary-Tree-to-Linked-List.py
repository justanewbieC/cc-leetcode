'''
本题要求将二叉树转换为链表,以右孩子的形式相连。
看过示例后，发现其遍历顺序为先序遍历，于是我采用递归的先序遍历，将遍历的每个节点添加至res列表中。
最后将res列表中的每个节点的left变为None，right变为列表中下一个节点。
本程序时间复杂度为O(n)。运行时间48ms，击败96.10%用户。
'''
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res= []
        self.recursionPreOrder(root, res)
        for index in range(len(res)-1):
            res[index].left = None  #左孩子变为None
            res[index].right = res[index+1] #右孩子变为下一节点
        
    def recursionPreOrder(self, root, res):
        if root:
            res.append(root)
            self.recursionPreOrder(root.left, res)
            self.recursionPreOrder(root.right, res)
