class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

'''
            10
        8        15
      3   9
'''

for group in numbers[1:]:
    node = TreeNode()
    node.data = group
    current = root
    while True:
        if group < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right  # move


def findmin(node):
    if node.left is None:
        return node
    return findmin(node.left)


  # # 삭제 # #
delete_number = 15 # -> 4 이 트리에 없음  / 9 -> 9 이 삭제됨요

current = root
parent = None
while True:
    if delete_number == current.data:
        if current.left == None and current.right == None: # 둘 다 none
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del(current)
        elif current.left != None and current.right == None: # 왼쪽 값, 오른쪽 none
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del(current)
        elif current.left == None and current.right != None: # 왼쪽 none, 오른쪽 값
            if parent.right == current:
                parent.right = current.right
            else:
                parent.left = current.right
            del(current)
        else:  # ⭐ 자식이 두 개 있는 경우 ⭐
            min_node = findmin(root.right)  # 오른쪽 서브트리에서 최소값 찾기
            root.data = min_node.data  # 대체
            root.right = delete_node(root.right, min_node.data)  # 기존 최소값 노드 삭제

    return root #??

        print(delete_number, '이 삭제됨요')
        break
    elif delete_number < current.data:
        if current.left == None:
            print(delete_number, '이 트리에 없음')
            break
        parent=current
        current = current.left
    else:  #delete_number > current.data
        if current.right == None:
            print(delete_number, '이 트리에 없음')
            break
        parent=current
        current = current.right


'''
자식 노드가 둘 있는 노드를 삭제할 때는 재귀를 사용해야 편리하다.
자식이 2개 있는 부분을 재귀함수로 처리해라.

자식 둘을 비교하는 과정이 필요.
그래서 위로 다시 올라가야 하므로 재귀 사용.

자식이 없는 경우 -> 그냥 삭제
자식이 하나만 있는 경우 -> 그 자식을 올림
자식이 둘 다 있는 경우 -> 오른쪽 서브트리에서 최소값을 찾아 대체
'''