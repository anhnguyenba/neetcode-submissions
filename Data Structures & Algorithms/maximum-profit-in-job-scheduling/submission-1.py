class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        index = list(range(n))
        index.sort(key=lambda i: startTime[i])
        
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            left, right, j = i + 1, n, n
            while left < right:
                mid = (left + right) // 2
                if endTime[index[i]] <= startTime[index[mid]]:
                    j = mid
                    right = mid
                else:
                    left = mid + 1
            
            dp[i] = max(dp[i + 1], profit[index[i]] + dp[j])
        
        return dp[0]