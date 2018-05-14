'''
本题在上一题基础上加大难度。给定一个二叉树和两个节点，求两个节点的最小祖先。
因为二叉树相对于BST是没有规律的。因此我准备采用非递归的方法，中序遍历二叉树。则
中序遍历得到的结果可以当做BST来处理。
首先判断如果p,q两个其中一个是另一个的父亲节点，则直接返回父亲节点。
接着中序遍历二叉树，直到两个节点都访问到。
再像上一问一样递归求解最小祖先。
本题时间复杂度为O(n+lgn)，空间复杂度O(n)。运行时间83ms，击败99.54%用户。
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.left == q or p.right == q: return p
        if q.left == p or q.right == p: return q
        treeStack , inTree , copyRoot , findCount = [] , [] , root , 2
        while (treeStack or root) and findCount != 0 : #中序遍历
            if root:
                treeStack.append(root)
                root = root.left
            else:
                root = treeStack.pop()
                inTree.append(root)
                findCount = findCount - 1 if root == p or root == q else findCount
                root = root.right
        return self.recursionAncestor(inTree, copyRoot, p ,q)
    
    def recursionAncestor(self, inTree, root, p, q):
        if root not in inTree: return self.recursionAncestor(inTree, root.left, p, q) #说明两个节点都在左子树
        index = inTree.index(root)
        if root == p or root == q or (p in inTree[:index] and q in inTree[index+1:]) or (p in inTree[index+1:] and q in inTree[:index]): return root
        elif p in inTree[:index] and q in inTree[:index]: return self.recursionAncestor(inTree[:index], root.left, p, q)
        else: return self.recursionAncestor(inTree[index+1:], root.right, p, q)
