class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        prev_index = None
        for i in nums:
            if i != prev_index:
                nums[index] = i
                index+=1
                prev_index = i
                
                
        return index
        
        
        # Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
