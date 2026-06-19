# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lmap = defaultdict(list)
        q = [(root, 0)]
        while q:
            curr, level = q.pop(0)
            lmap[level].append(curr.val)
            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))
        
        res = []
        for level in lmap:
            res.append(lmap[level])
        return res

