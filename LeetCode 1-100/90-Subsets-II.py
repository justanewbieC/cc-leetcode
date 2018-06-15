'''
本题在subsets-I的基础上增加了一些难度,在给定的nums数组中可能会出现重复元素.
因此只需在递归中加入判断条件即可(如果当前数字与前一个数字相同,则不递归).
本题运行时间48ms,击败96%用户.
'''
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, subres = [], []
        self.recursionSubsets(sorted(nums), res, subres)
        return res
    
    def recursionSubsets(self, nums, res, subres):
        res.append(subres)
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i-1] or i == 0:
                self.recursionSubsets(nums[i+1:], res, subres+[nums[i]])

