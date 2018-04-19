'''
本题要求按照树的层次分组输出每层的内容。
本题可采用先序遍历，递归实现，且需要维护层数，时间复杂度O(n)
本题用时40ms,击败100%的用户。
'''
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        self.preOrder(root, 0, res) #初始层次为0
        return res
         
    def preOrder(self, root, level, res):
        if root:
            if len(res) < level + 1: #本层数据第一次出现，创建空数组
                res.append([])
            res[level].append(root.val)
            self.preOrder(root.left, level+1 ,res) #先序遍历，遍历左子树
            self.preOrder(root.right, level+1, res)

'''
还有一个巧妙的解法，用到了deque。队列中的元素为元组，元组第一个元素为层数，第二个是结点。
对于队列，pop()、append()的时间复杂度均为O(1)
d.get(key,default=None) #在字典中寻找键为key的值，若没有，默认返回None。
此解法运行时间稍慢(每个元素都pop和append)
'''
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque([(0,root)])
        d = {}
        while queue:
            depth , root = queue.popleft()
            if root:
                d[depth] = d.get(depth , []) + [root.val]
                queue += (depth+1 , root.left) , (depth+1 , root.right)
        return [d[depth] for depth in d.keys()]
