def find_maximum(arr):
    maximum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum


arr = [12, 45, 7, 89, 34, 23]

result = find_maximum(arr)

print("Maximum element:", result)