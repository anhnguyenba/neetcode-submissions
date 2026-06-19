# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.numbers = []

        def get_number(root: TreeNode, number: str):
            if not root:
                return
            if not root.left and not root.right:
                number += str(root.val)
                self.numbers.append(number)
                return

            number += str(root.val)
            if root.left:
                get_number(root.left, number)
            if root.right:
                get_number(root.right, number)

        get_number(root, '0')
        return sum([int(num) for num in self.numbers])