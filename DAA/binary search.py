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

print(a)
low = 0
high = n - 1
found = 0
key = int(input("Enter the element you want to search: "))
while low <= high:
    mid = (low + high) // 2
    if key < a[mid]:
        high = mid - 1
    elif key > a[mid]:
        low = mid + 1
    elif key == a[mid]:
        print(f"Found at position {mid+1}")
        found = 1
        break

if found == 0:
    print("Not Found")