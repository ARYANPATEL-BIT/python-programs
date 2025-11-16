# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         key = arr[i]
#         j = i -1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key


#     return arr

# print(insertion_sort([1,5,3,7,5,4,8,7,4,8,5]))


# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1,n):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1

#         arr[j+1] = key
    
#     return arr

# print(insertion_sort([1,6,8,4,6,2,9,5,0,3,6,5,8,5]))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

print(insertion_sort([1,5,3,7,6,8,4,5,3,2,4,6,4,6]))