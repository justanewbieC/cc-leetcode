'''
�������һ�������һ��Ԫ�أ�Ҫ��ɾ�������нڵ�ֵ������һԪ�صĽڵ㣬������������
�����Ϊ�򵥣���������tail�ڵ㣬��nextΪhead����while tail.next.val==val������
if tail.next.val==val����Ϊ�������������:����[1,1,1,1]�������if����ڶ���
�͵��ĸ�1ɾ������
����ʱ�临�Ӷ�ΪO(n)������ʱ��80ms��
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
