
class Node():

    def __init__(self, key, value=float('inf')):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def inorder(self):
        if self.left:
            for i in self.left.inorder():
                yield i
        yield (self.key, self.value)
        if self.right:
            for i in self.right.inorder():
                yield i

class BST():

    def __init__(self, key, value):
        self.root = Node(key, value)

    def find_next(self, key):
        node = self.root
        while node:
            if node.key == key:
                return node
            elif node.key > key:
                if not node.left:
                    return node
                node = node.left
            else:
                node = node.right
        raise ValueError

    def get_or_add(self, key):
        # raise error when no root
        node, last = self.root, None
        while node:
            last = node
            if node.key == key:
                return node
            elif node.key > key:
                if not node.left:
                    node.left = Node(key)
                    return node.left
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = Node(key, float('inf'))
                    return node.right
                else:
                    node = node.right


class Solution():

    def find_best(self, chunks, L, B):
        tree = BST(0, 0)
        # chunks = [(0, 100), (0, 200), (20, 500), (190, 290), (250, 500)]
        # L = 15
        # B = 10
        for start, end in chunks:
            start_node = tree.find_next(start)
            end_node = tree.get_or_add(end)
            end_node.value = min(end_node.value, start_node.value + 2 * L + (end - start) / B)

        for i in tree.root.inorder():
            print i,
        print


if __name__ == '__main__':
    test_file = 'test_data6.txt'
    with open(test_file) as f:
        N = int(f.readline())  # the number of bytes in the original file.
        L = int(f.readline())  # the latency of the connection in seconds.
        B = int(f.readline())  # the bandwidth of the connection in bytes per second.
        C = int(f.readline())  # the number of chunks.
        chunks = [(int(x.split(',')[0]), int(x.split(',')[1].strip())) for x in f.readlines()]
        # print 'chunks before sorted:', chunks  # before sorted
        chunks.sort(key=lambda tup: tup[0])
        s = Solution()
        s.find_best(chunks, L, B)
