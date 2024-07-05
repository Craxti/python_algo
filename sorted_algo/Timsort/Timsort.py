def tim_sort(arr):
    min_run = 32

    def insertion_sort(sub_arr):
        for i in range(1, len(sub_arr)):
            key = sub_arr[i]
            j = i - 1
            while j >= 0 and key < sub_arr[j]:
                sub_arr[j + 1] = sub_arr[j]
                j -= 1
            sub_arr[j + 1] = key

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr[i:i + min_run])

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n, start + size)
            end = min(n, start + size * 2)
            arr[start:end] = merge(arr[start:mid], arr[mid:end])
        size *= 2
    return arr


print(tim_sort([1, 8, 12, 0, 123, 900, 1244, 2]))
