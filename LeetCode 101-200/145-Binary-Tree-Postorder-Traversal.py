'''
本题要求按照后序遍历二叉树，且保存遍历到的值，后序即为(左子树 → 右子树 → 根)，
尽量采用迭代的方式求解。我认为后序比前序，中序稍难些。
我决定给每个节点加入一个标志位flag，如果它的左右孩子被访问过，则将其flag置1。
在循环中，如果栈顶元素没有左右孩子，或它的flag为1，则将其出栈并加入result。
否则将其左右孩子入栈，并将其flag置1。
本题时间复杂度O(n)，击败99.22%用户。  
'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        treeStack , result = [] , []
        if root : treeStack.append([0, root]) #[标志位，根] 标志位表示其子节点是否被访问过
        while treeStack:
            if (not treeStack[-1][1].left and not treeStack[-1][1].right) or treeStack[-1][0] == 1:
                result.append(treeStack.pop()[1].val)      
            else:
                flag , root = treeStack[-1]
                if root.right: treeStack.append([0, root.right]) #标志位初始为0
                if root.left: treeStack.append([0, root.left]) #标志位初始为0
                treeStack[treeStack.index([0, root])] = [1, root] #标志位置1
        return result
