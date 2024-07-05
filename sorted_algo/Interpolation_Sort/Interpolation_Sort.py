def interpolation_search(arr, x):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


def interpolation_sort(arr):
    arr.sort()  # Requires the array to be sorted for interpolation search
    return arr


arr = [12, 3, 19, 0, 5, 14, 7, 9, 18, 15]
sorted_arr = interpolation_sort(arr.copy())
print("Sorted Array:", sorted_arr)

x = 9
index = interpolation_search(sorted_arr, x)
if index != -1:
    print(f"Element {x} found at index {index}")
else:
    print(f"Element {x} not found in the array")
