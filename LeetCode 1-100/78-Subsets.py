'''
�������һ����n����ͬ��������ɵ�nums���֣�Ҫ�󷵻�nums�������п��ܵ������顣
��nums=[1,2,3]
�����[[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]
��������õݹ�+�����������res�������п��ܵ������飻subres���浱ǰ�����н�Ҫ���
��res�����飬��ÿ�εݹ��У����Ƚ�subres��ӵ�res���ٶ���nums�е�ÿ�����֣��ݹ��
�����Ժ��nums����(�������ּ���subres��)��
��������ʱ��44ms������93%�û���
'''
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, subres = [], []
        self.recursionSubres(nums, res, subres)
        return res
    
    def recursionSubres(self, nums, res, subres):
        res.append(subres)
        for i in range(len(nums)):
            self.recursionSubres(nums[i+1:], res, subres+[nums[i]])
