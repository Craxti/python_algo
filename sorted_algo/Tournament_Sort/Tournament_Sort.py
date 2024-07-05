def tournament_sort(arr):
    if len(arr) <= 1:
        return arr
    tree = [None] * (2 * len(arr) - 1)
    idx = len(tree) - len(arr)
    for i in range(len(arr)):
        tree[idx + i] = (arr[i], i)
    idx -= 1
    while idx >= 0:
        left = tree[2 * idx + 1]
        right = tree[2 * idx + 2]
        if left is not None and right is not None:
            if left[0] < right[0]:
                tree[idx] = left
            else:
                tree[idx] = right
        elif left is not None:
            tree[idx] = left
        elif right is not None:
            tree[idx] = right
        idx -= 1
    sorted_arr = []
    for _ in range(len(arr)):
        sorted_arr.append(tree[0][0])
        pos = tree[0][1] + len(tree) - len(arr)
        tree[pos] = None
        idx = (pos - 1) // 2
        while idx >= 0:
            left = tree[2 * idx + 1]
            right = tree[2 * idx + 2]
            if left is not None and right is not None:
                if left[0] < right[0]:
                    tree[idx] = left
                else:
                    tree[idx] = right
            elif left is not None:
                tree[idx] = left
            elif right is not None:
                tree[idx] = right
            else:
                tree[idx] = None
            if idx == 0:
                break
            idx = (idx - 1) // 2
    return sorted_arr


print(tournament_sort([1, 8, 12, 0, 123, 900, 1244, 2]))
