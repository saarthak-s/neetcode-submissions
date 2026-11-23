class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1

        bucket=[[] for _ in range(len(nums))]
        for key,value in count.items():
            bucket[value-1].append(key)

        out=[]
        for i in range(len(nums)-1,-1,-1):
            for num in bucket[i]:
                if len(out) != k:
                    out.append(num)
        return out
