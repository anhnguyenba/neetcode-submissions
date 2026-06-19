# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def get_number(root: TreeNode, number: int):
            if not root:
                return 0
            
            number = number * 10 + root.val
            
            if not root.left and not root.right:
                return number

            return get_number(root.left, number) + get_number(root.right, number)

        return get_number(root, 0)