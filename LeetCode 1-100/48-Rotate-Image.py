'''
本题给定一个n*n的二维矩阵，要求将二维矩阵顺时针旋转九十度，且不用额外空间。
如输入矩阵:
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
则应输出:
[ [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]。
本题找出其中的规律即可简单的写出程序。
因为对第一行进行旋转就意味着对最后一行也进行旋转；对第二行进行旋转就意味着对倒数第
二行也进行了旋转。因此总共需要旋转的行为n/2。
而对于列，若是第一行，则需调整前n-1列；若是第二行，则需调整n-1*2-1列。因此设行为
row，则对于第row行，需要调整n-1-2*row列。
而对于每一行，每一列旋转的元素则如代码中所示。
本题时间复杂度为O(n*n),运行时间为40ms。
'''
def rotate(self, matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: void Do not return anything, modify matrix in-place instead.
	"""
	matLen = len(matrix)  #矩阵的边长
	for row in range(matLen//2):  #需要旋转的行
		for col in range(matLen-1-2*row):  #需要旋转的列
			matrix[row][row+col], matrix[row+col][matLen-1-row], matrix[matLen-1-row][matLen-1-row-col], matrix[matLen-1-row-col][row] \
				= matrix[matLen-1-row-col][row], matrix[row][row+col], matrix[row+col][matLen-1-row], matrix[matLen-1-row][matLen-1-row-col]
