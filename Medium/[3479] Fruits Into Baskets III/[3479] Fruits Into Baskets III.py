"""
Accepted
3479 [Medium]
Runtime: 1639 ms, faster than 93.29% of Python3 online submissions for Fruits Into Baskets III.
Memory Usage: 46.57 MB, less than 34.23% of Python3 online submissions for Fruits Into Baskets III.
"""
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        def build(baskets, low, high, idx):
            if low == high:
                seg_tree[idx] = baskets[low]
            else:
                mid = (low + high) // 2
                build(baskets, low, mid, idx * 2)
                build(baskets, mid + 1, high, idx * 2 + 1)
                seg_tree[idx] = max(seg_tree[idx * 2], seg_tree[idx * 2 + 1])


        def find(fruit, low, high, idx):
            # If this segment cannot fit the fruit
            if seg_tree[idx] < fruit:
                return False
            # If we're at a leaf, use it
            if low == high:
                seg_tree[idx] = 0
                return True
            
            mid = (low + high) // 2
            if seg_tree[idx * 2] >= fruit:
                res = find(fruit, low, mid, idx * 2)
            else:
                res = find(fruit, mid + 1, high, idx * 2 + 1)
                
            # Update this node after child has changed
            seg_tree[idx] = max(seg_tree[idx * 2], seg_tree[idx * 2 + 1])
            return res


        N = len(baskets)
        seg_tree = [0] * (4 * N)

        build(baskets, 0, N - 1, 1)

        unplaced = 0
        for fruit in fruits:
            if not find(fruit, 0, N - 1, 1):
                unplaced += 1

        return unplaced