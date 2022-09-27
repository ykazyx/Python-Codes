def partition(a, low, high):
    pivot = a[low]
    start = low
    end = high
    while start < end:
        while a[start] <= pivot:
            start += 1
        while a[end] > pivot:
            end -= 1
        if start < end:
            a[start], a[end] = a[end], a[start]
    a[low], a[end] = a[end], a[low]
    return pivot

def quicksort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quicksort(a, low, pi-1)  
        quicksort(a, pi+1, high)  
    return a


arr = [7,6,10,5,9,2,1,15,7]
print(quicksort(arr, 0, len(arr)-1))



























# def partition(l, r, nums):
#     pivot, ptr = nums[r], l
#     for i in range(l, r):
#         if nums[i] <= pivot:
#             nums[i], nums[ptr] = nums[ptr], nums[i]
#             ptr += 1
#     nums[ptr], nums[r] = nums[r], nums[ptr]
#     return ptr
 
# def quicksort(l, r, nums):
#     if len(nums) == 1:  
#         return nums
#     if l < r:
#         pi = partition(l, r, nums)
#         quicksort(l, pi-1, nums)  
#         quicksort(pi+1, r, nums)  
#     return nums
 
 

