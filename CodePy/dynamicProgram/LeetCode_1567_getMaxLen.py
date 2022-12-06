from typing import List

# 1567. 乘积为正数的最长子数组长度
# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
#
# 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
#
# 请你返回乘积为正数的最长子数组长度。

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        l = len(nums)
        positiveArr,negativeArr = [0] * l , [0] * l
        maxLen = 0
        if(nums[0] > 0):
            positiveArr[0] = 1
        elif(nums[0] < 0):
            negativeArr[0] = 1
        for i in range(1,l):
            if(nums[i] > 0):
                positiveArr[i] = positiveArr[i-1] + 1
                negativeArr[i] = negativeArr[i-1] + 1 if(negativeArr[i-1] > 0) else 0
            elif(nums[i] < 0):
                positiveArr[i] = negativeArr[i-1] + 1 if(negativeArr[i-1] > 0) else 0
                negativeArr[i] = positiveArr[i-1] + 1
            else:
                positiveArr[i] = 0
                negativeArr[i] = 0
            maxLen = max(positiveArr[i],maxLen)
        return maxLen

# class Solution:
#     def getMaxLen(self, nums: List[int]) -> int:
#         l = len(nums)
#         maxLen =  0
#         negative_cnt = 0
#         curMaxLen,preMaxLen = 0,0
#         for i in range(l):
#             if(nums[i] > 0):
#                 curMaxLen += 1
#             elif(nums[i] < 0):
#                 negative_cnt += 1
#                 if(negative_cnt % 2 != 0):
#                     preMaxLen = curMaxLen
#                     curMaxLen = 0
#                 elif(negative_cnt % 2 == 0):
#                     curMaxLen += preMaxLen + negative_cnt
#                     negative_cnt = 0
#             else:
#                 curMaxLen = 0
#                 negative_cnt = 0
#                 preMaxLen = 0
#                 # curPartMaxLen = 0
#             maxLen = max(curMaxLen,maxLen)
#         return maxLen

if __name__ == '__main__':
    solution = Solution()
    nums = [1,-2,-3,4]
    # nums = [0, 1, -2, -3, -4]
    # nums = [-1, -2, -3, 0, 1]
    # nums = [1,2,3,5,-6,4,0,10]
    # nums = [9,10,1,0,19,20,-28,30,-12,20,11,-8,7,21,-26]
    # nums = [-16,0,-5,2,2,-13,11,8]
    nums = [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
    res = solution.getMaxLen(nums)
    print(f'res->{res}')