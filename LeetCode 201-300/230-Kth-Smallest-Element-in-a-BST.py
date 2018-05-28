'''
����Ҫ����BST��Ѱ�ҵ�kС��Ԫ��.��Ϊ����BST��˵,����������Ա�����һ����������.
��˿��Բ��÷ǵݹ���������,ÿ�η���һ��Ԫ��ʱ,k-=1.ֱ��k==0,�����Ԫ�ط��ؼ���.
ʱ�临�Ӷ�O(n),����ʱ��60ms,����100%�û���
follow up:������BST��������(��/ɾ),�򾭳���ҪѰ�ҵ�kСԪ��,��������Ż��㷨��
�Ҿ��ÿ�������һ���б����ڴ�ű������������������Խ�ÿ�ε�k���б��ȱȽ�,����һ��
���Ż���
'''
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nodeStack = []
        while root or nodeStack:
            if root:
                nodeStack.append(root)
                root = root.left
            else:
                root = nodeStack.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
