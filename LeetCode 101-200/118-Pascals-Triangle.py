'''
����Ҫ����ڸ������кţ�������Ӧ��"pascal's triangle"��
��������к�5.��5�С����Ϊ:
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]��
����Ƚϼ򵥣��ҳ�ÿһ�й��ɼ��ɡ����ڷǵ�һ�к͵ڶ��У���ǵ�һ�����һ��Ԫ�أ�
ÿ��Ԫ��[i]������һ�е�Ԫ��[i-1]+[i]��
��������ʱ��36ms������90%�û���
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
