class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data) #삽입 오퍼레이션

    def pop(self): #스택에서의 팝은 마지막값을 꺼내므로, 인자값 필요X
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):     #def is_empty(self) -> bool:
        return len(self.items) == 0

    def peek(self):          #def peek(self) -> object:
        return self.items[-1]

s1 = Stack()
s1.push(-9)
s1.push(6)
s1.push(33)

# print(s1.pop()) #33, 삭제되고
# print(s1.peek()) #6, 삭제 안 되므로
# print(s1.peek()) #6

print(s1.peek()) #33
print(s1.pop()) #33
print(s1.peek()) #6
print(s1.is_empty()) #6과 -9가 남아있으므로, False
