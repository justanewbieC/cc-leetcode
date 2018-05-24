'''
����Ҫ��ʵ��һ��BST�ĵ���������next()��������BST�е���һ����Сֵ;hasnext()����
�ж�BST���Ƿ���δ������Ԫ�ء�
��Ϊ����˳�����BST�е�Ԫ�أ����Բ�����������������ķ�������˿��Խ��ǵݹ������
����������������ֿ�������__init__()��ά��һ��ջ����root�����������ڵ����stack�С�
��Ȼ���stack��û��Ԫ���ˣ���hasnext()������False.
��next�У��ȵ���ջ��Ԫ�أ�ջ��Ԫ�ص�val���ǵ�ǰ��Сֵ�����Ž�ջ��Ԫ�ص�right��ջ��
��������Ҫ��next()������ʱ�临�Ӷ�O(1):��Ȼ��������Ԫ��ʱ�临�Ӷ�ΪO(n)���������
��Ҫ����n��next��������next()ƽ��ʱ�临�Ӷ�ΪO(1);��stack����ഢ��h��Ԫ��(hΪ����)
������ռ临�Ӷ�O(h)��
'''
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        root = node.right
        while root:
            self.stack.append(root)
            root = root.left
        return node.val
