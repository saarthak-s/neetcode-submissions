class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        store = [1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            store[i] = store[i]*prefix
            prefix = prefix * nums[i]
        
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            store[i] = store[i]*suffix
            suffix = suffix * nums[i]
        return store

    



        