from typing import List


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