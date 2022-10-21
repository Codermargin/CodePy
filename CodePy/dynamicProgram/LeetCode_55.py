from typing import List


class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     l = len(nums)
    #     # if(l == 1): return True
    #     # 最大行动步数，剩下数组
    #     def help(maxStep,arr) -> bool:
    #         if(maxStep >= len(arr)): return True
    #         for i in range(0,maxStep):
    #             if(arr[i] == 0): continue
    #             # 能跳到终点
    #             if(arr[i] >= len(arr) - 1 - i):
    #                 return True
    #             canGoFinal = help(arr[i],arr[i+1 : len(arr)])
    #             if(i != maxStep - 1 and not canGoFinal) :
    #                 continue
    #             if(canGoFinal) : return True
    #         return False
    #
    #     return help(nums[0], nums[1:l]    def canJump(self, nums: List[int]) -> bool:
    #         l = len(nums)
    #         maxPos = 0
    #         for i in range(l):
    #             if(i > maxPos): return False
    #             maxPos = max(i + nums[i],maxPos)
    #         return True)
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        maxPos = 0
        for i in range(l):
            if(i > maxPos): return False
            maxPos = max(i + nums[i],maxPos)
        return True


if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    res = solution.canJump(nums)
    print(f'res->{res}')