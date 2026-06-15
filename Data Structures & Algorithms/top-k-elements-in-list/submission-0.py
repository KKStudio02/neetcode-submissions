class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        top_k = heapq.nlargest(k, freq.items(), key=lambda item:item[1])
        return [num for num,count in top_k]