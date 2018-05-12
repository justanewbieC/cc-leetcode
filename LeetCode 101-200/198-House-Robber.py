'''
本题给这样一个情景:现有一个街道，街道上的每个房子内都存有一定数量的钱。nums[i]表示
第i栋房子内存的钱。现有一小偷去偷钱，要求不能偷相邻两个房子的钱。求小偷一晚上最多可
以偷多少钱。本题是一个动态规划问题。
可以维护一个maxCountList数组，maxCountList[i]表示从前往后偷，偷到第i个房子最多
能偷多少钱。并维护一个maxCount变量表示当前最多能偷多少钱。遍历nums数组，每次将nums[i]
与maxCountList[-2]相加和maxCount比较，更新maxCount。最后maxCount即为所求。
本题时间复杂度O(n)，运行时间32ms，击败100%用户。
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCountList , maxCount = [] , 0
        for i in range(len(nums)):
            if i > 1 and nums[i] + maxCountList[-2] > maxCount:
                maxCount = nums[i] + maxCountList[-2]
            elif nums[i] > maxCount: #前两栋房子
                maxCount = nums[i]
            maxCountList.append(maxCount)
        return maxCount
