'''
本题要求将一个链表逆序输出，可用递归和非递归的方法。非递归方法如下:
先设reverseHead为None用于保存新的逆序链表；tail1指向head用于循环；tail2用于
保存每次循环时的tail1的值，每次循环时让tail2的next指向reverseHead，再将tail2
赋给reverseHead。这样操作下来便完成了当前位置的逆序。
需要特别注意:循环中的第2步不能出现在第4步之后。因为第1步过后tail1和tail2指向的
是同一个对象，如果将第2步放在第4步之后，那么第3步对于tail2的操作同样会操作于tail1.
这并不是我们想要的。
本题时间复杂度为O(n)，运行时间40ms，击败99.86%用户。
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
递归方法如下:
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
