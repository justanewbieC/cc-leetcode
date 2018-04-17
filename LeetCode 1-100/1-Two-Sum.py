'''
本题给定一个数组和一个目标数，要求在数组中找到两个数，其和等于目标数，并返回两数下标。
本题可先将数组排序，再用双指针夹逼，但时间复杂度为O(nlog n)，运行时间不理想。
python中的字典可解决这个问题。只要满足v,target-v均在字典中即可。
且dict的存储结构采用的是hash表，查询hash表的复杂度为O(1)。故总时间复杂度为O(n)。
程序运行时间为40ms，击败97.41%的用户。
'''
def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	d={}
	for k,v in enumerate(nums): #enumerate是一个包含列表元素下标和值的可迭代对象
		if (target-v) in d:
			return [d[target-v],k]
		d[v]=k #如果target-v不在字典的key中，就添加v:k键值对
 
