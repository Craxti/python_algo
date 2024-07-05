class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder_traversal(root, res):
    if root:
        inorder_traversal(root.left, res)
        res.append(root.val)
        inorder_traversal(root.right, res)


def tree_sort(arr):
    if len(arr) == 0:
        return arr
    root = TreeNode(arr[0])
    for i in range(1, len(arr)):
        insert(root, arr[i])
    result = []
    inorder_traversal(root, result)
    return result


arr = [12, 3, 19, 0, 5, 14, 7, 9, 18, 15]
sorted_arr = tree_sort(arr)
print("Sorted Array:", sorted_arr)
