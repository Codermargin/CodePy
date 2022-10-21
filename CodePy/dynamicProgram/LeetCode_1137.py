from typing import List

class Solution:
    def tribonacci(self, n: int) -> int:
        if(n == 0): return 0
        if(n <= 2): return 1
        dp = [0,1,1]
        for i in range(3,n+1):
            dp.append(dp[i - 3] + dp [i - 2] + dp[i - 1])
        return dp[n]

if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    num = 4
    res = solution.tribonacci(num)
    print(f'res->{res}')