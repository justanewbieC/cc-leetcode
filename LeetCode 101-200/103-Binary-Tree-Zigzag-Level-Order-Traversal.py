'''
本题要求以zig-zag的形式遍历树，如输入[3,9,20,null,null,15,7]，则
返回[[3],[20,9],[15,7]]，其中第二层反序。本题的思路与102题层次遍历类似。
用递归的方法，维护level(树的高度)。如果level是偶数，则应该正序添加；如果
level是奇数则应该用逆序添加(我选择用列表的insert实现，如果没有题目要求，
则可用deque实现，效率更高)。本题时间复杂度O(n)，运行时间40ms，击败98.04%用户。
'''
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.recursionTree(root, 0, res)
        return res
    
    def recursionTree(self, root, level, res):
        if root:
            if len(res) < level+1: #这一层第一个节点出现
                res.append([])
            if level % 2 == 0: #偶数层
                res[level].append(root.val)
            else: #奇数层
                res[level].insert(0,root.val)
            self.recursionTree(root.left, level+1, res)
            self.recursionTree(root.right, level+1, res)
