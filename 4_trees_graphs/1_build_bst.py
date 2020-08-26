class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class build_bst:
    def __init__(self):
        self.root = None

    def build(self, arr):
        self.add_node(arr, 0, len(arr)-1)

    def add_node(self, arr, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        node = Node(arr[mid])
        if not self.root:
            self.root = node
        node.left = self.add_node(arr, start, mid - 1)
        node.right = self.add_node(arr, mid+1, end)
        return node

    def in_order(self):
        visit = []
        self.__in_order(self.root, visit)
        return visit

    def __in_order(self, node,visit):
        if not node:
            return
        self.__in_order(node.left, visit)
        visit.append(node.val)
        self.__in_order(node.right, visit)





arr = list(range(9))

bst = build_bst()
bst.build(arr)
print(bst.in_order())
