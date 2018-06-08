'''
��������һ��Ļ�����,��������������ظ���Ԫ��,Ҫ�󷵻����в��ظ��Ŀ������.
����ֻ������һ��Ļ�����,�Ƚ�������nums��������.������һ���ж�����,���ж�
nums[i]�Ƿ����nums[i-1]��
��������ʱ��72ms������98%�û���
'''
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums : return []
        res , subres = [] , []
        self.recursionPermute(sorted(nums), res, subres)
        return res

    def recursionPermute(self, nums, res, subres):
        if not nums : 
            res.append(subres)
        for i in range(len(nums)):
            if i==0 or (i>0 and nums[i] != nums[i-1]) : 
                self.recursionPermute(nums[:i]+nums[i+1:], res, subres+[nums[i]])
