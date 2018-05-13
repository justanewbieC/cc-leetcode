'''
本题在house-robber-I的基础上增大难度。在一个街区里的所有房子组成一个圈。也就是
说第一个房子和最后一个房子是相连的，不能同时偷第一个房子和最后一个房子。
可以第一次求不包含第一个房子最多可以偷多少钱；第二次求不包含最后一个房子最多可以偷
多少钱。取两次的较大值即为所求。
特殊情况是只有一间房子，如果是特殊情况那么就返回它的值即可。
本算法时间复杂度为O(n)，运行时间36ms，击败97.55%用户。
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _rob(nums):
            a , b = 0 , 0
            for i in range(len(nums)):
                a , b = b , max(b, a+nums[i]) #更新最大值。
            return b
        a , b = _rob(nums[:-1]) , _rob(nums[1:])
        return max(a, b) if len(nums) != 1 else nums[0]
