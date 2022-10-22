from typing import List

# 198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if(l <= 2):
            return max(nums)
        # 到第二格不偷了
        nums[1] = max(nums[0],nums[1])
        for i in range(2,l):
            nums[i] = max(nums[i-2] + nums[i],nums[i-1])
        return nums[l-1]


if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    num = [2,1,1,2]
    res = solution.rob(num)
    print(f'res->{res}')