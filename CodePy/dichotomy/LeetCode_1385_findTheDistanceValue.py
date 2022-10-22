from typing import List

# 1385. 两个数组间的距离值 https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/
# 给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。
#
# 「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
# 输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# 输出：2

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # 遍历数组1 -> 去数组2找它的位置，并跟前后值比较
        arr2= sorted(arr2)
        cnt = 0
        for num in arr1:
            left = 0
            right = len(arr2) - 1
            while(left <= right):
                mid = (left + right) // 2
                if(num > arr2[mid]):
                    left = mid + 1
                else:
                    right = mid - 1
            # left 是目标插入位置
            if(left == 0):
                if(abs(num - arr2[left]) > d):
                    cnt += 1
            elif(left == len(arr2)):
                if(abs(num - arr2[left - 1]) > d):
                    cnt += 1
            elif(left == len(arr2) - 1):
                if (abs(num - arr2[left]) > d and abs(num - arr2[left - 1]) > d):
                    cnt += 1
            elif(abs(num - arr2[left]) > d and abs(num - arr2[left - 1]) > d and abs(num - arr2[left + 1]) > d):
                cnt += 1
        return cnt

if __name__ == '__main__':
    solution = Solution()
    # arr = [0, 10, 5, 2]
    num = 16
    # arr1=[-227, 537, -655, 993, -526, -518, 679, -420, -53, 120, 187, -203, -567, -75, 464, -472, -324, 16, 215, -773, 862,
    #  -563, -839, -906, -969, 633, -990, 756, -17, -346, 820, -216, 736, 188, -412, 881, -599, -181, -673, 802, 688, 553,
    #  323, -689, 625, 871, -938, -969, -207, -703, 794, 361, 111, -884, 156, -223, -480, -734, -838, -53, 335, 720, -379,
    #  855, -971, -928, 99, -876, 75, 721, -736, -913, 911]
    # arr2=[-440, 599, -760, -115, -814, -611, -944, 23, 305, -734, 524, -429, 406, 673, 731, -607, 357, -84, -202, -325, 292,
    #  -452, 985, -468, 314, 301, -503, -498, -877, 204, 915, 613, 209, -642, -284, -123, 239, 429, 147, 307, 69, 984,
    #  -876, 853, -277, 120, -155, 102, -592, 457, 802, 98, -132, 883, 356, -857, 461, -453, 522, 250, 476, 991, 540,
    #  -852, -485, -637, 999]
    # d=12
    arr1 = [2, 1, 100, 3]
    arr2 = [-5, -2, 10, -3, 7]
    d = 6
    res = solution.findTheDistanceValue(arr1,arr2,d)
    print(f'res->{res}')