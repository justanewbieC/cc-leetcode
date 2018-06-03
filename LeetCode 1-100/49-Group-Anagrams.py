'''
本题要求按字母异位词分组，即将组成元素相同但元素排列方式不同的单词分为一组。
本题可用hash table方法。维护一个strsDict字典。遍历每个单词，先将每个单词按照字母
升序排列。如果排列后的key在字典中，则添加进该键值对;若不存在，则添加新的键值对。
最后返回字典所有的值即可。
本题时间复杂度为O(n)(查找的时间复杂度O(1))，运行时间124ms，击败99%用户。
'''
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    strsDict = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key in strsDict:
            strsDict[key] += [word]
        else:
            strsDict[key] = [word]
    return list(strsDict.values())
