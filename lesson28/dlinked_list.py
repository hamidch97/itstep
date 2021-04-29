class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data}"


class DlinkedList:
    def __init__(self, nodes):
        self.nodes = nodes
        self.head = None
        self.tail = None
        if nodes is None:
            nodes = Node(nodes)
            self.nodes = nodes
            self.head = nodes

    def __str__(self):
        return " <-> ".join(self.nodes) + " <-> " + "None"

    def list_legth(self):

        return len(self.nodes)

    def insert(self, position, index=None):
        if isinstance(position, Node):
            position = Node(position)
        if self.head is None and index is None:
            self.head = position
            self.nodes.append(self.head)
            for i in self.nodes:
                return True
        elif self.head is None and index is not None:
            self.head = position
            self.nodes.insert(index, self.head)
            for i in self.nodes:
                return True
        return False

    def show_neighbors(self, position):
        if isinstance(position, Node):
            position = Node(position)
            next_node = position.next
            perev_node = position.prev
        if self.head == position:
            self.perev_node = position.prev
            self.next_node = position.next
            return f"{perev_node}->{position}->{next_node}"

    def remove(self, item):
        node = self.head
        if isinstance(node, Node):
            node = Node(node)
            for i in node:
                self.item = i[item]
                if self.head is not None:
                    if self.head == self.item:
                        del self.head
                        return True
                    elif self.item > len(self.nodes):
                        return False


if __name__ == "__main__":
    l = DlinkedList(["a", "b", "c", "d"])
    print(l.insert("q"))
    print(l.list_legth())
    # print(l.remove(2))
    # print(l.show_neighbors(2))
    print(l)
