from typing import List
import sys

# 题目详情
# 45. 跳跃游戏 II
# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 假设你总是可以到达数组的最后一个位置。

# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

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