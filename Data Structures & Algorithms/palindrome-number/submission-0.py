class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        reversed_x = 0

        while temp > 0:
            last_digit = temp % 10
            reversed_x = reversed_x * 10 + last_digit

            temp = temp // 10

        return reversed_x == x