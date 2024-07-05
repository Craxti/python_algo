def weave_sort(arr):
    def weave_merge(a, b):
        result = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            result.append(a[i])
            result.append(b[j])
            i += 1
            j += 1
        result.extend(a[i:])
        result.extend(b[j:])
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = weave_sort(arr[:mid])
    right = weave_sort(arr[mid:])
    return weave_merge(left, right)


print(weave_sort([1, 8, 12, 0, 123, 900, 1244, 2]))

