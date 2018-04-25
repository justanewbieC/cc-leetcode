'''
本题给一个candidates数组和一个target数，要求求出candidates数组中元素相加等于
target的所有情况，且一个元素可以重复多次。因为本题几乎要穷举所有可能，所以我采用递归
的思想，本题求解模型相当于一个树形结构，每个节点的孩子节点为所有不小于它的节点。
如果路径上的值相加小于target，则继续递归，如果大于等于则说明其后元素将均不符合条件。
例如candidates=[1,2,3,4]，target=2。第一层1的孩子节点为1,2,3,4。当第二层1与第一层1
相加等于2时，说明1后面的2,3,4将均不符合条件，故可以直接返回上一层。
程序运行时间68ms,击败98.43%用户。
'''
def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res , subres = [] , []
    self.recursionSum(sorted(candidates), target, res, subres)
    return res
        
def recursionSum(self, candidates, target, res, subres):
    for i in range(len(candidates)):
        if target - candidates[i] == 0 :
            subres.append(candidates[i])
            res.append(subres)
            return
        if target - candidates[i] < 0:
            return 
        else:
			#传的candidates是切片，即大于等于i的元素。
            self.recursionSum(candidates[i:], target-candidates[i], res, subres+[candidates[i]]) 

