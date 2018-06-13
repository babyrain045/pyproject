
#python构建二叉树，以及深度优先遍历
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

a = [1,2,3]
T = []

class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = TreeNode(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)


t = Tree()
for i in a:
    t.add(i)

print(t.root.val)
#计算二叉树支路上的数字和leetcode习题
def DFS(root,val):
    val = val*10 + root.val
    if root.left is None and root.right is None:
        return val
    sums = 0

    if root.left:
        sums += DFS(root.left,val)
    if root.right:
        sums += DFS(root.right,val)
    return sums

a = DFS(t.root,0)
print(a)




#class Solution(object):
#    def sumNumbers(self, root):
