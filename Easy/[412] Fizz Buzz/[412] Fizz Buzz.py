"""
Accepted
412 [Easy]
Runtime: 53 ms, faster than 5.62% of Python3 online submissions for Fizz Buzz.
Memory Usage: 17.53 MB, less than 96.29% of Python3 online submissions for Fizz Buzz.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer