class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n==0:
            return
        k=k%n
        nums[:]=nums[n-k:]+nums[:n-k]    
        