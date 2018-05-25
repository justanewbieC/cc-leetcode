'''
�������һ�ö�������������0-9.ÿһ������Ҷ�ӵ�·�������Ա�ʾһ�����֡��������Ҷ��
��·��Ϊ1->2->3���ʹ�������123.Ҫ���ҵ�����·���������·������ʾ������֮�͡�
������Ȼ��һ������������������Բ��õݹ�ķ��������
ά��һ��nodeSum����ǰ·�������֣�pathSum����·�������ܺ͡�
��ÿ�εݹ��У��ȸ���nodeSum��ֵ����nodeSum = nodeSum* 10 +root.val
����ݹ鵽�Ľڵ�û�к��ӽڵ㣬���������Ҷ�ӽڵ㡣����nodeSum��ֵ�ӵ�pathSum�У�
����pathSum���ɡ���˵ݹ������������������ɱ��⡣
����ʱ�临�Ӷ�ΪO(n)������ʱ��40ms������97%�û��� 
'''
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeSum , pathSum = 0 , 0
        return self.recursionTree(root, nodeSum, pathSum)
        
    def recursionTree(self, root, nodeSum, pathSum):
        if root:
            nodeSum = nodeSum* 10 + root.val 
            if not (root.left or root.right):
                return pathSum + nodeSum
            return self.recursionTree(root.left, nodeSum, pathSum) + self.recursionTree(root.right, nodeSum, pathSum)
        else: return pathSum
