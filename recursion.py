# sum of n numbers


# def func(n):
#     if n == 1:
#         return 1
#     return n + func(n-1)

# print(func(10))


# factorial of n numbers

# def factorial(n):
#     if n==1 or n==0:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))


# reverse a list


# def rev(arr,left,right):
#     if left >= right:
#         return arr
    

#     arr[left],arr[right] = arr[right], arr[left]
#     return rev(arr,left+1,right-1)

# def rev_arr(arr,left,right):
#     return(rev(arr, left, right))

# arr = [1,2,3,4,5,6,7,8,9,10]
# print(rev_arr(arr,0,9))

# palindrome

# def palindrom(S,left,right):
#     if left > right:
#         return True
#     if S[left] != S[right]:
#         return False
    
#     return palindrom(S,left+1,right-1)

# def is_palindrome(S,left,right):
#     print(palindrom(S,left,right))

# S = 'ABCCBA'
# left = 0 
# right = len(S)-1

# is_palindrome(S,left,right)

# Fibbonaci

# def fibo(num):
#     if num == 0 or num == 1:
#         return num
    
#     return fibo(num-1) + fibo(num-2)

# def get_fibo(num):
#     print(fibo(num))

# num = 9
# get_fibo(num)


# merge 2 sorted array

# arr1 = [1,3,5,7]
# arr2 = [2,4,6,8]

# def merge_array(arr1,arr2):
#     result = []

#     i,j = 0,0

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             result.append(arr1[i])
#             i+=1
#         else:
#             result.append(arr2[j])
#             j+=1
        
       
#     while i < len(arr1):
#             result.append(arr1[i])
#             i+=1
        
#     while j < len(arr2):
#             result.append(arr2[j])
#             j+=1

#     return result


# # merge sort

# def merge_sort(arr):
     
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr)//2

#     left_half = arr[:mid]
#     right_half = arr[mid:] 
#     left_sort = merge_sort(left_half)
#     right_sort = merge_sort(right_half)

#     return merge_array(left_sort,right_sort)

# arr = [1,4,2,5,6,3,2,6,2,7,4,8,9,5,6,10]
# print(merge_sort(arr))


# quick sort 


# def partition(arr,low,high):

#     i,j = low,high
#     pivot = arr[low]
    
#     while i < j:

#         while arr[i] <= pivot and i <= high-1:
#             i+= 1
#         while arr[j] > pivot and j >= low +1:
#             j -= 1
        
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[low],arr[j] = arr[j], arr[low]
    
#     return j


# def quick_sort(arr, low , high):
#     if low<high:
#         p_index = partition(arr,low,high)
#         quick_sort(arr,low,p_index-1)
#         quick_sort(arr, p_index+1, high)


# arr = [1,5,4,6,3,7,4,2,2,3,7,8,6,3,2,1]
# low = 0
# high = len(arr)-1

# quick_sort(arr,low,high)

# print(arr)




def partition(arr,low,high):
    i,j = low,high
    pivot = arr[low]

    while i < j:

        while arr[i] <= pivot and i <= high-1:
            i+=1
        while arr[j] > pivot and j >= low+1:
            j-=1

        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr,low,high):
    if low < high:
        p_index = partition(arr,low,high)
        quick_sort(arr,low,p_index-1)
        quick_sort(arr,p_index+1,high)

arr = [1,6,4,7,3,9,4,3,2,9,0,10,2,3,4,5,6]

quick_sort(arr,0,len(arr)-1)

print(arr)