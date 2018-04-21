'''
本题要判断最后一个下标是否可达。
如:[2,3,1,1,4]可达：第二个元素可到达最后一个元素。
如:[3,2,1,0,4]不可达：虽然可到达倒数第二个元素，但不可到达最后一个元素。
本题可采用贪心的思想，即维护一个maxjump变量，每一个下标都跳到能跳到的最远距离。
时间复杂度为O(n)。
本题用时52ms，击败80.88%的用户。
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index , maxjump = 0 , 0
        for index in range(len(nums)) :
            if index > maxjump:  #说明此下标不可达
                return False
            maxjump = max(index + nums[index] , maxjump)
            if maxjump >= len(nums) - 1:
                return True
        return maxjump >= len(nums) - 1
