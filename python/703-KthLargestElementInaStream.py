import heapq
class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)    #KthLargest自身の持つスコアをヒープにする
        
        while len(self.nums) > k:
            heapq.heappop(self.nums)
            #k位以内に収まるまで、最小スコアから追放していく...

    def add(self, val):
        heapq.heappush(self.nums, val)  #新しいスコアをヒープの中に入れていく
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        #常にheapがk個であるようにすれば、自動的に最小のものがk位になるということか...
        
