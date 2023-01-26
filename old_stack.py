class Stack:

    def __init__(self):
        self.data = ''
        self._type = ''
        self._sep = "|"
        self._label = ' -> '

    def is_empty(self):
        if not self.data:
            return True
        return False

    def push(self, value):
        self._set_data(value)

    def add(self, value):

        self._set_data(value)

    def pop(self):
        if not self.data:
            raise StackPopException

        data_first = self._split(self.data)[-1]
        type_first = self._split(self._type)[-1]
        self.data = (self._sep).join(self._split(self.data)[:-1])
        self._type = (self._sep).join(self._split(self._type)[:-1])

        result = self._get_value(type_first, data_first)

        return result

    def _get_value(self, t, v):

        if t == 'int':
            return int(v)

        elif t == 'float':
            return float(v)

        elif t == 'list':
            return list(v)

        elif t == 'dict':
            return dict(v)

        else:
            return str(v)

    def _set_data(self, value):
        if not self.data:
            self.data = f"{value}"
            self._type = f"{type(value).__name__}"
        else:
            self.data = f"{value}{self._sep}" + self.data
            self._type = f"{type(value).__name__}{self._sep}" + self._type

    def _split(self, data):
        return data.split(self._sep)

    def __len__(self) -> int:
        if not self.data:
            return 0
        return len(self._split(self.data))

    def __str__(self):
        if not self.data:
            return self.data

        return self.data.replace(self._sep, self._label)

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        str_repr = self.data.replace(self._sep, ', ')
        return f"<{cls}: ({str_repr})>"


class StackPopException(Exception):
    "Não pode remover uma instancia vazia"
    pass
