'''
����Ҫ��һ������������������õݹ�ͷǵݹ�ķ������ǵݹ鷽������:
����reverseHeadΪNone���ڱ����µ���������tail1ָ��head����ѭ����tail2����
����ÿ��ѭ��ʱ��tail1��ֵ��ÿ��ѭ��ʱ��tail2��nextָ��reverseHead���ٽ�tail2
����reverseHead��������������������˵�ǰλ�õ�����
��Ҫ�ر�ע��:ѭ���еĵ�2�����ܳ����ڵ�4��֮����Ϊ��1������tail1��tail2ָ���
��ͬһ�������������2�����ڵ�4��֮����ô��3������tail2�Ĳ���ͬ���������tail1.
�Ⲣ����������Ҫ�ġ�
����ʱ�临�Ӷ�ΪO(n)������ʱ��40ms������99.86%�û���
'''
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverseHead , tail1 = None , head 
        while tail1:
            tail2 = tail1 #1
            tail1 = tail1.next #2
            tail2.next = reverseHead #3
            reverseHead = tail2 #4
        return reverseHead
'''
�ݹ鷽������:
'''
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverseHead = None
        return self.recursionList(head, reverseHead)
        
    
    def recursionList(self, head, reverseHead):
        if head:
            cur = head
            head = head.next
            cur.next = reverseHead
            reverseHead = cur
            return self.recursionList(head, reverseHead)
        else:
            return reverseHead
