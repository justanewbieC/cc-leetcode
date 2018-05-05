'''
本题要求给定两个有序数组(长度分别为m与n),找出两个数组的中位数.且要求时间复杂度为O(log(m+n))
要想求得本题,需要知道这一性质.如有有序数组A,B(元素互不相等),且A的长度小于B的长度,A,B组成C。
如果要求C中第K大的元素,则:
(1)若A[k/2-1]<B[k/2-1]，则A[k/2-1]<C[k-1]。
可用反证法证明。假设A[k/2-1]>C[k-1]，则A[k/2-1]至少为第K+1大元素。又因为A[k/2-1]<B[k/2-1]，
则B[k/2-1]至少为第K+2大元素。又因为A，B有序，则A中有k/2-1个元素比A小，B中有k/2-1个元素比B小。
则至多共有k/2-1+k/2-1+1=k-1个元素比B小，说明B至多为第K大元素，与假设矛盾。
(2)若A[k/2-1]==B[k/2-1]，则A[k/2-1]==B[k/2-1]==C[k-1]
因此若A[k/2-1]<B[k/2-1]，则可一次性删除k/2个元素，满足时间复杂度要求。
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len=len(nums1)+len(nums2)
        if total_len%2==1: # 如果总长度为奇数，则求最中间数即可
            return float(self.findkth(nums1,nums2,total_len//2+1))
        else: #如果总长度为偶数，则求最中间两个数
            return float((self.findkth(nums1,nums2,total_len//2)+self.findkth(nums1,nums2,total_len//2+1))/2)
        
    def findkth(self,nums1,nums2,k): #寻找第k大元素
        if len(nums1)>len(nums2): #假定第一个数组总比第二个数组小
            return self.findkth(nums2,nums1,k)
        if len(nums1)==0: 
            return nums2[k-1]
        if k==1:
            return min(nums1[0],nums2[0])
        i=min(k//2,len(nums1))
        j=k-i
        if nums1[i-1]<nums2[j-1]:
            return self.findkth(nums1[i:],nums2,k-i)
        elif nums1[i-1]>nums2[j-1]:
            return self.findkth(nums1,nums2[j:],k-j)
        else:
            return nums1[i-1]
