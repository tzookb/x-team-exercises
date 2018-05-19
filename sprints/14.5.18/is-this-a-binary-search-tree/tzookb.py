class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    tree_items = get_node_items(root)

    # check for duplicates
    if len(tree_items) != len(set(tree_items)):
        return False

    if not all(tree_items[i] <= tree_items[i+1] for i in range(len(tree_items)-1)):
        return False
    
    return True

def get_node_items(root):
    items = []
    if root.left:
        items = get_node_items(root.left) + items
    items.append(root.data)
    if root.right:
        items = items + get_node_items(root.right)
    return items


# test code 

# root = Node(5)
# l1 = Node(2)
# l2 = Node(1)
# l3 = Node(3)
# r1 = Node(6)

# root.left = l1
# root.right = r1

# l1.left = l2
# l1.right = l3

# res = checkBST(root)

# print(res)