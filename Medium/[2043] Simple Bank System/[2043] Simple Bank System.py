"""
Accepted
2043 [Medium]
Runtime: 40 ms, faster than 40.29% of Python3 online submissions for Simple Bank System.
Memory Usage: 47.69 MB, less than 82.51% of Python3 online submissions for Simple Bank System.
"""
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (0 < account1 <= len(self.balance) and 0 < account2 <= len(self.balance)):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not (0 < account <= len(self.balance)):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not (0 < account <= len(self.balance)):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)