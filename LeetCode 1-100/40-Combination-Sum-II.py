'''
本题在上一题的基础上加大了一些难度，每个元素只能使用一次，但candidates数组中会有
重复元素出现。我开始想的是只用在上一问的基础上，将递归candidates[i:]改为
递归candidates[i+1:]即可(避免同一元素使用多次)，但最后结果却不是我想要的。
res列表中会有重复列表的出现。原来比如candidates=[2,5,2,1,2],target=5。

则      1        这是第一层节点为1的情况，第三层得到1+2+2=5后，程序回到第二层。
      /| |\	 第二层的第二个2继续遍历，这样再会得到1+2+2=5的结果并加入res。
     2  2 2 5    这显然不是我想要的。因此我在遍历之前加入一个判断，如果candidates[i]
    /|\ |\ \     =candidates[i-1]，就跳过这次遍历。
   2 2 52 5 5    这样改动后得到了我想要的结果。
程序运行时间为56ms，击败94.31%用户。
'''
def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res , subres = [] , [] 
    self.recursionComb(sorted(candidates), target, res, subres)
    return res
        
def recursionComb(self, candidates, target, res, subres):
    for i in range(len(candidates)):
        if i > 0 and candidates[i] == candidates[i-1]: #如果在当前层这个元素的值以前出现过，则跳过这次遍历
            continue
        if target - candidates[i] == 0:
            subres.append(candidates[i])
            res.append(subres)
            return 
        elif target - candidates[i] < 0:
            return
        self.recursionComb(candidates[i+1:], target-candidates[i], res, subres+[candidates[i]])
