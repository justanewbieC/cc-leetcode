'''
本题给定一个m*n的矩阵，要求以螺旋的顺序返回包含矩阵所有元素的列表。
如[[1,2,3],[4,5,6],[7,8,9]]，返回[1,2,3,6,9,8,7,4,5]。
本题显然有一定的规律。row,col分别表示行和列。用i,j去完成循环。
可以这样看待一次循环:当前行号为第i行，列号为第j列。
1.先将当前行的[j:col-j]添加入列表。
2.将[i+1,row-i-1]行每行的第col-j-1个元素添加入列表。
3.将第row-i-1行的[j:col-j]添加入列表。
4.将[i+1,row-i-1]行每行的第j个元素逆序添加入列表。
以上便完成一次循环，i，j分别加1.
当只剩下小于等于2行可以循环或所有列都遍历过便结束循环。
本题时间复杂度为O(m*n)，运行时间36ms，击败95.57%用户
'''
def spiralOrder(matrix):
    if not matrix : return []
    row , col , spiralMatrix = len(matrix) , len(matrix[0]) , [] 
    i , j = 0 , 0
    while (row-i-1) - i > 1 and (col-j-1) - j >= 0:
		#添加本次循环的第一行
        for _ in matrix[i][j:col-j] : spiralMatrix.append(_)
		#添加本次循环的中间行的最后一个元素
        for k in range(i+1, row-i-1): spiralMatrix.append(matrix[k][col-j-1])
        #逆序添加本次循环的最后一行
        for _ in matrix[row-i-1][j:col-j][::-1] : spiralMatrix.append(_)
        #逆序添加本次循环中间行的第一个元素
        if j != col-j-1:
            for k in range(row-i-2, i, -1):
                spiralMatrix.append(matrix[k][j])
        i , j = i+1 , j+1
    for _ in matrix[i][j:col-j] : spiralMatrix.append(_)
    if (row-i-1) - i == 1:
        for _ in matrix[row-i-1][j:col-j][::-1] : spiralMatrix.append(_)
    return spiralMatrix

'''
discuss中有一个可读性更好的程序。它在每次循环时删除遍历到的元素。
'''    
def spiralOrder(self, matrix):
    ret = []
    while matrix:
        ret += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        if matrix:
            ret += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
    return ret
