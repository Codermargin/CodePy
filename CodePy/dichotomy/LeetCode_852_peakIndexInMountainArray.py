from typing import List

# 852. 山脉数组的峰顶索引 https://leetcode.cn/problems/peak-index-in-a-mountain-array/
# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。

# 输入：arr = [0,1,0]
# 输出：1
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