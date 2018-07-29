'''
本题给定一个链表和一个元素，要求删除链表中节点值等于这一元素的节点，并返回新链表。
本题较为简单，可以设置tail节点，其next为head。用while tail.next.val==val而不是
if tail.next.val==val是因为会有这样的情况:链表[1,1,1,1]，如果是if，则第二个
和第四个1删不掉。
本题时间复杂度为O(n)，运行时间80ms。
'''
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return head
        tail = ListNode(0)
        tail.next = head
        new_tail = tail
        while tail:
            while tail.next and tail.next.val == val:
                tail.next = tail.next.next
            tail = tail.next
        return new_tail.next
