'''
本题给定一个数组，要求找出有连乘最大值的子数组,输出最大值
比如[2,3,-2,4],输出为6(2*3)。
本题我没有什么思路，借鉴了discuss中的思想。
因为第i个元素可能是正数可能是负数。因此i-1的最大连乘值乘i后，可能变为i的最大
连乘值，也可能变成i的最小连乘值。
因此用maxLast,minLast保存第i个元素以前的连乘最大值和连乘最小值;
用maxCur,minCur保存当前的连乘最大值和连乘最小值。更新maxTol即可。
本题时间复杂度O(n)，运行时间48ms。
'''
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCur , minCur , maxTol = nums[0] , nums[0] , nums[0]
        for num in nums[1:]:
            maxLast , minLast = maxCur , minCur
            maxCur , minCur = max(num, num*maxLast, num*minLast) , min(num, num*maxLast, num*minLast)
            maxTol = maxTol if maxTol >= maxCur else maxCur
        return maxTol
