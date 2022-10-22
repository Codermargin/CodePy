from typing import List

# 744. 寻找比目标字母大的最小字母
# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
#
# 在比较时，字母是依序循环出现的。举个例子：
#
# 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
# 输入: letters = ["c", "f", "j"]，target = "a"
# 输出: "c"
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        if(letters[right] > target):
            while(left < right):
                mid = (left + right) // 2
                if(mid == len(letters) - 1):
                    break
                if(letters[mid] <= target and letters[mid + 1] > target):
                    return letters[mid + 1]
                elif(letters[mid] <= target):
                    left = mid
                else:
                    right = mid
        return letters[0]

if __name__ == '__main__':
    solution = Solution()
    # letters = ["e","e","e","e","e","e","n","n","n","n"]
    # target = "n"
    letters = ["c","f","j"]
    target = "z"
    res = solution.nextGreatestLetter(letters,target)
    print(f'res->{res}')