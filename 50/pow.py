class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        sub_n = self.myPow(x, int(n / 2))
        sub_n_squared = sub_n * sub_n

        if n % 2 == 0:
            return sub_n_squared
        elif n > 0:
            return x * sub_n_squared
        else:
            return sub_n_squared / x
