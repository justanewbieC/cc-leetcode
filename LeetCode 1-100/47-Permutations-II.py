'''
本题在上一题的基础上,给定的数组包含重复的元素,要求返回所有不重复的可能组合.
本题只需在上一题的基础上,先将给定的nums数组排序.再增加一个判断条件,即判断
nums[i]是否等于nums[i-1]。
本题运行时间72ms，击败98%用户。
'''
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums : return []
        res , subres = [] , []
        self.recursionPermute(sorted(nums), res, subres)
        return res

    def recursionPermute(self, nums, res, subres):
        if not nums : 
            res.append(subres)
        for i in range(len(nums)):
            if i==0 or (i>0 and nums[i] != nums[i-1]) : 
                self.recursionPermute(nums[:i]+nums[i+1:], res, subres+[nums[i]])
