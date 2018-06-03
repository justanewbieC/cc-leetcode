'''
����Ҫ����ĸ��λ�ʷ��飬�������Ԫ����ͬ��Ԫ�����з�ʽ��ͬ�ĵ��ʷ�Ϊһ�顣
�������hash table������ά��һ��strsDict�ֵ䡣����ÿ�����ʣ��Ƚ�ÿ�����ʰ�����ĸ
�������С�������к��key���ֵ��У�����ӽ��ü�ֵ��;�������ڣ�������µļ�ֵ�ԡ�
��󷵻��ֵ����е�ֵ���ɡ�
����ʱ�临�Ӷ�ΪO(n)(���ҵ�ʱ�临�Ӷ�O(1))������ʱ��124ms������99%�û���
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
