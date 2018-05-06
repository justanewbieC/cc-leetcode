'''
����Ҫ�������������Ԫ�ز�������һ�����飬�������õ����ķ��������
��˿���ά��һ��treeStack�б����ڵ����ڵ�ջ���Ƚ����ڵ����ջ�С�
��ѭ���У��Ƚ�ջ��Ԫ�ص���������result�����У�Ȼ������ѹ���Һ��ӡ����ӡ�
����ʱ�临�Ӷ�ΪO(n)������ʱ��36ms������98.84%�û���
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
