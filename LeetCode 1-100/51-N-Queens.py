'''
本题是n皇后问题，要求打印出一个字符串列表。比如在一个4*4的棋盘上，任意两颗棋子不能出现在同一行，同一列或同一对角线上。
本题是一道经典的backtracing类型题。可用递归解决。col代表列，row代表行，cur代表当前行，subres表示某一行的字符串。
对于每一行，依次判断棋子放到每一列是否可行(如:col=1表示在当前行，棋子放到第1列是否可行)。
对于每一列，需要依次判断cur以上行的棋子是否与当前行冲突(如:row=1表示第1行的棋子是否与当前行棋子冲突)
判断是否同列:如果col值等于第row行Q所在的位置，则同列，不满足条件。
判断是否对角线:(cur,col)表示当前棋子位置，(row,subres[row].index('Q'))表示第row行棋子位置，
			  若两个纵坐标之差的绝对值等于横坐标之差，则在同一对角线上，不满足条件。
如果满足上述条件，则可进行递归，ljust，rjust是字符串对齐函数。
本解法虽能满足题目要求，但运行速度不快。
'''
class Solution:
    def solveNQueens(self, n):
        res , subres= [] , []
        self.nQueens(n, res, subres)
        return res
        
    def nQueens(self, n, res, subres, cur=0):
        if cur == n:
            res.append(subres)
            return 
        for col in range(n):
            flag = True
            for row in range(cur):
                index = subres[row].index('Q') #Q所在的行下标
                if index == col or abs(col-index) == cur-row: # 第一个等式判断同列，第二个等式判断对角线    
                    flag = False
                    break
            if flag:
                self.nQueens(n, res, subres+['Q'.ljust(n-col,'.').rjust(n,'.')], cur+1)
'''
在discuss中看到别人的解法，发现上面的解法在循环嵌套上浪费了时间。
他的解法额外用到了xy_dif,xy_sum两个列表。xy_dif表示横纵坐标之差，xy_sum表示横纵坐标之和。
判断一个元素a是否在另一元素b的左下对角线:a的横纵坐标之和是否等于b的横纵坐标之和。(xy_dif)
判断一个元素a是否在灵异元素b的右下对角线:a的横纵坐标之差是否等于b的横纵坐标之差。(xy_sum)
他用这样的判断代替了上面解法的第二层for循环，使得运行速度加快。
程序运行时间68ms，击败93.58%用户。
'''
class Solution:
    def solveNQueens(self, n):
        res , subres , xy_dif , xy_sum = [] , [] , [] , []
        self.nQueens([], n, res, subres, xy_dif, xy_sum)
        return res
        
    def nQueens(self, A, n, res, subres, xy_dif, xy_sum, cur=0):
        if cur == n:
            res.append(subres)
            return 
        for col in range(n):
            if col not in A and (col-cur) not in xy_dif and (col+cur) not in xy_sum:
                self.nQueens(A+[col], n, res, subres+['Q'.ljust(n-col,'.').rjust(n,'.')], xy_dif+[col-cur], xy_sum+[col+cur], cur+1)
            
