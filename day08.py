## group 추가

class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()       #node 초기화 과정
                            #node 는 계속 업데이트 될 예정.
    node.data = numbers[0]
    root = node

    for group in numbers[1:]: #1번방부터 끝방까지 슬라이싱
        node = TreeNode()
        node.data = group
        current = root    #current = root & while True
        while True:
            if group < current.data:
                if current.left is None:  #왼쪽에 붙는 경우
                    current.left = node
                    break
                current = current.left  # 이동
            else:
                if current.right is None:  #오른쪽에 붙는 경우
                    current.right = node
                    break
                current = current.right  # m이동

    print("BST 구성 완료")


## find_group
    find_group = int(input())

    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data: # elif에서 거짓이면 else로 감
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.left # 왼쪽에 뭐가 있으니, 이동
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.right # 오른쪽에 뭐가 있으니, 이동



