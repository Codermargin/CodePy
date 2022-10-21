from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        dp=[]

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