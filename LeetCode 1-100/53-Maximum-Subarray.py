'''
����Ҫ�����һ�����飬������ֵ������������顣��[-2,1,-3,4,-1,2,1,-5,4]��Ӧ
����6(4-1+2+1)��
������ö�̬�滮��⣬��Ŀ���ָ�������չ�����Ƿ�����÷���˼������dp�ⷨ����:
ά����������:maxSum������ϵ�ǰֵ������������ֵ(max(maxSum,maxSum+num));
maxSumTot���浱ǰ�±�������������ֵ�����԰�����ǰֵ��Ҳ���Բ�������ǰֵ(max(
maxSumTot,maxSum))��������ɺ󷵻�maxSumTot���ɡ�
������ʱ�临�Ӷ�ΪO(n)����ʱ44ms������99.97%�û���
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        maxSum , maxSumTot = float('-inf') , float('-inf')
        for num in nums:
            maxSum = maxSum+num if num < maxSum+num else num
            maxSumTot = maxSumTot if maxSumTot > maxSum else maxSum
        return maxSumTot
'''
����˼������:
��������м�ֵ�����м�ֵ�������������м�ֵ���ҵ�������ֱ�ݹ飬ֱ�����鳤��Ϊ1��2.
���ŷֱ������������maximum�����������ֵ��ʱ�临�Ӷ�ΪO(nlogn)��
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        return self.divide(nums)
        
    def divide(self, nums):
        if len(nums) == 1 : return nums[0]
        if len(nums) == 2 : return max(nums[0], nums[1], nums[0]+nums[1])
        
        mid = len(nums) // 2
        lsum = self.divide(nums[:mid])
        rsum = self.divide(nums[mid+1:])

        msum = nums[mid]
        #��ɶ�������maximum�����
        totsum = msum
        for i in range(mid-1, -1, -1):
            totsum += nums[i]
            msum = max(msum, totsum)
        
        #��ɶ�������maximum���
        totsum = msum
        for i in range(mid+1, len(nums)):
            totsum += nums[i]
            msum = max(msum, totsum)
        return max(lsum, msum, rsum)
