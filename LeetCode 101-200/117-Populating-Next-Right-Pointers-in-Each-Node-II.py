'''
��������һ��Ļ����ϼӴ��Ѷȣ�������������һ��Ϊ����������
����ͬ��Ҫ�����ÿһ���ڵ�ĵ�һ�����ֵܽڵ�,û�оͷ���NULL(Ĭ��ΪNULL)��
����ͬ����Ҫά��prevΪͬ������������һ���ֵܽڵ����ڵ㡣
��Ϊ������������������Ҫ���⿼����������
(1)�ýڵ������Һ��ӽڵ㡣��prev.next=root.left,left.next=right,prev=right
(2)�ýڵ�ֻ�����ӽڵ㡣��prev.next=root.left,�ٽ�prev��Ϊroot.left
(3)�ýڵ�ֻ���Һ��ӽڵ㡣��prev.next=root.right,�ٽ�prev��Ϊroot.right
(4)�ýڵ�ΪҶ�ӽڵ㡣�޲���
����ͬ���迼�Ǳ�����ò��root��ѡ��Ӧѡ��������ӻ��Һ��ӵĽڵ�Ϊroot��
���������O(1)�ռ䣬ʱ�临�Ӷ�O(n).����ʱ��89ms������97.41%�û���
'''
def connect(self, root):
    if not root:return None
    while root.left or root.right:
        cur = root.left if root.left else root.right #��������ӣ��򽫹���������
        prev = None
        while root:
            if root.left: #������
                if prev: prev.next = root.left
                if root.right: #���Һ���
                    root.left.next = root.right
                    prev = root.right
                else: #���Һ���
                    prev = root.left
            else: #������
                if root.right: #���Һ���
                    if prev: prev.next = root.right
                    prev = root.right
            root = root.next
        root = cur
        while root.next and not root.left and not root.right : #ѡ����ʵ�root
            root = root.next
