from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while(left < right):
            mid = (left + right) // 2
            if(arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]):
                return mid
            elif(arr[mid] < arr[mid + 1]):
                left = mid
            else:
                right = mid

if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    res = solution.peakIndexInMountainArray(arr)
    print(f'res->{res}')