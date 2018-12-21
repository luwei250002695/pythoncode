def quick_sort(alist, start, end):  #alist列表，start第一个元素下标，end最后元素下标
    # 递归的退出条件
    if start >= end:
        return
    mid = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and mid <= alist[high]:
            high -= 1
        alist[low] = alist[high]
        while low < high and mid > alist[low]:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)


alist2 = [54, 8888888888888, 26, 93, 17, 77, 31, 4, 45, 5, 17, 17, -1, -11, 20]
quick_sort(alist2, 0, len(alist2) - 1)
print(alist2)
print(quick_sort(alist2, 0, len(alist2) - 1))