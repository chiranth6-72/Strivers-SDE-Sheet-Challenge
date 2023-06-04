
# ***  Kadane’s Algorithm : Maximum Subarray Sum in an Array
# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

# The intuition of the algorithm is not to consider the subarray as a part of the answer if its sum is less than 0. A subarray with a sum less than 0 will always reduce our answer and so this type of subarray cannot be a part of the subarray with maximum sum.

import math


def maxSubArray(nums):

    maxim = -math.inf
    start, end = 0, 0
    curSum = 0
    for i in range(len(nums)):
        if curSum == 0:
            start = i
        curSum += nums[i]

        maxim = max(maxim, curSum)
        end = i

        if curSum < 0:
            curSum = 0

    return maxim
