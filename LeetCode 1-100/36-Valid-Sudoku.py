'''
本题要求判断给定的数独是否是有效的。
如何判断有效:在一个9*9的数独中
(1)每一行包含1-9且不重复
(2)每一列包含1-9且不重复
(3)每一个3*3的子网格中包含1-9且不重复
(4)数独中还没有填的数字用'.'表示。
本题可用Hash Table(其查找的时间复杂度为O(1))解决。在python中，字典就是这一数据结构。
每一行，每一列，每一3*3矩阵均分别维护一个dict。遍历数独中的所有元素:
(1)如果是'.'，则pass
(2)如果这一元素存在于当前行或当前列或当前矩阵的字典中，则返回false
(3)如果不在，则依次添加进它所在的三个字典中
本题时间复杂度为O(n)，n为数独中格子的数量。运行时间60ms，击败97.60%用户。
'''
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board : return False
        dictList = [{} for _ in range(18)] #字典列表
        for row in range(0,9,3): #row = 0, 3, 6
            for col in range(0,9,3): #col = 0, 3, 6
                sudokuDict = {}
                for subRow in range(3):
                    for subCol in range(3):
                        if board[row+subRow][col+subCol]=='.':
                            pass
                        else:
                            item = board[row+subRow][col+subCol]
                            if item in sudokuDict or item in dictList[row+subRow] or item in dictList[9+col+subCol]:
                                return False
                            else:
                                sudokuDict[item] = 1
                                dictList[row+subRow][item] = 1
                                dictList[9+col+subCol][item] = 1
        return True
