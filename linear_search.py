def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([1,9,2,8,3,7,4,6,5,10],4))