'''
本题给定一个由n个不同的数字组成的nums数字，要求返回nums数组所有可能的子数组。
如nums=[1,2,3]
输出：[[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]
本题可以用递归+回溯来解决。res保存所有可能的子数组；subres保存当前函数中将要添加
入res的数组，在每次递归中，首先将subres添加到res，再对于nums中的每个数字，递归该
数字以后的nums即可(将该数字加入subres中)。
本题运行时间44ms，击败93%用户。
'''
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, subres = [], []
        self.recursionSubres(nums, res, subres)
        return res
    
    def recursionSubres(self, nums, res, subres):
        res.append(subres)
        for i in range(len(nums)):
            self.recursionSubres(nums[i+1:], res, subres+[nums[i]])
