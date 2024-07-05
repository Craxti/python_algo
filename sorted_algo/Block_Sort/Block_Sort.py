from sorted_algo.Insertion_Sort.Insertion_Sort import insertion_sort


def block_sort(arr):
    if len(arr) <= 1:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    bucket_size = (max_val - min_val) / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_val) / bucket_size)
        if index == len(arr):
            index -= 1
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr


print(block_sort([1, 8, 12, 0, 123, 900, 1244, 2]))
