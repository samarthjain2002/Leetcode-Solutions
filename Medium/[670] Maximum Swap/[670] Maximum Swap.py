"""
Accepted
670 [Medium]
Runtime: 29 ms, faster than 88.62% of Python3 online submissions for Maximum Swap.
Memory Usage:  16.36 MB, less than 97.49% of Python3 online submissions for Maximum Swap.
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = []
        for dig in str(num):
            arr.append(int(dig))
        N = len(arr)

        hashMap = defaultdict(int)
        for i, dig in enumerate(arr):
            hashMap[dig] = i

        flag = False
        for i, dig in enumerate(arr):
            for j in range(9, -1, -1):
                if j > dig and i < hashMap[j]:
                    temp = dig
                    arr[i] = j
                    arr[hashMap[j]] = temp
                    flag = True
                    break
            if flag:
                break
        
        res = ""
        for dig in arr:
            res += str(dig)
        return int(res)



"""
Runtime: 32 ms, faster than 74.49% of Python3 online submissions for Maximum Swap.
Memory Usage:  16.54 MB, less than 42.30% of Python3 online submissions for Maximum Swap.
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = []
        for dig in str(num):
            arr.append(int(dig))
        N = len(arr)

        hashMap = defaultdict(int)
        for dig in arr:
            hashMap[dig] += 1
            
        flag = False
        for i, dig in enumerate(arr):
            for j in range(9, -1, -1):
                if j > dig and hashMap[j] > 0:
                    for k in range(N - 1, -1, -1):
                        if arr[k] == j:
                            temp = arr[k]
                            arr[k] = dig
                            arr[i] = temp
                            flag = True
                            break
                if flag:
                    break
            hashMap[dig] -= 1
            if flag:
                break

        res = ""
        for dig in arr:
            res += str(dig)
        return int(res)