import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        ans = ""
        q = []
        q.append(root)
        while (q):
            cur = q[0]
            ans += (str(cur.data) + " ")
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)
            q.pop(0)
        print(ans)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
