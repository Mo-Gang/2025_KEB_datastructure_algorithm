class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): #헤드가 가르킨 노드가 있는지 없는지
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next: #존재하면 연결돼있다는 뜻이니까
            current = current.next #다음노드로 이동
        current.next = Node(data)


if __name__ == "__main__":
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)

