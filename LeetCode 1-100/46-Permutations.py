'''
����Ҫ�����һ���ɲ�ͬ������ɵļ��ϣ�������Щ���ֵ�������������
������[1,2,3]������[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]��
������õݹ��backtrace��ά��res��subres�������顣
ѭ��nums�����е�ÿһ��������ÿһ�����ݹ���ó�����������顣
����ôεݹ���numsΪ�գ���subres�����res��
����ʱ�临�Ӷ�ΪO(n!)��nΪnums�ĳ��ȣ�����ʱ��52ms������97%�û���
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums : return []
        res , subres = [] , []
        self.recursionPermute(nums, res, subres)
        return res
    
    def recursionPermute(self, nums, res, subres):
        if not nums : 
            res.append(subres)
        for i in range(len(nums)):
			# nums[:i]+nums[i+1:]Ϊ�����������
            self.recursionPermute(nums[:i]+nums[i+1:], res, subres+[nums[i]])
