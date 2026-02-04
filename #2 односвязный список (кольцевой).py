class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Добавляет элемент в конец списка"""
        new_node = Node(data)
        
        if not self.head:
            # Первый элемент - он же голова и хвост
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Замыкаем на себя
        else:
            # Добавляем после хвоста
            self.tail.next = new_node
            new_node.next = self.head  # Новый элемент ссылается на голову
            self.tail = new_node  # Обновляем хвост

    def print_list(self):
        """Печатает все элементы списка"""
        if not self.head:
            print("Список пуст")
            return
        
        current = self.head
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.head:
                break
        print(f"(возврат к head: {self.head.data})")

    def get_tail(self):
        """Возвращает ссылку на последний элемент"""
        return self.tail

    def print_tail_info(self):
        """Печатает информацию о хвосте"""
        if self.tail:
            print(f"Хвост списка: {self.tail.data}")
            print(f"Хвост ссылается на: {self.tail.next.data if self.tail.next else 'None'}")
        else:
            print("Список пуст")

# Тестирование
cll = CircularLinkedList()

print("Добавляем элементы:")
cll.append(1)
cll.append(2)
cll.append(3)

print("\nСписок:")
cll.print_list() 

print("\nИнформация о хвосте:")
cll.print_tail_info()

print("\nПроверка связности:")
print(f"1 -> {cll.head.next.data if cll.head.next else 'None'}")
print(f"2 -> {cll.head.next.next.data if cll.head.next and cll.head.next.next else 'None'}")
print(f"3 -> {cll.tail.next.data if cll.tail and cll.tail.next else 'None'}")