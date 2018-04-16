'''
找到下一个排列。举个例子：
(1,2,3)→(1,3,2)→(2,1,3)→(2,3,1)→(3,1,2)→(3,2,1)
可以看出排列顺序就是按照数组元素组成的数的大小排列。
因此可以使用两个指针。第一个指针从后往前遍历，用于寻找出第一个非递增的数。
第二个指针同样从后往前遍历，用于将上一步寻找的数与递增序列(从后往前看的)中的某一值置换。
此步完成后，将新的递增序列变为递减序列即可。因为题目要求in-place，故自己写一个my_reverse()函数
注意题目要求do not return anything
'''
def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    r1,r2=len(nums)-1,len(nums)-1 #设置两个从后往前遍历的指针
    while r1>0:
        if nums[r1]<=nums[r1-1]:
            r1-=1
        else: #找到第一个减小的数:nums[r1-1]
            while r2>(r1-1):
                if nums[r2]<=nums[r1-1]:
                    r2-=1
                else: #找到nums[r1-1]应该置换的位置
                    nums[r2],nums[r1-1]=nums[r1-1],nums[r2]
                    my_reverse(nums,r1,len(nums)-1)
                    return None
    my_reverse(nums,0,len(nums)-1)
    return None
                          
def my_reverse(nums,l,r): #递减序列变为递增序列
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
