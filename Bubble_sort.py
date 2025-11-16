# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]
#                 swapped = True
#         if not swapped:
#             break

#     return arr

# print(bubble_sort([6,3,8,2,9,5,8,4,1,8,]))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True
        if not swapped:
            break

    return arr

print(bubble_sort([1,2,7,6,9,4,5,0,7,3,4,6,3]))

# Time complaxity = O(n^2)
# Space = O(1)