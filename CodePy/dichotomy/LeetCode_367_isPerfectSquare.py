from typing import List

# 367. 有效的完全平方数 https://leetcode.cn/problems/valid-perfect-square/
#
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#
# 进阶：不要 使用任何内置的库函数，如  sqrt 。
# 输入：num = 16
# 输出：true

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while(left < right):
            mid = (left + right) // 2
            if(mid * mid == num):
                return True
            elif(mid * mid < num):
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    num = 16
    res = solution.isPerfectSquare(num)
    print(f'res->{res}')