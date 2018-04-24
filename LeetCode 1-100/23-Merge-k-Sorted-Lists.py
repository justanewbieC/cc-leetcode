'''
本题输入为k个有序链表，要求将k个链表合为一个有序链表输出。
我对输入情况开始不是很清楚，在学习了discuss中的算法后有了一些更进一步的认识。
比如想输入的数据为[[1,4,5],[1,3,4],[2,6]]，则输入进去的数据结构为[Node(1),Node(1),Node(2)]。
其中Node(1)、Node(1)、Node(2)表示三个链表。
discuss中的算法运用了heapq模块中的heapify,heappop,heapreplace函数。
heapq.heapreplace(heap,n) #删除heap中的最小元素，并加入元素n。
heappop,heapreplace的时间复杂度为O(logk)(k为子链个数),while循环则需要循环n次(n为总节点数)。
因此我认为总时间复杂度为O(nlogk)。
程序运行时间为104ms，击败95.30%用户。
'''
import headp

def mergeKLists(lists):
	dummy = node = ListNode(0)
	h = [(n.val, n) for n in lists if n] #若输入为所给用例，则h中有3个三个元素。
	heapq.heapify(h) #最小堆调整。
	while h: 
		v , n = h[0]
		if n.next: #没有遍历到子链链尾。
			heapq.heapreplace(h, (n.next.val, n.next)) #用某一节点的后继节点代替此节点。
		else: #该链遍历到链尾，便可将其删除。
			heapq.heappop(h)
		node.next = n
		node = node.next
	return dummy.next
			
