from typing import List

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