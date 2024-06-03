""" Factorial Program in Python """


class Factorial:

    @staticmethod
    def factorial(num: int) -> int:
        if num == 0 or num == 1:
            return 1
        else:
            result = num * Factorial.factorial(num - 1)
        return result


if __name__ == '__main__':
    print(Factorial.factorial(6))
