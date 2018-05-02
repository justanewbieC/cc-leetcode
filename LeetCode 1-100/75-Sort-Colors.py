'''
本题是荷兰旗问题，给定一个数组(只出现0或1或2)，要求将其按顺序输出。
要求一次遍历得到结果且使用常数项空间。
本题可使用三个指针，begin指针指向左边第一个非0数，end指针指向右边第一个非2数，cur指针用于遍历。
代码前面的两个while循环我觉得非常有必要，可以省略不必要的交换操作(如[0,0,0,2,1]，可省略前三个交换)
程序时间复杂度为O(n)，运行时间36ms，击败100%用户。
'''
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) in [0,1]:
            return
        begin , end = 0 , len(nums)-1
        while begin < len(nums)-1 and nums[begin] == 0 :#将begin移到左边第一个非0处
            begin += 1
        while end > 1 and nums[end] == 2:#将end移到右边第一个非2处
            end -= 1
        cur = begin
        while cur <= end:
            if nums[cur] == 0: #交换begin与cur，且两个指针均后移
                nums[begin] , nums[cur] = nums[cur] , nums[begin]
                begin , cur = begin+1 , cur+1
            elif nums[cur] == 2: #此处不移动cur是因为cur还可能等于0
                nums[end] , nums[cur] = nums[cur] , nums[end]
                end -= 1
            else: cur += 1 #如果等于1，则不用交换任何值，cur直接加1即可
