'''
本题要求给定一棵满二叉树，要求将每一个节点的next指向其右边
第一个兄弟节点，若没有就指向NULL(默认为NULL)，要求只能使用
额外的常数空间。我参考了discuss中的方法，该方法需维护一个prev变量，
其保存左子树的右孩子节点。它的next指向右子树的左孩子节点。且算法是按层次遍历节点。
因为这是满二叉树，故不需考虑其他情况。
本题额外使用空间O(1)，时间复杂度为O(n)，运行时间为76ms，击败97.29%用户。
'''
class Solution:
    # @param root, a tree link node
    # @return nothing
    # 本算法是用上一层的节点来判断如何完成本层的next
    def connect(self, root):
        if not root: return
        while root.left: #遍历直到最后一层
            cur = root.left #光标指向上一层的左孩子节点(即当前层)
            prev = None #保存左子树的右孩子节点
            while root: #直到上一层遍历完成
                if prev: prev.next = root.left #完成左右子树间next的更改
                root.left.next = root.right
                prev = root.right
                root = root.next #root变为上一层的下一个节点
            root = cur #root移向下一层
