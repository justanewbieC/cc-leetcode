'''
本题要求删除链表中的重复元素，本题较为简单。
如果两元素相同，tail.next = tail.next.next即可。
本题时间复杂度O(n)。
本题用时52ms，击败96.59%用户。
'''
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = head
        while tail and tail.next:
            if tail.val == tail.next.val:
                tail.next = tail.next.next
            else:
                tail = tail.next
        return head
