import sys
from typing import List

## 题目详情
# 53. 最大子数组和 ：https://leetcode.cn/problems/maximum-subarray/description/
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        maxSub =  nums[0]
        for i in range(1,l):
            nums[i] = max(nums[i-1] + nums[i],nums[i])
            maxSub = max(nums[i],maxSub)
        return maxSub

if __name__ == '__main__':
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = solution.maxSubArray(nums)
    print(f'res->{res}')