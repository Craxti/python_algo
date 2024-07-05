def bitonic_sort(arr, up=True):
    def bitonic_merge(arr, up):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        for i in range(mid):
            if (arr[i] > arr[i + mid]) == up:
                arr[i], arr[i + mid] = arr[i + mid], arr[i]
        left = bitonic_merge(arr[:mid], up)
        right = bitonic_merge(arr[mid:], up)
        return left + right

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = bitonic_sort(arr[:mid], True)
    right = bitonic_sort(arr[mid:], False)
    return bitonic_merge(left + right, up)


print(bitonic_sort([1, 8, 12, 0, 123, 900, 1244, 2]))
