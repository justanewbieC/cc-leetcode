'''
本题要求给定一个由不同数字组成的集合，返回这些数字的所有组合情况。
如输入[1,2,3]，返回[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]。
本题可用递归的backtrace。维护res和subres两个数组。
循环nums数组中的每一个数，对每一个数递归调用除它以外的数组。
如果该次递归中nums为空，则将subres添加入res。
程序时间复杂度为O(n!)，n为nums的长度，运行时间52ms，击败97%用户。
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums : return []
        res , subres = [] , []
        self.recursionPermute(nums, res, subres)
        return res
    
    def recursionPermute(self, nums, res, subres):
        if not nums : 
            res.append(subres)
        for i in range(len(nums)):
			# nums[:i]+nums[i+1:]为除它外的数组
            self.recursionPermute(nums[:i]+nums[i+1:], res, subres+[nums[i]])
