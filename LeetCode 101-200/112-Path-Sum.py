'''
本题要求找到在树中是否存在这样的路径(从根到叶子)，其值加起来等于给定的sum。
我的想法是用递归的方法维护一个pathSum，先左后右递归节点，若pathSum==sum，就返回True。
时间复杂度为O(n)，n为节点的个数。
运行时间为56ms，击败96.19%的用户
'''
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return True if self.recursionSum(root, 0, sum) == True else False
             
    def recursionSum(self, root, pathSum, sum):
        if root:
            pathSum += root.val
            if pathSum == sum and not root.right and not root.left: #一定注意此节点必须为叶子节点
                return True
            else:
                return self.recursionSum(root.left, pathSum, sum) or self.recursionSum(root.right, pathSum, sum)
'''
我在discuss中看到另外一个思路，大体与我的一样，只是他没有额外用到变量pathSum。
他选择用sum-root.val来对sum进行更新，直到sum==root.val。
时间复杂度同样为O(n)。
'''
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.right and not root.left and root.val == sum :
            return True
        else:
            sum -= root.val
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

