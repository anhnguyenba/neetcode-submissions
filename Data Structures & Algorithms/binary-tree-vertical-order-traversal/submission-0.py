# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        cmap = defaultdict(list)
        cmap[0] = [root.val]
        while queue:
            node, col = queue.pop(0)
            if node.left:
                cmap[col - 1].append(node.left.val)
                queue.append((node.left, col - 1))
            if node.right:
                cmap[col + 1].append(node.right.val)
                queue.append((node.right, col + 1))

        cmap = sorted(cmap.items())
        return [values for _, values in cmap]
