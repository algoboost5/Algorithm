# inputs = ['7', 'A B C', 'B D .', 'C E F', 'E . .', 'F . G', 'D . .','G . .']
# node_num = int(inputs[0])
# nodes = {}
# for idx in range(node_num):
#     nodes[chr(65+idx)] = Node(chr(65+idx))
#
# for idx in range(1, len(inputs)):
#
#     center, left, right = inputs[idx].split()
#     # print(center, left, right)
#     nodes[center].left = nodes[left] if left!='.' else None
#     nodes[center].right = nodes[right] if right!='.' else None
#
# for node in nodes.values():
#     print(node.data, node.left, node.right)



class Node:
    def __init__(self,  name):

        self.data = name
        self.left = None
        self.right = None

def preorder(root, result):
    if not root:
        return ''
    else:
        result += root.data
        result += preorder(root.left, '')
        result += preorder(root.right, '')
        return result

def inorder(root, result):
    if not root:
        return ''
    else:
        result += inorder(root.left, '')
        result += root.data
        result += inorder(root.right, '')
        return result

def postorder(root, result):
    if not root:
        return ''
    else:
        result += postorder(root.left, '')
        result += postorder(root.right, '')
        result += root.data
        return result




import sys



node_num = int(sys.stdin.readline())
nodes = {}

for idx in range(node_num):
    nodes[chr(65+idx)] = Node(chr(65+idx))

for _ in range(node_num):

    center, left, right = sys.stdin.readline().split()
    nodes[center].left = nodes[left] if left!='.' else None
    nodes[center].right = nodes[right] if right!='.' else None


print(preorder(nodes['A'], ''))
print(inorder(nodes['A'], ''))
print(postorder(nodes['A'], ''))