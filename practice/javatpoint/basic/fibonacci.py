""" Fibonacci series in Python """


class Fibonacci:

    def __init__(self) -> None:
        # num: int = int(input("Enter your nuber: "))
        self.num = ""
        self.first = 0
        self.second = 1
        self.temp = 0
        self.fibo = "0 1"

    def generate_fibonacci_till_n(self, num: int) -> str:
        self.num = num
        if self.num == 0:
            return "0"
        elif self.num == 1:
            return "0 1 1"
        else:
            self.temp = self.first + self.second
            self.first = self.second
            self.second = self.temp
            if self.temp <= self.num:
                self.fibo = self.fibo + " " + str(self.temp)
                self.generate_fibonacci_till_n(num)

        return self.fibo

    def generate_n_fibonaci(self, num) -> str:
        self.num = num
        if self.num == 0:
            return "Invalid Input -" + str(self.num)
        if self.num == 1:
            return "0 1"
        else:
            self.temp = self.first + self.second
            self.first = self.second
            self.second = self.temp
            self.fibo = self.fibo + " " + str(self.temp)
            self.generate_n_fibonaci(self.num-1)
        return self.fibo


if __name__ == '__main__':
    print(Fibonacci().generate_fibonacci_till_n(2583))
    print(Fibonacci().generate_n_fibonaci(18))
