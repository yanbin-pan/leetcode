class Solution:
    """Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.

    O(n) time complexity
    """
    def maxSubArray(self, nums: List[int]) -> int:
        Max = nums[0]  #contains max till now
        temp_sum = 0     # contain temporary sum
        
        for i in range(len(nums)):
            temp_sum += nums[i]

            # if Max is less than temp_sum update Max
            if(Max < temp_sum): 
                Max = temp_sum

             # if temp_Sum becomes negative it will only decrease sum value so reset it to 0
             # if temp_sum is positive it will always add to the tot sublist, we want to remove the contriburtion from negative numbers by resetting to 0
             # and account for a new substring
            if temp_sum < 0:
                temp_sum = 0
        return Max