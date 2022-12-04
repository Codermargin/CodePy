from typing import List

# 152. 乘积最大子数组
# 泰波那契序列 Tn 定义如下：
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个 32-位 整数。
#
# 子数组 是数组的连续子序列。

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        maxPro,minPro,resMaxPro = nums[0],nums[0],nums[0]
        for i in range(1,l):
            mx,mi = maxPro,minPro
            maxPro = max(mx * nums[i],nums[i],mi * nums[i])
            minPro = min(mi * nums[i],nums[i],mx * nums[i])
            resMaxPro = max(resMaxPro,maxPro)
        return resMaxPro


if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,-2,4]
    # nums = [-2]
    # nums = [-2,3,-4]
    nums = [-4, -3, -2]
    res = solution.maxProduct(nums)
    print(f'res->{res}')