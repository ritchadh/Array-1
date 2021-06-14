# Product of Array Except Self

# Time Complexity: O(n)
# Space Complexity: O(n) because of the extra array space we used
# Did this code successfully run on Leetcode: all test cases passed
# Any problem you faced while coding this: No

# Approach 1: Take all the multipliers from the left side of the array except for the number at the index itself, (running muliplication)
# Also, take all the multipliers from the right side. Multiply the result of both the array and return the output.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # len(nums) > = 2
        
        if len(nums) == 0 or nums is None:
            return 0 
        
        # Left direction array
        lda = [1 for i in range(len(nums))]
        print(lda)
        lm = 1
        
        for idx,i in enumerate(nums):
            
            lda[idx] = lm
            lm = lm * i

        # Right direction array
        rda = [1 for i in range(len(nums))]
        rm = 1

        j = len(nums)-1
        while(j >= 0):
            
            rda[j] = rm
            rm = rm * nums[j]
            j=j-1

        # Multiply both the indices of the left and the right arrays and return the output
            
        for i in range(0,len(nums)):
            lda[i] = lda[i] * rda[i]
        
        return lda

# SPACE OPTIMAL SOLUTION

# Time Complexity: O(n)
# Space Complexity: O(1) because of the extra array space we used
# Approach 2: Reduce the same complexity to O(1) by eliminating the use of array rda

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # len(nums) > = 2
        
        if len(nums) == 0 or nums is None:
            return 0 
        
        # left direction array
        lda = [1 for i in range(len(nums))]
        print(lda)
        lm = 1
        rm = 1
        
        for idx,i in enumerate(nums):
            
            lda[idx] = lm
            lm = lm * i
        
        j = len(nums)-1
        while(j >= 0):
            
            lda[j] = lda[j] * rm
            rm = rm * nums[j]
            j=j-1
        
        return lda
        

