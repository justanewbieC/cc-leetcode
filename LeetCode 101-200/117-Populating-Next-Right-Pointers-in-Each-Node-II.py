'''
本题在上一题的基础上加大难度，所给二叉树不一定为满二叉树。
本题同样要求求出每一个节点的第一个右兄弟节点,没有就返回NULL(默认为NULL)。
本题同样需要维护prev为同层两个子树间一对兄弟节点的左节点。
因为不是满二叉树，所以要额外考虑许多情况。
(1)该节点有左右孩子节点。则prev.next=root.left,left.next=right,prev=right
(2)该节点只有左孩子节点。则prev.next=root.left,再将prev变为root.left
(3)该节点只有右孩子节点。则prev.next=root.right,再讲prev变为root.right
(4)该节点为叶子节点。无操作
本题同样需考虑遍历完该层后，root的选择，应选择具有左孩子或右孩子的节点为root。
本题额外需O(1)空间，时间复杂度O(n).运行时间89ms，击败97.41%用户。
'''
def connect(self, root):
    if not root:return None
    while root.left or root.right:
        cur = root.left if root.left else root.right #如果有左孩子，则将光标放至左孩子
        prev = None
        while root:
            if root.left: #有左孩子
                if prev: prev.next = root.left
                if root.right: #有右孩子
                    root.left.next = root.right
                    prev = root.right
                else: #无右孩子
                    prev = root.left
            else: #无左孩子
                if root.right: #有右孩子
                    if prev: prev.next = root.right
                    prev = root.right
            root = root.next
        root = cur
        while root.next and not root.left and not root.right : #选择合适的root
            root = root.next
