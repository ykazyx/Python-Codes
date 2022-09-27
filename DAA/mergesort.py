def mergesort(arr, lb, ub):
    mid = int()
    if lb < ub:
        mid = (lb + ub) // 2
        l = arr[ : mid]
        b = arr[mid: ]
        mergesort(l, lb, mid)
        mergesort(b, mid + 1, ub) 
        merge(arr, lb, mid, ub)

def merge(arr, lb, mid, ub):
    i = lb
    j = mid + 1
    k = 0
    print(arr, lb, mid, ub)
    brr = arr
    while i <= mid and j <= ub:
        if arr[i] < arr[j]:
            brr[k] = arr[i]
            i += 1
            k += 1
        else:
            brr[k] = arr[j]
            j += 1
            k += 1

    while i < mid + 1:
            brr[k] = arr[i]
            i += 1
            k += 1
  
    while j < ub + 1:
            brr[k] = arr[j]
            j += 1
            k += 1
    
    

arr = [10, 6, 9, 12, 5, 29]
mergesort(arr, 0, 5)
print(arr)