class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        b=[]
        for num in a.keys():
            heapq.heappush(b,(a[num],num))

            if len(b)>k:
                heapq.heappop(b)
        out=[]
        for i in range(k):
            out.append(heapq.heappop(b)[1])
        return out
        




        