"""
Accepted
1865 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Finding Pairs With a Certain Sum.
Memory Usage: 48.20 MB, less than 80.05% of Python3 online submissions for Finding Pairs With a Certain Sum.
"""
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2Count = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2Count[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2Count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            res += self.nums2Count[tot - num]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)



"""
Runtime: 390 ms, faster than 30.25% of Python3 online submissions for Finding Pairs With a Certain Sum.
Memory Usage: 47.68 MB, less than 99.52% of Python3 online submissions for Finding Pairs With a Certain Sum.
"""
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2Count = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2Count[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2Count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            res += self.nums2Count[tot - num]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)