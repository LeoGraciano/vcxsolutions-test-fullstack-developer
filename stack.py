import re


class Stack:

    def __init__(self):
        self.data = ''
        self._sep = "\n"
        self._label = f"%s: -> %s%s"

    def is_empty(self):
        if not self.data:
            return True
        return False

    def push(self, value):
        self.data += self.__get_label(value)

    def pop(self):
        first = self.__split[0]
        self.data = (self._sep).join(self.__split[1:])
        return first

    def __get_label(self, value):
        str_type = type(value).__name__
        return self._label % (value, str_type, self._sep)

    @property
    def __split(self):
        return self.data.split(self._sep)

    def __len__(self) -> int:
        return len(self.__split)

    def __str__(self) -> str:
        return self.data

    def __repr__(self) -> str:
        str_repr = re.sub(self._label, ", ", self.data)
        str_repr = re.sub(r'^:*,$', "", str_repr)
        return f"<Stack: ({str_repr})>"


if __name__ == '__main__':
    s = Stack()
    s.push('frango')
    s.push('Abacaxi')
    s.push([1, 3, 4, 5])
    s.pop()
    s.__repr__()
    pass
