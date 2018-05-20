'''
本题要求给定一个正数n，返回一个以螺旋的顺序包含n*n个元素的正方形矩阵。
如 n=3 ， 返回[[1,2,3],[8,9,4],[7,6,5]]
本题同样含有一定规律，用i表示行，用j表示列完成循环。一次循环过程如下:
(1)在当前第i行添加[j,n-j]个元素，用_循换[j,n-j]，每个元素的插入位置为_。
(2)在中间行添加数字，插入位置为-j。
(3)在当前循环的最后一行添加[j,n-j]个元素，每个元素插入位置为j。
(4)在中间行添加数字，插入位置为j。
如此循环直至在下一次循环中最后一行减去第一行小于2.
本题时间复杂度为O(n*n)，运行时间40ms，击败96.54%用户。
'''
def generateMatrix(n):
    res = [[] for _ in range(n)]
    i , j , num = 0 , 0 , 1
    while (n-i-1) - i > 1:
        for _ in range(j, n-j): #本次循环第一行行列表添加元素
            res[i].insert(_, num)
            num += 1
        for _ in range(i+1, n-i-1): #本次循环中间行列表添加元素(最后一个元素)
            res[_].insert(-j, num)
            num += 1
        for _ in range(j, n-j): #本次循环最后一行列表添加元素
            res[n-i-1].insert(j, num)
            num += 1
        for _ in range(n-i-2, i, -1): #本次循环中间行添加元素(第一个元素)
            res[_].insert(j, num)
            num += 1
        i , j = i+1 , j+1
    for _ in range(j, n-j):
        res[i].insert(_, num)
        num += 1
    if (n-i-1) - i == 1:
        for _ in range(j, n-j):
            res[n-i-1].insert(j, num)
            num += 1
    return res
