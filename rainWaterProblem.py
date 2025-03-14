class Solution:
    def maxWater(self, arr):
        lmax = rmax = total = 0
        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l] < arr[r]:
                if arr[l] < lmax:
                    total += lmax - arr[l]
                else:
                    lmax = arr[l]
                l += 1
            else:
                if arr[r] < rmax:
                    total += rmax - arr[r]
                else:
                    rmax = arr[r]
                r -= 1
        return total

# Example usage
arr = [class Solution:
    def maxWater(self, arr):
        lmax = rmax = total = 0
        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l] < arr[r]:
                if arr[l] < lmax:
                    total += lmax - arr[l]
                else:
                    lmax = arr[l]
                l += 1
            else:
                if arr[r] < rmax:
                    total += rmax - arr[r]
                else:
                    rmax = arr[r]
                r -= 1
        return total

# Example usage
# arr=[3, 0,2, 0, 4]
arr = [3, 0, 1, 0, 4, 0, 2]
sol = Solution()
result = sol.maxWater(arr)
print("Trapped water:", result)]
sol = Solution()
result = sol.maxWater(arr)
print("Trapped water:", result)
