'''
����Ҫ���жϸ����Ķ������Ƿ���ƽ���������
ƽ�����������:�ڶ������У����нڵ�����������߶����С�ڵ���1.
�������ʹ�����������������leftDepth��¼�������߶�;rightDepth��¼�������߶ȡ�
����������������ڵ���1������False;���򷵻����������߶ȵ����ֵ��
����ʱ�临�Ӷ�O(n)������ʱ��60ms������100%�û���
'''
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root : return True
        depth = 0
        return True if self.recursionTree(root, depth) else False
        
    def recursionTree(self, root, depth):
        if root:
            leftDepth = self.recursionTree(root.left, depth+1)
            if not leftDepth: #������������ƽ�������������
                return False
            else:
                rightDepth = self.recursionTree(root.right, depth+1)
                if not rightDepth: #������������ƽ�������������
                    return False
                else:
                    return max(leftDepth, rightDepth) if abs(leftDepth-rightDepth) <=1 else False    
        else:
            return depth
