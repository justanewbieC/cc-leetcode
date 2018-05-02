'''
����Ҫ�󻯼���������б���ظ����֡���[[1,3],[2,6],[8,10],[15,18]]
����[[1,6],[8,10],[15,18]]����Ϊ3�غ���[2,6]�С�
���Ȱ����ҵ��뷨д����û��ac�������ҽ����discuss�е��㷨��
���Ƚ��б���Interval�е�start����Ȼ������б��е�ÿһ��Ԫ�أ�ά��res�б�
���interval.start<=res[-1].end��������res[-1].end��
����ʱ�临�Ӷ�ΪO(nlogn+n)(����+����)������ʱ��60s������100%�û���
'''
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for interval in sorted(intervals, key = lambda k: k.start): #��Ϊ����Ԫ�ز�һ������
            if res and interval.start <= res[-1].end:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval) #ֱ�����interval
        return res
