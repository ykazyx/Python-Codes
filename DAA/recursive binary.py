def recursive_binary(a,low,high,key):
    if high >= low:
        mid = (high + low) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            return recursive_binary(a, low, mid - 1, key)
        else:
            return recursive_binary(a, mid + 1, high, key)
    else:
        return 0

n = int(input("Enter the size of the array: "))
a = []
print("Enter the elements of the array: ")
for i in range(n):
    a.append(int(input()))

for i in range(n):
    j = i + 1
    while j < n:
        if a[i] > a [j]:
            num = a[i]
            a[i] = a[j]
            a[j] = num
        j += 1
key = int(input("Enter the element you want to search: "))
found = recursive_binary(a, 0, n - 1 , key)

if found == 0:
    print("Not Found")
else:
    print(f"Found at position {found + 1}")