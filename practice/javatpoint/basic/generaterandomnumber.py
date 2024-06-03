""" Generate Random Number in Python """
import random


class RandomNumber:

    @staticmethod
    def random_number_of_n_bits(bits: int) -> int:
        if bits <= 0:
            print("Invalid Input" + str(bits))
            exit()
        number: int = 0
        for i in range(1, bits + 1):
            rnd = random.randint(0, 9)
            number = number + (rnd * (10 ** (i - 1)))
        return number

    @staticmethod
    def random_number_between_limit(num1: int , num2: int):
        return random.randint(num1, num2)


if __name__ == '__main__':
    #print(RandomNumber.random_number_of_n_bits(0))
    print(RandomNumber.random_number_of_n_bits(1))
    print(RandomNumber.random_number_of_n_bits(2))
    print(RandomNumber.random_number_of_n_bits(4))

    print(RandomNumber.random_number_between_limit(-100,200))
    print(RandomNumber.random_number_between_limit(100,999))