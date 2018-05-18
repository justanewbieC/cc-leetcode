'''
本题要求给定一个数组，返回数值相加最大的子数组。如[-2,1,-3,4,-1,2,1,-5,4]，应
返回6(4-1+2+1)。
本题可用动态规划求解，题目中又给出了扩展，问是否可以用分治思想解决。dp解法如下:
维护两个变量:maxSum保存加上当前值后子数组的最大值(max(maxSum,maxSum+num));
maxSumTot保存当前下标下子数组的最大值，可以包括当前值，也可以不包括当前值(max(
maxSumTot,maxSum))。遍历完成后返回maxSumTot即可。
本程序时间复杂度为O(n)，用时44ms，击败99.97%用户。
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        maxSum , maxSumTot = float('-inf') , float('-inf')
        for num in nums:
            maxSum = maxSum+num if num < maxSum+num else num
            maxSumTot = maxSumTot if maxSumTot > maxSum else maxSum
        return maxSumTot
'''
分治思想如下:
求得数组中间值，对中间值以左的左数组和中间值以右的右数组分别递归，直到数组长度为1或2.
接着分别求左右数组的maximum，并返回最大值。时间复杂度为O(nlogn)。
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        return self.divide(nums)
        
    def divide(self, nums):
        if len(nums) == 1 : return nums[0]
        if len(nums) == 2 : return max(nums[0], nums[1], nums[0]+nums[1])
        
        mid = len(nums) // 2
        lsum = self.divide(nums[:mid])
        rsum = self.divide(nums[mid+1:])

        msum = nums[mid]
        #完成对左数组maximum的求解
        totsum = msum
        for i in range(mid-1, -1, -1):
            totsum += nums[i]
            msum = max(msum, totsum)
        
        #完成对右数组maximum求解
        totsum = msum
        for i in range(mid+1, len(nums)):
            totsum += nums[i]
            msum = max(msum, totsum)
        return max(lsum, msum, rsum)
