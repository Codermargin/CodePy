from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxVal = max(nums)
        arr = [0] * (maxVal + 1)
        for num in nums:
            arr[num] += num

        def rob(dp: List[int]) -> int:
            l = len(dp)
            dp[1] = max(dp[0],dp[1])
            for i in range(2,l):
                # 到这个位置我不偷了dp[i-1] 或者 偷间隔之前的
                dp[i] = max(dp[i-2]+dp[i],dp[i-1])
            return dp[l-1]
        return rob(arr)

if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    nums = [2,2,3,3,3,4]
    res = solution.deleteAndEarn(nums)
    print(f'res->{res}')