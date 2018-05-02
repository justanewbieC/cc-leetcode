'''
本题要求化简给定数组列表的重复部分。如[[1,3],[2,6],[8,10],[15,18]]
返回[[1,6],[8,10],[15,18]]。因为3重合在[2,6]中。
我先按照我的想法写，但没有ac。于是我借鉴了discuss中的算法。
他先将列表按照Interval中的start排序，然后遍历列表中的每一个元素，维护res列表。
如果interval.start<=res[-1].end，将更新res[-1].end。
本题时间复杂度为O(nlogn+n)(排序+遍历)，运行时间60s，击败100%用户。
'''
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for interval in sorted(intervals, key = lambda k: k.start): #因为所给元素不一定有序
            if res and interval.start <= res[-1].end:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval) #直接添加interval
        return res
