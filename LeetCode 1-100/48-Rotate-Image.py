'''
�������һ��n*n�Ķ�ά����Ҫ�󽫶�ά����˳ʱ����ת��ʮ�ȣ��Ҳ��ö���ռ䡣
���������:
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
��Ӧ���:
[ [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]��
�����ҳ����еĹ��ɼ��ɼ򵥵�д������
��Ϊ�Ե�һ�н�����ת����ζ�Ŷ����һ��Ҳ������ת���Եڶ��н�����ת����ζ�ŶԵ�����
����Ҳ��������ת������ܹ���Ҫ��ת����Ϊn/2��
�������У����ǵ�һ�У��������ǰn-1�У����ǵڶ��У��������n-1*2-1�С��������Ϊ
row������ڵ�row�У���Ҫ����n-1-2*row�С�
������ÿһ�У�ÿһ����ת��Ԫ�������������ʾ��
����ʱ�临�Ӷ�ΪO(n*n),����ʱ��Ϊ40ms��
'''
def rotate(self, matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: void Do not return anything, modify matrix in-place instead.
	"""
	matLen = len(matrix)  #����ı߳�
	for row in range(matLen//2):  #��Ҫ��ת����
		for col in range(matLen-1-2*row):  #��Ҫ��ת����
			matrix[row][row+col], matrix[row+col][matLen-1-row], matrix[matLen-1-row][matLen-1-row-col], matrix[matLen-1-row-col][row] \
				= matrix[matLen-1-row-col][row], matrix[row][row+col], matrix[row+col][matLen-1-row], matrix[matLen-1-row][matLen-1-row-col]
