# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i] , arr[min_index] = arr[min_index] , arr[i]
#         # print(f"pass {i+1}:", arr)
#     return arr

# print(selection_sort([1,6,4,7,3,4,9,6,8,4,6,4,3,7,6,4,8,4,5]))


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    
    return arr

print(selection_sort([1,5,7,4,3,8,5,9,6,3,4,7,0,4]))
