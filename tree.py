class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_complete_binary_tree(n):
    if n == 0:
        return None

    queue = [Node(1)]
    i = 2
    while i <= n:
        level = []
        while queue:
            node = queue.pop(0)
            if i <= n:
                node.left = Node(i)
                level.append(node.left)
                i += 1
            if i <= n:
                node.right = Node(i)
                level.append(node.right)
                i += 1
            queue.append(node)
        queue = level
    return queue[0]
