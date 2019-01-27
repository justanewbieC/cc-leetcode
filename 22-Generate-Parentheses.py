'''
�������һ������n��Ҫ�󷵻ذ���n�ԺϷ���Բ���ŵ����з��������������3��
��Ӧ���ؼ��ϣ�["((()))","(()())","(())()","()(())","()()()"]��
������Ҫ�õ����ݷ�(����Ϊ����������������)��������뵽�˵ݹ顣�ݹ麯����
��������һ��absNum��ʾ���ǵ�ǰ�ַ������������������Ĳ�ֵ����'(()'����
���ű������Ŷ�1������absNumΪ1.��absNum����0ʱ��ÿ�εݹ飬string����
��'('��Ҳ���Լ�')'������absNum����0ʱ����ֻ�����'('�����n=0ʱ�����
��string����List�С�
������ʱ36ms������100%�û�
'''
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        if n == 1: return ['()']
        stack = []
        self.recursionGenerate('', n, 0, stack)
        return stack
    
    def recursionGenerate(self, string, n, absNum, stack):#absNumΪ�������������Ĳ�ֵ
        if n == 0:
            string += (')'*absNum)
            stack.append(string)
        else:
            if absNum > 0:
                self.recursionGenerate(string+'(', n-1, absNum+1, stack)
                self.recursionGenerate(string+')', n, absNum-1, stack)
            else:
                self.recursionGenerate(string+'(', n-1, absNum+1, stack)
