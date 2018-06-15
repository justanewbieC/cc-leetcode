'''
������subsets-I�Ļ�����������һЩ�Ѷ�,�ڸ�����nums�����п��ܻ�����ظ�Ԫ��.
���ֻ���ڵݹ��м����ж���������(�����ǰ������ǰһ��������ͬ,�򲻵ݹ�).
��������ʱ��48ms,����96%�û�.
'''
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, subres = [], []
        self.recursionSubsets(sorted(nums), res, subres)
        return res
    
    def recursionSubsets(self, nums, res, subres):
        res.append(subres)
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i-1] or i == 0:
                self.recursionSubsets(nums[i+1:], res, subres+[nums[i]])

