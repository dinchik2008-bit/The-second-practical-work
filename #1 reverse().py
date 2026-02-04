class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def reverse(self):
        # Правильная реализация реверса списка
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  
            current.next = prev      
            prev = current            
            current = next_node    
        
        self.head = prev  

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("Исходный список:")
    ll.print_list()
    
    ll.reverse()
    print("\nПеревернутый список:")
    ll.print_list()