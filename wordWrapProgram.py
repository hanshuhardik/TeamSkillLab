class Solution:
    def solveWordWrap(self, arr, k):
        n = len(arr)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0  # No cost for the last line
        track = [-1] * n

        # Start from the last word and calculate costs for each position
        for i in range(n - 1, -1, -1):
            curr_length = 0
            for j in range(i, n):
                curr_length += arr[j] + (1 if j > i else 0)
                if curr_length > k:
                    break
                
                cost = (k - curr_length) ** 2 if j < n - 1 else 0
                if dp[j + 1] + cost < dp[i]:
                    dp[i] = dp[j + 1] + cost
                    track[i] = j
        return dp[0]

# Example usage
arr = [3, 2, 2, 5]
k = 6
sol = Solution()
min_cost = sol.solveWordWrap(arr, k)
print("Minimum cost:", min_cost)
