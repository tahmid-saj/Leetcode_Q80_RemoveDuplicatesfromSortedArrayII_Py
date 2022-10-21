class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for c in nums:
            if index < 2 or c > nums[index-2]:
                nums[index] = c
                index += 1
        return index
