'''
����Ҫ���жϸ����������Ƿ�����Ч�ġ�
����ж���Ч:��һ��9*9��������
(1)ÿһ�а���1-9�Ҳ��ظ�
(2)ÿһ�а���1-9�Ҳ��ظ�
(3)ÿһ��3*3���������а���1-9�Ҳ��ظ�
(4)�����л�û�����������'.'��ʾ��
�������Hash Table(����ҵ�ʱ�临�Ӷ�ΪO(1))�������python�У��ֵ������һ���ݽṹ��
ÿһ�У�ÿһ�У�ÿһ3*3������ֱ�ά��һ��dict�����������е�����Ԫ��:
(1)�����'.'����pass
(2)�����һԪ�ش����ڵ�ǰ�л�ǰ�л�ǰ������ֵ��У��򷵻�false
(3)������ڣ���������ӽ������ڵ������ֵ���
����ʱ�临�Ӷ�ΪO(n)��nΪ�����и��ӵ�����������ʱ��60ms������97.60%�û���
'''
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board : return False
        dictList = [{} for _ in range(18)] #�ֵ��б�
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
