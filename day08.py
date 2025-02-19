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


  # # 삭제 # #
delete_number = 4 # -> 4 이 트리에 없음  / 9 -> 9 이 삭제됨요

current = root
parent = None
while True:
    if delete_number == current.data:
        if current.left == None and current.right == None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del(current)
        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del(current)
        elif current.left == None and current.right != None:
            if parent.right == current:
                parent.right = current.right
            else:
                parent.right = current.right
            del(current)

        print(delete_number, '이 삭제됨요')
        break
    elif delete_number < current.data:
        if current.left == None:
            print(delete_number, '이 트리에 없음')
            break
        parent=current
        current = current.left
    else:
        if current.right == None:
            print(delete_number, '이 트리에 없음')
            break
        parent=current
        current = current.right








