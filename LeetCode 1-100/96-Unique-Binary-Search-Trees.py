'''
本题要求给出一个数n后，求出(1...n)数组可以构成多少个异构的BST。
BST:binary search trees 满足以下要求:
(1)左子树的节点小于根节点
(2)右子树的节点大于根节点
(3)所有子树均满足(1) (2)的要求
本题可以用递归的思想。比如对于数i，其左子树必定为小于i的值，即(1...i-1)，
右子树必定为大于i的值，即(i+1...n)。对于根为i的二叉树，异构BST个数显然为
左子树的个数*右子树的个数。因此可以继续递归下去，如:
for i in range(n):
    result += self.numTrees(i) * self.numTrees(n-i-1)
但递归在这里会超时，因此可将算法改为递推的样式:
result[0]=result[1]=1
result[2]=result[0]*result[1]+result[1]*result[0]
result[3]=result[0]*result[2]+result[1]*result[1]+result[2]*result[0]
...
result[n]=result[0]*result[n-1]+result[1]*result[n-2]...
本题时间复杂度为O(n²)，运行时间32ms，击败100%的用户。
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=[0] * (n+1) #初始化结果数组
        result[0] , result[1] = 1 , 1
        for i in range(2,n+1):
            for j in range(i): #更新result[i]
                result[i] += result[j] * result[i-j-1]
        return result[n]
