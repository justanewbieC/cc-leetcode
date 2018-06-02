'''
本题要求将一个链表重新排序。
如原链表:L1 → L2 → L3 → L4 → L5 更新后链表:L1 → L5 → L2 → L4 → L3
本题解法可分为三步:
1.首先找到链表的中点。用fast和slow快慢指针即可。
2.将链表后半部分逆序。用到元组的特性。如在例子中一个链表变为两个:L1→L2→L3;L5→L4→L3
3.将两个链表合并。
本题时间复杂度为O(n),运行时间100ms，击败98.73%用户。
'''
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next : return
        
        #寻找链表的中点
        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #将链表的后半部分逆序
        last , node  = None , slow
        while node:
            #last , node , node.next = node , node.next , last #注意这一行与下一行的区别
            last, node.next, node = node, last, node.next
        
        #将逆序后的链表与正序链表MERGE
        first , second = head , last
        while second.next:
            first.next , first = second , first.next
            second.next , second = first , second.next
            #first , first.next = first.next , second
            #second , second.next = second.next , first  #注意这两行与上两行的区别
            
        return
