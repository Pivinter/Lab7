class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list():
    # Функція для створення однозв'язного списку з введенням значень елементів з клавіатури

    head = None
    n = int(input("Введіть кількість елементів списку: "))
    for i in range(n):
        data = input("Введіть значення елемента: ")
        new_node = Node(data)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
    return head

def print_linked_list(head):
    # Функція для виведення значень елементів однозв'язного списку на екран

    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

def sublist(head, start, length):
    # Функція для копіювання підсписку в новий список

    current = head
    count = 1
    while current is not None and count < start:
        current = current.next
        count += 1
    new_head = None
    while current is not None and count <= start+length-1:
        new_node = Node(current.data)
        if new_head is None:
            new_head = new_node
        else:
            new_current = new_head
            while new_current.next is not None:
                new_current = new_current.next
            new_current.next = new_node
        current = current.next
        count += 1
    return new_head

def create_linked_list_from_file(file_name):
    # Функція для створення однозв'язного списку з вмісту текстового файлу

    head = None
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip()
            new_node = Node(data)
            if head is None:
                head = new_node
            else:
                current = head
                while current.next is not None:
                    current = current.next
                current.next = new_node
    return head

sourse = int(input("Виберіть джерело вхідних даних: клавіатура (1), файл (2): "))
if sourse == 1:
    # Основна програма
    head = create_linked_list()
    print("Список:")
    print_linked_list(head)
    start = int(input("Введіть номер початкового елемента підсписку: "))
    length = int(input("Введіть довжину підсписку: "))
    sub = sublist(head, start, length)
    print("Підсписок:")
    print_linked_list(sub)

if sourse == 2:
    file_name = input("Введіть назву файлу зі списком: ")
    head = create_linked_list_from_file(file_name)
    print("Список:")
    print_linked_list(head)
    start = int(input("Введіть номер початкового елемента підсписку: "))
    length = int(input("Введіть довжину підсписку: "))
    sub = sublist(head, start, length)
    print("Підсписок:")
    print_linked_list(sub)

