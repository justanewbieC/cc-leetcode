'''
������house-robber-I�Ļ����������Ѷȡ���һ������������з������һ��Ȧ��Ҳ����
˵��һ�����Ӻ����һ�������������ģ�����ͬʱ͵��һ�����Ӻ����һ�����ӡ�
���Ե�һ���󲻰�����һ������������͵����Ǯ���ڶ����󲻰������һ������������͵
����Ǯ��ȡ���εĽϴ�ֵ��Ϊ����
���������ֻ��һ�䷿�ӣ���������������ô�ͷ�������ֵ���ɡ�
���㷨ʱ�临�Ӷ�ΪO(n)������ʱ��36ms������97.55%�û���
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _rob(nums):
            a , b = 0 , 0
            for i in range(len(nums)):
                a , b = b , max(b, a+nums[i]) #�������ֵ��
            return b
        a , b = _rob(nums[:-1]) , _rob(nums[1:])
        return max(a, b) if len(nums) != 1 else nums[0]
