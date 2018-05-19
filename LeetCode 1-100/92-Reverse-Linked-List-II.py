'''
本题给定一个链表和两个数m,n，要求将链表中第m个节点到第n个节点逆序，其余不变。
本题有一个特殊情况:逆序从第一个节点开始.
首先考虑一般化的情况:维护reverseHead表示逆序的链表部分;curNum表示当前遍历到第
curNum个下标;tail初始指向head用于遍历链表。当遍历到m的前一个节点时，用tail1记录
此点;当curNum在[m,n]中时利用reverse-linked-list中的方法将此部分逆序;当遍历到
n的后一个节点时,显然reverseHead的最后一个节点是tail1.next,因此将tail1.next.next
指向当前tail,再将tail1.next指向reverseHead即可。
特殊情况:即reverseHead的最后一个节点就是head，将head.next指向第n+1个节点即可
本题完成了题目要求(do it in one-pass)，时间复杂度O(n)，运行时间36ms，击败99.63%用户。
'''
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head : return None
        reverseHead , curNum , tail = None , 1 , head 
        while tail:
            if curNum == m-1 and m != 1: #此节点为第m-1个节点，记录下来
                tail1 = tail
            if m <= curNum <= n: #将链表逆序的部分
                tail2 = tail
                tail = tail.next
                tail2.next = reverseHead
                reverseHead = tail2
                curNum += 1
            else:
                tail = tail.next
                curNum += 1
            if curNum == n+1 and m != 1:
                tail1.next.next = tail
                tail1.next = reverseHead
            elif curNum == n+1:
                head.next = tail
        return head if m != 1 else reverseHead
