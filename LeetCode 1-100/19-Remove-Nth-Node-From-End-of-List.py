'''
本题要求删除链表中从后往前数第N个节点。
本想着先遍历一遍链表，求出链表长度，然后再删除待删除元素。
但题目要求:do this in one pass，即时间复杂度须为O(n)。
因此可以用fast,slow两个指针来遍历，当fast走到n+1后，slow开始走动。
当fast结束后，只需slow.next=slow.next.next即可。
程序运行时间为40ms,击败99.91%用户
'''
def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    fast,slow,fast_index,slow_index=head,head,0,None
    while fast:
        fast_index+=1
        fast=fast.next
        if fast_index>n:
            slow_index=slow
            slow=slow.next#slow指针开始移动
    if slow_index!=None:
        slow_index.next=slow_index.next.next
        return head
    else:#链表本身过小，slow指针还未移动。如输入:([1,2],2)
        return head.next
