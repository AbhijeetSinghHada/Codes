class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node->{self.data}"
