from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2]
        for i in range(2, n):
            arr.append(arr[i - 2] + arr[i - 1])
        return arr[n - 1]


if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    num = 4
    res = solution.climbStairs(num)
    print(f'res->{res}')