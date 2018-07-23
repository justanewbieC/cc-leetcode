'''
本题要求对于给定的行号，给出对应的"pascal's triangle"。
例如给定行号5.即5行。输出为:
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]。
本题比较简单，找出每一行规律即可。对于非第一行和第二行，其非第一和最后一个元素，
每个元素[i]等于上一行的元素[i-1]+[i]。
本题运行时间36ms，击败90%用户。
'''
def generate(self, numRows):
	"""
	:type numRows: int
	:rtype: List[List[int]]
	"""
	res = []
	for i in range(1, numRows+1):
		if i == 1:
			res.append([1])
		elif i == 2:
			res.append([1, 1])
		else:
			subres = []
			for j in range(i):
				if j == 0 or j == i-1:
					subres.append(1)
				else:
					subres.append(res[i-2][j]+res[i-2][j-1])
			res.append(subres)
	return res
