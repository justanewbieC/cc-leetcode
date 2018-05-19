'''
本题要求将一个乱序链表排列成有序链表,要求时间复杂度为O(nlogn),空间复杂度O(1).
本题的难点在于对空间复杂度的要求，即只能使用额外的常数个空间。
本题可以采用mergeSort的思想对链表排序。
(1)在mergeSort中首先找到链表的中点。我开始的想法是先将链表遍历一遍得到其长度，再
遍历一次链表到长度/2的地方。这样做显然不是最优的(因为多遍历了一遍)，更高效的方法是
采用slow,fast两个指针，每一次slow走一步fast走两步，这样当fast走完时，slow便是中点。
(2)在merge中，用head来保存merge的结果。首先将head初始设为空节点。依次比较两个
链表，让head.next指向val值更小的一个节点，如此操作，将两个链表均遍历完后返回
head.next即可。
'''
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head : return None
        return self.mergeSort(head)
    
    def mergeSort(self, head):
        if not head.next : return head
        firstCount , secondCount , tail = 0 , 0 , head
        while tail: #求链表长度
            firstCount , tail = firstCount + 1 , tail.next
        tail = head
        while secondCount < firstCount//2 - 1:
            secondCount , tail = secondCount + 1 , tail.next 
        right = self.mergeSort(tail.next) #对中点以右进行递归
        tail.next = None
        left = self.mergeSort(head) #对中点以左进行递归
        return self.merge(left, right)
    
    def merge(self, left, right):
        head = ListNode(None) 
        tail = head
        while left and right:
            if left.val < right.val: 
                tail.next = left
                left = left.next
            else: 
                tail.next = right
                right = right.next
            tail = tail.next
        if left: tail.next = left #left中还有剩余节点
        else: tail.next = right #right中还有剩余节点
        return head.next
