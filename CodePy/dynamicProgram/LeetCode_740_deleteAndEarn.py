from typing import List

# 740. 删除并获得点数
# 给你一个整数数组 nums ，你可以对它进行一些操作。
#
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。
#
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。

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