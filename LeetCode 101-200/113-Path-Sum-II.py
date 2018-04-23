'''
本题在上一题的基础上加大难度,要求打印所有符合条件的路径组成的列表。
我同样准备沿用上一题的思路，将每个元素添加至subres列表，如果遍历到叶子时路径上元素之和等于sum，
则将此列表添入res。这样看似没有问题，但是实际运行出来res中则是两个包含全部元素的列表。
原来在python中，列表是可变对象，故对列表的修改在递归栈的每一个元素中均会体现。因此我在每次递归时，
将原来的传入subres改为传subres的切片，问题得以解决。
时间复杂度为O(n)，但运行时间需要64ms，仅击败79.17%用户。
我认为原因出在切片上，每次创建切片都会耗费额外的内存与时间。
我看了discuss中的解决方法，有的方案传的参是subres+[root.val]，这样可以避免涉及到对象的可变性。运行时间也有了提升。
'''
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res, subres = [] , []
        self.recursionSum(root, 0, sum, res, subres)
        return res
        
    def recursionSum(self, root, pathSum, sum, res, subres):
        if root:
            pathSum += root.val
            subres.append(root.val)
            if pathSum == sum and not root.right and not root.left:
                res.append(subres)
            else:
                self.recursionSum(root.left, pathSum, sum, res, subres[:]) #传入切片
                self.recursionSum(root.right, pathSum, sum, res, subres[:]) #传入切片
