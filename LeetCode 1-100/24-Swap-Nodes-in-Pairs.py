'''
本提要求在一个列表中，调换每两个相邻的节点。
对于1→2→3→4:
(1)tmp = head.next # 2→3→4
(2)head = tmp.next # 1→3→4
(3)tmp.next = head # 2→1→3→4
基于此，可用递归的方法对整个链表完成操作。
本题用时36ms，击败99.56%的用户。
'''
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: #链表为空
            return None
        if head.next == None: #链表只有一个节点
            return head
        tmp = head.next
        head.next = self.swapPairs(tmp.next) #递归调用
        tmp.next = head
        return tmp
