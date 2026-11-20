class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for num in nums:
            a[num] =  a.get(num,0)+1
        
        b=[[] for i in range(len(nums)+1)]

        for num,freq in a.items():
            b[freq].append(num)
        out=[]
        for freq in range(len(b)-1,-1,-1):
            for num in b[freq]:
                out.append(num)
                if len(out) >=k:
                     return out




        




        