'''
本题给定一个二叉树，现假设站在树的右边看。求能看到的节点的集合(从上往下看)。
本题可以使用非递归的广度优先搜索的方法。nodeStack保存要遍历的节点，rightSide保存
从右边看到的节点。nodeStack中每次添加的元素为[level,root]，level为root所在的
层数。如果当前节点的下一个元素的level为本level+1或者nodeStack中无节点，就说明
当前节点为当前层最右端的节点，直接将其加入rightSide。
本题时间复杂度为O(n)，运行时间44ms，击败95%用户。
'''
from collections import deque
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeStack , rightSide = deque() , []
        if root : nodeStack.append([0, root])
        while nodeStack:
            level, root = nodeStack.popleft()
            if not nodeStack or nodeStack[0][0] == level+1:
                rightSide.append(root.val)
            if root.left : nodeStack.append([level+1, root.left])
            if root.right : nodeStack.append([level+1, root.right])
        return rightSide
