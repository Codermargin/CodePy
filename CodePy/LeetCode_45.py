from typing import List
import sys


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        maxLen = 0
        dp = [sys.maxsize] * l
        dp[0] = 0
        stage = 1
        for i in range(l):
            if(dp[l - 1] != sys.maxsize):
                break
            # 每一格更新后面的步数
            if (i + nums[i] > maxLen):
                for j in range(maxLen + 1, min(i + nums[i] + 1,l)):
                    dp[j] = min(dp[i] + 1, dp[j])
                # 更新最远距离
                maxLen = i + nums[i]
        return dp[l - 1]

if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    nums = [2,1]
    res = solution.jump(nums)
    print(f'res->{res}')