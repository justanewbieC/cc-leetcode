'''
本题在上一题(153)的基础上加大难度，在数组中允许有相同的元素。因此如果沿用上一题
的解法，当nums[mid]==nums[len(nums)-1]时，将无法判断是移动left还是right。
如[3,1,3]:第一次nums[mid]=1<3,right=mid，第二次nums[mid]=3，此时应该left右移。
再如[3,1,2,2,2]:第一次nums[mid]=2，而此时却应该right左移。
因此不妨将比较对象换为nums[right]，当等于时，只用让right左移一位即可。
本题运行时间为40ms，击败100%用户。
'''
def findMin(self, nums):
    left , right , mid = 0 , len(nums)-1 , 0
    while left < right :
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1
    return nums[left]
