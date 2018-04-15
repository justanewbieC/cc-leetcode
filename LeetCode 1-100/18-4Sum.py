'''
本题与15题3Sum解法相似。先将数组排序，后依次固定一个数，用双指针将结果夹逼。
但我的做法显得很笨重，对于4Sum需要三层循环，若对于KSum，则很难完成。
因此本题用时816ms，只击败48.69的用户。
def fourSum(nums, target):
	if nums==None or len(nums)<4:
		return []
	result=[]
	nums.sort()
	twoSum=0
	for i in range(len(nums)-3):#i只需到倒数第四个数
		if i>0 and nums[i]==nums[i-1]:#去重
			continue
		j=i+1
		while j<len(nums)-2:#j只需到倒数第三个数
			if j>i+1 and nums[j]==nums[j-1]:#去重
				j+=1
				continue
			l,r=j+1,len(nums)-1
			twoSum=target-nums[i]-nums[j]
			while l<r:
				if nums[l]+nums[r]<twoSum:
					l+=1
				elif nums[l]+nums[r]>twoSum:
					r-=1
				else:
					result.append([nums[i],nums[j],nums[l],nums[r]])
					l+=1
					r-=1
					while l<r and nums[l]==nums[l-1]:#去重
						l+=1
					while l<r and nums[r]==nums[r+1]:#去重
						r-=1
			j+=1
	return result
'''
#因此，我在discuss中借鉴了他人优秀的答案，用递归的方法将NSum减到2Sum。这样代码就显得很灵活。
#这个答案的运行时间为112ms，击败了92.11%的用户
def fourSum(nums, target):
    def findNsum(nums, target, N, result, results):#result保存每次固定的值
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:#判断数组是否符合条件
            return
        if N == 2: # 2个指针解决2Sum问题
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:#去重
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # 递归减小N
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):#or 后面的内容用于去重
                    findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results

