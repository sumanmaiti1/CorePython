""" Palindrome Number in Python"""


class Palindrome:

    @staticmethod
    def is_palindrome_num(num):
        result, sum1 = num, 0

        while result > 0:
            reminder = result % 10
            sum1 = sum1 * 10 + reminder
            result = result // 10
        print(f"{num} is Palindrome.") if (sum1 == num) else print(f"{num} is NOT Palindrome.")

    @staticmethod
    def is_palindrome_str(str1):
        print(f"{str1} is Palindrome.") if (str1[::-1] == str1) else print(f"{str1} is NOT Palindrome.")


if __name__ == '__main__':
    Palindrome.is_palindrome_num(12321)
    Palindrome.is_palindrome_str("ABCBA")
    Palindrome.is_palindrome_num(1234)
    Palindrome.is_palindrome_str("ABbA")
