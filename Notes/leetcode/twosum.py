class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for key, value in enumerate(nums):
            complement = target - value
            if dictionary.__contains__(complement):
                return [dictionary.get(complement), key]
            else:
                dictionary[value] = key


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 3], 6))
