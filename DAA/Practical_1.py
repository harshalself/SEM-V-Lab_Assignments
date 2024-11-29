def binary_search(arr, key):
    low = 0 
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Taking input from the user
arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter a number: "))
    arr.append(num)

# Sorting the array
arr.sort()

key = int(input("Enter the number to search for: "))

result = binary_search(arr, key)

if result == -1:
    print("Element not found")  
else:
    print(f"Element found at index {result}")
