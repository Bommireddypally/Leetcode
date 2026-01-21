class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, curr):
            if not node:
                return 0

            curr = curr * 10 + node.val

            # leaf node
            if not node.left and not node.right:
                return curr

            return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)
