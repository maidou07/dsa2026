def QuickSort(alist):
    if len(alist) <= 1:
        return alist
    pivotvalue = alist[0]
    left_list = [alist[i] for i in range(1,len(alist)) if alist[i] <= pivotvalue]
    right_list = [alist[i] for i in range(1,len(alist)) if alist[i] > pivotvalue]
    return QuickSort(left_list)+[pivotvalue]+QuickSort(right_list)

print("0502")
print("- 快速排序测试")
list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("原始 list：")
print(list1)
print("快速排序后的 list：")
print(QuickSort(list1))


