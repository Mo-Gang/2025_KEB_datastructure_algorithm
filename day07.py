def is_queue_full() :
    if rear == size - 1:
        return True
    else:
        return False

def is_queue_empty() :
    global size, queue, front, rear
    if front == rear:
        return True
    else :
        return False

def en_queue(data) :
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def de_queue() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[front+1]


size = int(input("큐의 크기를 입력 : "))
queue = [None for _ in range(size)]
front = rear = -1

if __name__ == "__main__" :
    while True:
        menu = input("삽입(E)/삭제(D)/확인(P)/종료(X) : ")
        if menu == 'X' or menu == 'x':
            break
        elif menu== 'E' or menu == 'e' :
            data = input("입력할 데이터 : ")
            en_queue(data)
            print(queue)
        elif menu== 'D' or menu == 'd' :
            print("삭제된 데이터 : ", de_queue())
            print(queue)
        elif menu== 'P' or menu == 'p' :
            print("확인된 데이터 : ", peek())
            print(queue)
        else:
            print("입력이 잘못됨")
    print("프로그램 종료!")