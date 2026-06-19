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
        min_col, max_col = 0, 0

        while queue:
            node, col = queue.pop(0)
            if node.left:
                cmap[col - 1].append(node.left.val)
                queue.append((node.left, col - 1))
            if node.right:
                cmap[col + 1].append(node.right.val)
                queue.append((node.right, col + 1))
            min_col = min(min_col, col)
            max_col = max(max_col, col)

        return [cmap[col] for col in range(min_col, max_col + 1)]
