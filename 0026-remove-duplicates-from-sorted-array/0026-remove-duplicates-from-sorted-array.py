class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        # freq_map={}
        # for i in range(0,n):
        #     freq_map[nums[i]]=0
        # j=0
        # for k in freq_map:
        #     nums[j]=k
        #     j+=1
        # return j 
        i=0
        j=i+1
        while j<n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1    
        return i+1               
        