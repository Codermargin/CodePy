from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        for i in range(2,l):
            # if( i == len(cost) ):
            #     cost.append(min(cost[i-1],cost[i-2]))
            #     break
            # else:
                cost[i] = min(cost[i-1],cost[i-2]) + cost[i]
        return min(cost[l-1],cost[l-2])


if __name__ == '__main__':
    solution = Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    res = solution.minCostClimbingStairs(cost)
    print(f'res->{res}')