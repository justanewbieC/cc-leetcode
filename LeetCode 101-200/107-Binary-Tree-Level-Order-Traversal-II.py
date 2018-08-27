'''
����Ҫ�����һ���������������¶��ϣ������ҵ�˳�򷵻ض����������нڵ㡣
�磺������[3,9,20,null,null,15,7]����������������򷵻�[[15,7],[9,20],[3]]��
������õݹ��˼·�����ά��һ����ʾ���Ĳ����ı����ͱ����������鼴�ɡ�
��ʼlevel=1����ʼ����root�����res�ĳ���С��level����˵����ǰlevel���ǵ�һ�η��ʣ�
����res��insertһ�����飬���Ž�root��ֵ�����½��������У������ж�root�������Һ��ӣ�
���ݹ���ʼ��ɡ�
����ϼ򵥣�ʱ�临�Ӷ�O(n)������ʱ��40ms������100%�û���
'''
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = [] 
        if root : self.recursionTree(root, res, 1)
        return res
    
    def recursionTree(self, root, res, level):
        if len(res) < level:
            res.insert(0, [])
        res[-level].append(root.val)
        if root.left:
            self.recursionTree(root.left, res, level+1)
        if root.right:
            self.recursionTree(root.right, res, level+1)
