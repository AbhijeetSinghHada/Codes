from Node import Node


class BinaryTree:
    def __init__(self, head: Node) -> None:
        self.head = head

    def add_node(self, data):
        current_node = self.head
        while current_node:
            if data == current_node.data:
                raise ValueError("Duplicate Element Already eself.headists")
            elif data < current_node.data:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(data)
                    break
            elif data > current_node.data:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(data)
                    break

    def buildTree(self, arr):
        root = None
        parent = None
        parentIndex = 0
        nodes = [None]*len(arr)
        for i, val in enumerate(arr):
            node = None
            if val != 'n':
                num = int(val)
                node = Node(num)
            nodes[i] = node
            if i == 0:
                root = node
                parentIndex = 0
            else:
                parent = nodes[parentIndex]
                if i % 2 == 0:
                    root = node
                    parentIndex = 0

                else:
                    parent = nodes[parentIndex]
                    if i % 2 == 0:
                        parent.right = node
                        parentIndex += 1
                        while parentIndex <= i and nodes[parentIndex] == None:
                            parentIndex += 1
                    else:
                        parent.left = node
        return root

    def get_head(self):
        return self.head

    def inorder(self, head):
        if head == None:
            return
        self.inorder(head.left)
        print(head.data)
        self.inorder(head.right)

    def communicateToEmployees(self, root):
        ans = []
        if not root:
            return
        queue = [root]
        left_to_right = True  # Flag to alternate between leftmost and rightmost nodes

        while queue:
            level_size = len(queue)

            if left_to_right:
                ans.append(queue[0].data)
            else:
                ans.append(queue[-1].data)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            left_to_right = not left_to_right  # Toggle the flag

        res = ' '.join(map(str, ans))
        print(res)

    def find(self, val):
        current_node = self.head
        while current_node:
            if val == current_node.data:
                return current_node
            elif val < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        raise LookupError(f"Node with Value {val} not found.")

    def find_parent(self, value: int) -> Node:
        current_node = self.head
        while current_node:
            if current_node.left and current_node.left.data == value or\
                    current_node.right and current_node.right.data == value:
                return current_node
            elif value < current_node.data:
                current_node = current_node.left
            elif value > current_node.data:
                current_node = current_node.right

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node
