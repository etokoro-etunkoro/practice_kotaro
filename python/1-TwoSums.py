class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pair_ans = {}

        for i, num in enumerate(nums):  #enumerate関数→要素とインデックスの取得
            if target - num in pair_ans:
                return [i, pair_ans[target - num]]
            
            pair_ans[num] = i
