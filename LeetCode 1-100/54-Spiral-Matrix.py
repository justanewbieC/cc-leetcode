'''
�������һ��m*n�ľ���Ҫ����������˳�򷵻ذ�����������Ԫ�ص��б�
��[[1,2,3],[4,5,6],[7,8,9]]������[1,2,3,6,9,8,7,4,5]��
������Ȼ��һ���Ĺ��ɡ�row,col�ֱ��ʾ�к��С���i,jȥ���ѭ����
������������һ��ѭ��:��ǰ�к�Ϊ��i�У��к�Ϊ��j�С�
1.�Ƚ���ǰ�е�[j:col-j]������б�
2.��[i+1,row-i-1]��ÿ�еĵ�col-j-1��Ԫ��������б�
3.����row-i-1�е�[j:col-j]������б�
4.��[i+1,row-i-1]��ÿ�еĵ�j��Ԫ������������б�
���ϱ����һ��ѭ����i��j�ֱ��1.
��ֻʣ��С�ڵ���2�п���ѭ���������ж������������ѭ����
����ʱ�临�Ӷ�ΪO(m*n)������ʱ��36ms������95.57%�û�
'''
def spiralOrder(matrix):
    if not matrix : return []
    row , col , spiralMatrix = len(matrix) , len(matrix[0]) , [] 
    i , j = 0 , 0
    while (row-i-1) - i > 1 and (col-j-1) - j >= 0:
		#��ӱ���ѭ���ĵ�һ��
        for _ in matrix[i][j:col-j] : spiralMatrix.append(_)
		#��ӱ���ѭ�����м��е����һ��Ԫ��
        for k in range(i+1, row-i-1): spiralMatrix.append(matrix[k][col-j-1])
        #������ӱ���ѭ�������һ��
        for _ in matrix[row-i-1][j:col-j][::-1] : spiralMatrix.append(_)
        #������ӱ���ѭ���м��еĵ�һ��Ԫ��
        if j != col-j-1:
            for k in range(row-i-2, i, -1):
                spiralMatrix.append(matrix[k][j])
        i , j = i+1 , j+1
    for _ in matrix[i][j:col-j] : spiralMatrix.append(_)
    if (row-i-1) - i == 1:
        for _ in matrix[row-i-1][j:col-j][::-1] : spiralMatrix.append(_)
    return spiralMatrix

'''
discuss����һ���ɶ��Ը��õĳ�������ÿ��ѭ��ʱɾ����������Ԫ�ء�
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
