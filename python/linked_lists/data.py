class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def append(self, node):
        next_node = self

        while next_node.next:
            next_node = next_node.next

        next_node.next = node

    def __str__(self):
        node = self
        values = []

        while node:
            values.append(str(node.val))
            node = node.next

        return " ".join(values)


def create_list(data):
    linked_list = Node(data[0])

    node = linked_list
    for x in data[1:]:
        new_node = Node(x)
        node.next = new_node
        node = new_node
    return linked_list
