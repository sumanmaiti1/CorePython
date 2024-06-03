""" Prime Number in Python"""


class Prime:

    @staticmethod
    def is_prime(num: int) -> bool:
        if num in [0, 1]:
            return False
        for i in range(num-1, 1, -1):
            if num % i == 0:
                return False
            else:
                continue
        return True


if __name__ == '__main__':
    print(Prime.is_prime(5))
