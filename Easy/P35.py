from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    k = [x for x in nums if x < target]
    w = len(k)
    return w



searchInsert([1,2,4,5], 4)