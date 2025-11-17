# def find_hcf(a, b):
#     while b%a != 0:
#         a, b = b, b % a
#     return a
# def find_lcm(a, b):
#     return (a * b) // find_hcf(a, b)



# print(find_hcf(5,10))
# print(find_lcm(5,10))


## common GCD of an array

def find_hcf(arr):
    smallest = min(arr)
    largest = max(arr)
    while largest % smallest != 0:
        largest , smallest = smallest , largest% smallest
    return smallest


print(find_hcf([1,2,3,4,5,6,7,8,9,10]))

