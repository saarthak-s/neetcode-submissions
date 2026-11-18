class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        b=[]
        for freq in a.values():
            b.append(freq)
        b = sorted(b,reverse = True)
        b = b[:k]
        matching_keys = [k for k, v in a.items() if v in b]
        return matching_keys
        



        