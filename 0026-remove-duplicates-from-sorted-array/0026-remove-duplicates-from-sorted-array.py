class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            copy = nums
            indices = [index for index, x in enumerate(nums) if x == num ]
            length =  len(indices)
            
            if length > 1:
                while len(indices) > 1:
                    ind = indices.pop()
                    copy.pop(ind)
            k = len(copy)        
        return k