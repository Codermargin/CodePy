import sys
from typing import List

## 题目详情
# 918. 环形子数组的最大和 ：https://leetcode.cn/problems/maximum-sum-circular-subarray/?envType=study-plan&id=dong-tai-gui-hua-ru-men&plan=dynamic-programming&plan_progress=4a1b2lj
# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
#
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。
#
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
#
# 子数组 是数组中的一个连续部分。
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3

# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         l = len(nums)
#         nums2 = nums.copy()
#         nums2.insert(0,nums[l - 1])
#         nums2.pop(l)
#         def getMaxSum(nums:List[int]) -> int:
#             l = len(nums)
#             maxSum = nums[0]
#             for i in range(1, l):
#                 nums[i] = max(nums[i], nums[i - 1] + nums[i])
#                 maxSum = max(maxSum, nums[i])
#             return maxSum
#         return max(getMaxSum(nums),getMaxSum(nums2))

# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         nums.extend(nums)
#         l = len(nums)
#         maxSum = nums[0]
#         for i in range(1,l):
#             nums[i] = max(nums[i] + nums[i-1],nums[i]) if nums[i] + nums[i-1] >= maxSum else nums[i]
#             maxSum = max(nums[i],maxSum)
#         return maxSum

# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         originalNums = nums.copy()
#         ol = len(originalNums)
#         nums.extend(nums)
#         l = len(nums)
#         maxSum = nums[0]
#         for i in range(1,l):
#             if(i >= l/2):
#                 nums[i] = max(nums[i] + nums[i-1] - originalNums[i - ol],nums[i],nums[i] + originalNums[i - ol])
#             else:
#                 nums[i] = max(nums[i] + nums[i-1],nums[i])
#             maxSum = max(nums[i],maxSum)
#         return maxSum

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        total = 0
        for i in range(len(nums)):
            curMax = max(curMax + nums[i],nums[i])
            curMin = min(curMin + nums[i],nums[i])
            maxSum = max(curMax,maxSum)
            minSum = min(curMin,minSum)
            total += nums[i]
        return max(maxSum,total - minSum) if maxSum > 0 else maxSum

if __name__ == '__main__':
    solution = Solution()
    nums = [-2,4,-5,4,-5,9,4]
    res = solution.maxSubarraySumCircular(nums)
    print(f'res->{res}')