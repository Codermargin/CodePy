from typing import List

# 70. 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
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