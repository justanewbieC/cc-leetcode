'''
����Ҫ�󽫶�������ת����������������������������
����Ƚϼ򵥣����õݹ�ķ��������ݹ鵽�Ľڵ�������������������������pythonԪ��
�����ԣ���left,right������������ݹ����������������ؽڵ㡣
����ʱ�临�Ӷ�O(n)������ʱ��36ms������99%�û���
'''
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        return self.recursionTree(root)
    
    def recursionTree(self, root):
        if root.left or root.right:
            root.left , root.right = root.right , root.left
        if root.left : self.recursionTree(root.left)
        if root.right : self.recursionTree(root.right)
        return root
