class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])      # x part
            result.append(nums[i + n])  # y part
        return result
