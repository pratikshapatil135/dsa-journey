def move_zeroes(arr):
    non_zero = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero], arr[i] = arr[i], arr[non_zero]
            non_zero += 1

    return arr


arr = [0, 1, 0, 3, 12]

result = move_zeroes(arr)

print("Array after moving zeroes:", result)