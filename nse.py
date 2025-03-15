def nextSmallerElement(arr):
    n = len(arr)
    nse = [-1] * n  # Initialize NSE array with -1
    stack = []  # Stack to keep track of elements

    # Traverse array from right to left
    for i in range(n - 1, -1, -1):
        # Remove all elements larger than or equal to arr[i]
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        # If stack is not empty, the top is the next smaller element
        if stack:
            nse[i] = stack[-1]

        # Push current element onto the stack
        stack.append(arr[i])

    return nse

# Example Test Cases
arr1 = [4, 8, 5, 2, 25]
print(nextSmallerElement(arr1))  # Output: [2, 5, 2, -1, -1]

arr2 = [13, 7, 6, 12]
print(nextSmallerElement(arr2))  # Output: [7, 6, -1, -1]
