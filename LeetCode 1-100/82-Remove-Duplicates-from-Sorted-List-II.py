'''
题在83题的基础上增加了难度，要求只要是重复出现的元素，就删除掉。
我想到用快慢两个指针来解决此问题。先创建一个节点phead，让phead.next=head。
这样phead就是一个头结点为空，其余结点为head的链表。
fast为head上的指针，slow为phead上的指针。并用sameNum记录元素重复出现的次数。
每当fast.val==fast.next.val时，sameNum就加1，然后用slow在sameNum的基础上循环删除相同值的结点。
本题时间复杂度O(n)。运行时间52ms，击败96.11%用户。
'''
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        phead , phead.next , fast = ListNode(0) , head , head #phead.next指向head
        slow = phead #slow指向phead
        while fast and fast.next :
            sameNum = 1
            while fast.next and fast.val == fast.next.val :
                sameNum += 1
                fast = fast.next
            fast = fast.next
            if sameNum != 1:
                for _ in range(sameNum , 0 ,-1): #循环删除有相同值的结点
                    slow.next = slow.next.next
            else:
                slow = slow.next
        return phead.next
