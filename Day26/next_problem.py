def missing_number(arr):
    n = len(arr)
    xor_result = n

    for i in range(n):
        xor_result ^= i
        xor_result ^= arr[i]

    return xor_result


arr = [3, 0, 1]

result = missing_number(arr)

print("Missing number:", result)
