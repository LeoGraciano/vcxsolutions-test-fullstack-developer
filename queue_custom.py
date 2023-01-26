class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self._sep = " -> "

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def enqueue(self, data):
        self._set_data(data)

    def dequeue(self):
        if not self.head:
            raise QueueDequeueException

        index = 0
        current_idx = 0
        current_node = self.head

        while current_node is not None:
            if current_idx == index:
                if current_node.next is None:
                    self.head = None
                else:
                    self.head = current_node.next

                return current_node.data

            current_node = current_node.next
            current_idx += 1

    def _set_data(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def __len__(self) -> int:
        if self.head is None:
            return 0

        current_node = self.head
        total = 0

        while current_node:
            total += 1
            current_node = current_node.next

        return total

    def __str__(self):
        contents = self.head

        if contents is None:
            return ""

        temp_str = ''
        while contents:
            if temp_str:
                temp_str += self._sep
            temp_str += str(contents.data)
            contents = contents.next

        return temp_str

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"<{cls}: ({self.__len__})>"


class QueueDequeueException(Exception):
    "Não pode remover uma instancia vazia"
    pass
