class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


def insert_btree(root, key, t):
    def split_child(node, i):
        new_node = BTreeNode(node.children[i].leaf)
        t = len(node.children[i].keys) // 2
        node.keys.insert(i, node.children[i].keys[t])
        new_node.keys = node.children[i].keys[t + 1:]
        node.children[i].keys = node.children[i].keys[:t]
        if not node.children[i].leaf:
            new_node.children = node.children[i].children[t + 1:]
            node.children[i].children = node.children[i].children[:t + 1]
        node.children.insert(i + 1, new_node)

    def insert_non_full(node, key):
        if node.leaf:
            i = len(node.keys) - 1
            node.keys.append(key)
            while i >= 0 and node.keys[i] > key:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            i = len(node.keys) - 1
            while i >= 0 and node.keys[i] > key:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * t - 1:
                split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            insert_non_full(node.children[i], key)

    if len(root.keys) == 2 * t - 1:
        new_root = BTreeNode()
        new_root.children.append(root)
        split_child(new_root, 0)
        insert_non_full(new_root, key)
        return new_root
    else:
        insert_non_full(root, key)
        return root


def btree_sort(arr, t):
    root = BTreeNode(True)
    for key in arr:
        root = insert_btree(root, key, t)
    sorted_arr = []

    def inorder_traversal(node):
        for i in range(len(node.keys)):
            if not node.leaf:
                inorder_traversal(node.children[i])
            sorted_arr.append(node.keys[i])
        if not node.leaf:
            inorder_traversal(node.children[len(node.keys)])

    inorder_traversal(root)
    return sorted_arr


arr = [12, 3, 19, 0, 5, 14, 7, 9, 18, 15]
t = 2

sorted_arr = btree_sort(arr, t)
print("Sorted Array:", sorted_arr)
