class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None  # Очередь пуста
        val = self.start.data
        if self.start.nref:
            self.start = self.start.nref
            self.start.pref = None
        else:
            self.start = None
            self.end = None
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)
        current = self.start
        i = 0
        while current:
            if i == n:
                new_node.nref = current
                new_node.pref = current.pref
                if current.pref:
                    current.pref.nref = new_node
                current.pref = new_node
                if current == self.start:
                    self.start = new_node
                return
            current = current.nref
            i += 1

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.nref
        print()
