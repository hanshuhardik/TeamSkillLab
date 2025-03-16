#linear Search 

def missing_number_linear(arr):
    d = (arr[-1] - arr[0]) // (len(arr) + 1 - 1)  # Correct common difference
    print(d)
    for i in range(len(arr) - 1):  
        if arr[i+1] - arr[i] != d:  # If gap is wrong, missing number is found
            return arr[i] + d  # Return the missing number

    return -1  # No missing number
# Example usage:
arr = [2, 4, 8, 10]  # Missing 6
print(missing_number_linear(arr))  # Output: 6




#Binaray search 

def missing_number_binary_search(arr):
    n = len(arr) +1  # Total number of terms in original AP
    # Calculate the common difference based on the first and last terms
    d = (arr[-1] - arr[0]) // (n-1)  # Corrected formula for d

    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        expected_value = arr[0] + mid * d  # Expected value at mid

        if arr[mid] == expected_value:
            left = mid + 1  # Move right
        else:
            right = mid  # Move left

    return arr[0] + left * d  # Return missing number

# Example usage:
arr = [2, 4, 6, 10, 12]  # Missing 8
print(missing_number_binary_search(arr))  # Output: 8# Example usage:

