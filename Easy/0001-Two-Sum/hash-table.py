class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} # nums_value:nums_index
        for nums_index, nums_value in enumerate(nums):
            diff = target - nums_value
            if diff in hash_table:
                return hash_table[diff], nums_index
            hash_table[nums_value] = nums_index
        return []