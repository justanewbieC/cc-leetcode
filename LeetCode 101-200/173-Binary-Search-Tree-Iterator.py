'''
本题要求实现一个BST的迭代器。其next()方法返回BST中的下一个最小值;hasnext()方法
判断BST中是否还有未迭代的元素。
因为对于顺序访问BST中的元素，可以采用中序遍历二叉树的方法。因此可以将非递归的中序
遍历二叉树方法拆分开来。在__init__()中维护一个栈，将root的左子树根节点放入stack中。
显然如果stack中没有元素了，则hasnext()将返回False.
在next中，先弹出栈顶元素，栈顶元素的val就是当前最小值。接着将栈顶元素的right入栈。
对于题中要求next()方法的时间复杂度O(1):显然遍历所有元素时间复杂度为O(n)，遍历完成
需要调用n次next方法，则next()平均时间复杂度为O(1);且stack中最多储存h个元素(h为树高)
，满足空间复杂度O(h)。
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
