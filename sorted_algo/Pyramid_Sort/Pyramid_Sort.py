def pyramid_sort(arr):
    def sift_down(arr, start, end):
        root = start
        while (root * 2 + 1) <= end:
            child = root * 2 + 1
            swap = root
            if arr[swap] < arr[child]:
                swap = child
            if (child + 1) <= end and arr[swap] < arr[child + 1]:
                swap = child + 1
            if swap != root:
                arr[root], arr[swap] = arr[swap], arr[root]
                root = swap
            else:
                return

    n = len(arr)
    for start in range((n - 2) // 2, -1, -1):
        sift_down(arr, start, n - 1)
    for end in range(n - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        sift_down(arr, 0, end - 1)
    return arr


print(pyramid_sort([1, 8, 12, 0, 123, 900, 1244, 2]))
