import math


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list)-1

    time = 0

    while low <= high:
        time += 1
        mid = math.ceil((low+high) / 2)

        if target == sorted_list[mid]:
            return {"index": mid, "time": time}
        elif target <= sorted_list[mid]:
            high = mid-1
        else:
            low = mid+1

    return None


list1 = list(range(1, 129))
list2 = list(range(1, 257))
# print(list)
print(binary_search(list1, 128))
print(binary_search(list2, 255))
