# # 이진트리의 순회 Traversal


#전위(처-왼-오)
def pre_order(node):
    if node is None:
        return
    print(node.data, end='-') #처
    pre_order(node.left) #왼
    pre_order(node.right) #오

#중위(왼-처-오)
def in_order(node):
    if node is None:
        return
    in_order(node.left) #왼
    print(node.data, end='-') #처
    in_order(node.right) #오

#후위(왼-오-처)
def post_order(node):
    if node is None:
        return
    post_order(node.left) #왼
    post_order(node.right) #오
    print(node.data, end='-') #처


class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

node1 = TreeNode()
node1.data = 'hs'

node2 = TreeNode()
node2.data = 'sl'
node1.left = node2

node3 = TreeNode()
node3.data = 'mb'
node1.right = node3

node4 = TreeNode()
node4.data = 'hw'
node2.left = node4

node5 = TreeNode()
node5.data = 'zz'
node2.right = node5

node6 = TreeNode()
node6.data = 'sm'
node3.left = node6

node7 = TreeNode()
node7.data = 'dy'
node4.right = node7

node8 = TreeNode()
node8.data = 'sn'
node6.right=node8


post_order(node1)
print()
pre_order(node1)
print()
in_order(node1)
