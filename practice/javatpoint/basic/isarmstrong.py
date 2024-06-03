""" Armstrong Number in Python """


class Armstrong:

    @staticmethod
    def is_armstrong(num: int) -> None:
        result, sum1 = num, 0
        while result > 0:
            reminder = result % 10
            sum1 = sum1 + (reminder ** 3)
            result = result // 10

        print(f'{num} is Armstrong Number') if (sum1 == num) else print(f'{num} is NOT Armstrong Number')


if __name__ == '__main__':
    Armstrong.is_armstrong(153)
    Armstrong.is_armstrong(1230)
