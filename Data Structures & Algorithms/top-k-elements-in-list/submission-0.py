class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        sorted_k = sorted(map.items(), key=lambda x: x[1], reverse=True)
        
        return[num for num, count in sorted_k[:k]]
