'''
本题给定一个数组，数组原来是有序的，但在输入时数组绕某一点旋转过。
如原数组[1,2,3,4,5,6,7]，可能变为[4,5,6,7,1,2,3]。让求出数组的最小元素
本题可以采用二分法，每次得到的nums[mid]与nums[0]或nums[len(nums)-1]比。
但是我认为本题有几个特殊情况，如输入数组仍然升序，或输入数组只有两个元素，因此
我认为拿nums[mid]与nums[len(nums)-1]比更为合适。如果nums[mid]>nums[len(nums)-1]，
则最小的数只可能在nums[mid]的右边出现，若小于则只能在mid及mid左边出现。
本题时间复杂度为O(logN)，运行时间36ms，击败100%用户。
'''
def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left , right , mid = 0 , len(nums)-1 , 0
    while left < right :
        mid = (left + right) // 2
        if nums[mid] > nums[len(nums)-1]:
            left = mid + 1
        elif nums[mid] < nums[len(nums)-1]:
            right = mid
    return nums[left]
