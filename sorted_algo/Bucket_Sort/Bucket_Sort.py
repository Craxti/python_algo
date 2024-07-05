from sorted_algo.Insertion_Sort.Insertion_Sort import insertion_sort


def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    bucket = []
    slot_num = 10
    for i in range(slot_num):
        bucket.append([])

    for j in arr:
        index = int(slot_num * j)
        bucket[index].append(j)

    for i in range(slot_num):
        bucket[i] = insertion_sort(bucket[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr


print(bucket_sort([1, 8, 12, 0, 123, 900, 1244, 2]))