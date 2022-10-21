from typing import List


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