# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        res = []
        while q:
            qLen = len(q)
            last = None
            for i in range(qLen):
                node = q.pop(0)
                if node:
                    last = node.val
                    q.append(node.left)
                    q.append(node.right)
            if last:
                res.append(last)

        return res
