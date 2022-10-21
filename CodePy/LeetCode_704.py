from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while(left <= right):
            mid = int((left + right) / 2)
            if(mid > len(nums) - 1): break
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    res = solution.search(nums,target)
    print(f'res->{res}')