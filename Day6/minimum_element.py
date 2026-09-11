def find_minimum(arr):
    minimum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]

    return minimum


arr = [12, 45, 7, 89, 34, 23]

result = find_minimum(arr)

print("Minimum element:", result)