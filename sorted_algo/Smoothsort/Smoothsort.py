def smoothsort(arr):
    def sift(arr, pshift, head):
        while pshift > 1:
            rt = head - 1
            lf = head - 1 - pshift // 2
            if arr[head] >= arr[lf] and arr[head] >= arr[rt]:
                break
            if arr[lf] >= arr[rt]:
                arr[head], arr[lf] = arr[lf], arr[head]
                head = lf
                pshift = pshift // 2
            else:
                arr[head], arr[rt] = arr[rt], arr[head]
                head = rt
                pshift = pshift - 1 - pshift // 2

    def trinkle(arr, p, pshift, head, trusty):
        while p != 0:
            while (p & 1) == 0:
                p = p >> 1
                pshift += 1
            head = head - lp[pshift]
            if p == 1 or arr[head] <= arr[head + lp[pshift]]:
                p = (p - 1) >> 1
                pshift -= 1
            else:
                break
        sift(arr, pshift, head)

    def semitrinkle(arr, p, pshift, head):
        head = head - lp[pshift - 1]
        if arr[head] > arr[head + lp[pshift]]:
            arr[head], arr[head + lp[pshift]] = arr[head + lp[pshift]], arr[head]
        sift(arr, pshift - 1, head)

    n = len(arr)
    lp = [1, 1]
    while lp[-1] < n:
        lp.append(lp[-1] + lp[-2] + 1)

    p = 1
    pshift = 1
    head = 1

    while head < n:
        if (p & 3) == 3:
            sift(arr, pshift, head)
            p = (p + 1) >> 2
            pshift += 2
        else:
            if lp[pshift - 1] >= n - head:
                trinkle(arr, p, pshift, head, False)
            else:
                sift(arr, pshift, head)
            if pshift == 1:
                p = p << 1
                pshift -= 1
            else:
                p = (p << 1) + 1
                pshift -= 1
        head += 1

    trinkle(arr, p, pshift, head, False)

    while pshift != 1 or p != 1:
        if pshift <= 1:
            while (p & 1) == 0:
                p = p >> 1
                pshift += 1
            p = p - 1
        else:
            if pshift == 2:
                p = p << 1
                pshift -= 1
            else:
                p = (p << 1) - 1
                pshift -= 2
        semitrinkle(arr, p, pshift, head)
        head -= 1


arr = [12, 3, 19, 0, 5, 14, 7, 9, 18, 15]
smoothsort(arr)
print("Sorted Array:", arr)
