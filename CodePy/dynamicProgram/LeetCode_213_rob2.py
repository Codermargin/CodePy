from typing import List

# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        # 需要拷贝一份新的数组
        dp = nums.copy()
        # Bool 数组，判断是否有拿过第一个元素
        bool = [True,False]
        if(l > 3):
            dp[2] += nums[0]
            bool.append(True)
        else:
            return max(dp)
        for i in range(3,l):
            if(i == l - 1):
                dp[i] += max(dp[i - 2]-min(nums[0], nums[l - 1]) if bool[i-2] else dp[i - 2],dp[i - 3]-min(nums[0], nums[l - 1]) if bool[i-3] else dp[i - 3])
                break
            bool.append(bool[i - 2] if dp[i - 2] >= dp[i - 3] else bool[i - 3])
            dp[i] += (dp[i - 2] if dp[i - 2] >= dp[i - 3] else dp[i - 3])
        return max(dp[l-1],dp[l-2])
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         l = len(nums)
#         dp = nums.copy()
#         if(l > 3):
#             dp[3] += dp[1]
#         for i in range(4,l):
#             dp[i] += max(dp[i-2],dp[i-3])
#         return max(dp[l-1],dp[l-2])


if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    nums = [2,1,2,6,1,8,10,10]
    res = solution.rob(nums)
    print(f'res->{res}')