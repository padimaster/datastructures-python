class Node:
    def __init__(self, value, index, next):
        self.value = value
        self.index = index
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def append(self, value):
        # Lista vacia, la cabeza y la cola van a ser el elemento ingresado
        if self.tail is None:
            self.head = Node(value, self.counter, None)
            self.tail = self.head
            self.counter += 1

            return
        
        new_node = Node(value, self.counter, None)

        # Añadimos la referencia al nuevo nodo, en el nodo tail
        self.tail.next = new_node

        # Cambiar el nodo tail, al nuevo nodo
        self.tail = new_node

        self.counter += 1

def main():
    my_linked_list = LinkedList()    
    my_linked_list.append(5)
    my_linked_list.append(6)
    my_linked_list.append(7)
    my_linked_list.append(8)

    print(my_linked_list.counter)

main()

