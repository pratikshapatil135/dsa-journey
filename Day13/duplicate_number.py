def find_duplicate(arr):
    slow = arr[0]
    fast = arr[0]

    # Find the meeting point
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]

        if slow == fast:
            break

    # Find the entrance of the cycle
    slow = arr[0]

    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


arr = [1, 3, 4, 2, 2]

result = find_duplicate(arr)

print("Duplicate number:", result)