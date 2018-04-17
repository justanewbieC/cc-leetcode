'''
本题要找第k大的元素。
python中有heapq模块，可以通过heapq.heapify(list)来建一个最小堆，
这样heapq.heappop(list)每次弹出的都是优先级最小的元素。总时间复杂度O(nlogN)。
程序运行时间为44ms，击败94.56%的用户。
'''
import heapq
def findKthLargest(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	heapq.heapify(nums)
	for i in range(len(nums)-k): 
		heapq.heappop(nums)
	return heapq.heappop(nums)

'''
但上题的解法用到了python中已有的模块。
如果不用已有的堆模块，则可以借助快速排序的思想，时间复杂度同样为O(nlogN)。
运行时间同样为44ms。
'''
from random import randint
def findKthLargest(nums, k):
    pivot = randint(0 , len(nums) - 1) #随机产生一个用来比较的数
    left  = [l for l in nums if l < nums[pivot]]
    equal = [e for e in nums if e == nums[pivot]]
    right = [r for r in nums if r > nums[pivot]]

    if k <= len(right): #第K大数在大于随机数的列表
        return findKthLargest(right, k)
    elif (k - len(right)) <= len(equal):
        return equal[0]
    else:
        return findKthLargest(left, k - len(right) - len(equal))
