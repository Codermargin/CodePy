from typing import List

# 746. 使用最小花费爬楼梯
# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
#
# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
#
# 请你计算并返回达到楼梯顶部的最低花费。
# 输入：cost = [10,15,20]
# 输出：15
# 解释：你将从下标为 1 的台阶开始。
# - 支付 15 ，向上爬两个台阶，到达楼梯顶部。
# 总花费为 15 。

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