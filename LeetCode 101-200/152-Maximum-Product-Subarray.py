'''
�������һ�����飬Ҫ���ҳ����������ֵ��������,������ֵ
����[2,3,-2,4],���Ϊ6(2*3)��
������û��ʲô˼·�������discuss�е�˼�롣
��Ϊ��i��Ԫ�ؿ��������������Ǹ��������i-1���������ֵ��i�󣬿��ܱ�Ϊi�����
����ֵ��Ҳ���ܱ��i����С����ֵ��
�����maxLast,minLast�����i��Ԫ����ǰ���������ֵ��������Сֵ;
��maxCur,minCur���浱ǰ���������ֵ��������Сֵ������maxTol���ɡ�
����ʱ�临�Ӷ�O(n)������ʱ��48ms��
'''
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCur , minCur , maxTol = nums[0] , nums[0] , nums[0]
        for num in nums[1:]:
            maxLast , minLast = maxCur , minCur
            maxCur , minCur = max(num, num*maxLast, num*minLast) , min(num, num*maxLast, num*minLast)
            maxTol = maxTol if maxTol >= maxCur else maxCur
        return maxTol
