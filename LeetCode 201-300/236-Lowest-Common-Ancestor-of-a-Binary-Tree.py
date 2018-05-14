'''
��������һ������ϼӴ��Ѷȡ�����һ���������������ڵ㣬�������ڵ����С���ȡ�
��Ϊ�����������BST��û�й��ɵġ������׼�����÷ǵݹ�ķ����������������������
��������õ��Ľ�����Ե���BST������
�����ж����p,q��������һ������һ���ĸ��׽ڵ㣬��ֱ�ӷ��ظ��׽ڵ㡣
�������������������ֱ�������ڵ㶼���ʵ���
������һ��һ���ݹ������С���ȡ�
����ʱ�临�Ӷ�ΪO(n+lgn)���ռ临�Ӷ�O(n)������ʱ��83ms������99.54%�û���
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
        while (treeStack or root) and findCount != 0 : #�������
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
        if root not in inTree: return self.recursionAncestor(inTree, root.left, p, q) #˵�������ڵ㶼��������
        index = inTree.index(root)
        if root == p or root == q or (p in inTree[:index] and q in inTree[index+1:]) or (p in inTree[index+1:] and q in inTree[:index]): return root
        elif p in inTree[:index] and q in inTree[:index]: return self.recursionAncestor(inTree[:index], root.left, p, q)
        else: return self.recursionAncestor(inTree[index+1:], root.right, p, q)
