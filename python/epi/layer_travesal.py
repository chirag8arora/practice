class Solution():
    def printLayer(self, root):
        if not root:
            return
        queue = [root]
        current_level = 1
        next_level = 0
        while queue:
            node = queue.pop()
            print node.val,
            current_level -= 1
            if node.left:
                next_level += 1
                queue.insert(0, node.left)
            if node.right:
                next_level += 1
                queue.insert(0, node.right)
            if not current_level:
                print
                current_level = next_level
                next_level = 0
