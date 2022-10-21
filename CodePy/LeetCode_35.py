from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(len(nums) == 1):
            return 0 if nums[0] >= target else 1
        mid = int( (0 + len(nums)) / 2)
        start = 0
        end = len(nums) - 1
        while(mid >= start and mid <= end):
            if(target == nums[mid]):
                return mid
            elif(target > nums[mid]):
                if(mid == end): break
                if(target < nums[mid + 1]):
                    return mid + 1
                else:
                    mid += 1
            elif(target < nums[mid]):
                if (mid == start): break
                if(target > nums[mid - 1]):
                    return mid

                else:
                    mid -= 1
        return 0 if mid <= 0 else len(nums)

if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,5]
    target = 4
    res = solution.searchInsert(nums,target)
    print(f'res->{res}')