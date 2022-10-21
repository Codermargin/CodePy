from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 1 or x == 0): return x
        left = 0
        right = x
        while(left < right):
            mid = (left + right) // 2
            if(mid * mid == x):
                return mid
            elif((right - left) == 1):
                return left
            elif(mid * mid > x):
                right = mid
            else:
                left = mid

if __name__ == '__main__':
    solution = Solution()
    x = 0
    res = solution.mySqrt(x)
    print(f'res->{res}')