'''
本题给的数列是在原有序数列的基础上绕某一点旋转的数列。因此数列可以分为两部分，且两部分分别有序。
本题要求时间复杂度为O(log n)。因此可采用二分查找。
维护左右指针l,r，直到l<=r-1。
这样如果nums[l],nums[r]都不是target，就返回-1。
本题运行时间为40ms，击败98.97%的用户。
'''
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0: #如果数列没有元素
		return -1
    l, r, m=0, len(nums)-1, 0 #左，右，中三个指针。
    while l <= r-1:
        m = (l + r) // 2
        if nums[m] < nums[l]:
            if nums[m] <= target <= nums[r]: #查找右半部分
                l = m
            else: #查找左半部分
                r = m - 1
        else:
            if nums[l] <= target <= nums[m]: #查找左半部分
                r = m
            else: #查找右半部分
                l = m + 1
    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    return -1
