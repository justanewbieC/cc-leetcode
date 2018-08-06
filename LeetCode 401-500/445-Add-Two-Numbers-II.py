'''
本题给定两个链表代表两个数。如L1:7->2->4->3代表7243;L2:5->6->4代表564.
要求将两个数相加，并用链表形式返回，如L1+L2=7807,则返回7->8->0->7.
本题可以首先遍历两个链表，并计算其结果放入num1,num2中，然后将两数相加；
接着创建一个新的链表节点，并将相加的结果按位放入新链表中即可。
本题运行时间112ms，击败96.20%用户。
'''
def addTwoNumbers(self, l1, l2):
	"""
	:type l1: ListNode
	:type l2: ListNode
	:rtype: ListNode
	"""
	res = ListNode(0)
	tail1, tail2, tail3 = l1, l2, res
	num1, num2 = 0, 0
	while tail1 or tail2:
		if tail1:
			num1 = num1*10 + tail1.val #得到链表所表示的数
			tail1 = tail1.next
		if tail2:
			num2 = num2*10 + tail2.val
			tail2 = tail2.next
	numSum = str(num1 + num2)
	for i in range(len(numSum)):
		tail3.val = numSum[i]
		if i != len(numSum)-1:
			tail3.next = ListNode(0)
			tail3 = tail3.next
	return res
