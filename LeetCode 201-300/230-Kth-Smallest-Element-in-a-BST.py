'''
本题要求在BST中寻找第k小的元素.因为对于BST来说,中序遍历可以遍历到一个有序数列.
因此可以采用非递归的中序遍历,每次访问一个元素时,k-=1.直到k==0,将这个元素返回即可.
时间复杂度O(n),运行时间60ms,击败100%用户。
follow up:如果这个BST经常调整(增/删),或经常需要寻找第k小元素,可以如何优化算法？
我觉得可以增加一个列表用于存放遍历到的数。这样可以将每次的k与列表长度比较,可有一定
的优化。
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
