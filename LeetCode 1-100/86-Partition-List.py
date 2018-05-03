'''
本题要求给定一个链表和一个数(x),将链表按数字大小分成两部分.比x小的放在前面,其余放在
后面,且在两个划分中,结点原本的先后顺序不变。
如1 → 4 → 3 → 2 → 5 → 2，x=3.划分后为:1 → 2 → 2 → 4 → 3 → 5.
本题我用三个指针完成遍历。firstGreater指针用于找到第一个大于等于x的数；
cur指针为遍历链表的指针，当cur.next.val<x时，将cur.next删除(cur.next=cur.next.next)；
newHead为一个新建的链表用于保存划分，newCur指向newHead，然后进行移动。当cur指针
遍历完成后，newCur指向firstGreater即可。
本题时间复杂度为O(n)，运行时间44ms，击败96.39%用户。
'''
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next: #链表无结点或1个结点
            return head
        newHead , cur = ListNode(None) , ListNode(None) 
        cur.next , newCur , firstGreater = head , newHead , head #cur.next指向head
        while firstGreater and firstGreater.val < x: #寻找第一个值大于等于x的结点
            firstGreater = firstGreater.next
        while cur:
            if cur.next and cur.next.val < x : 
                newCur.next = cur.next #newCur指针指向这个值小于x的结点
                cur.next = cur.next.next #删除cur.next
                newCur = newCur.next #newCur指针后移一个
            else:
                cur = cur.next
        newCur.next = firstGreater #遍历结束后，newCur指向firstGreater
        return newHead.next
