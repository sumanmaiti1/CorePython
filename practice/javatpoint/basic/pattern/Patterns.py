""" RDifferent Patterns in Python """


class Pattern:

    @staticmethod
    def right_triangle(no_of_rows: int, fill: str) -> None:
        for i in range(no_of_rows):
            strrow = (fill + " ") * (i + 1)
            print(strrow)

    @staticmethod
    def left_triangle(no_of_rows: int, fill: str) -> None:
        total_string_length = (2 * no_of_rows) - 1
        for i in range(no_of_rows):
            strfill = (fill + " ") * (i + 1)
            strspace = " " * (total_string_length - len(strfill) + 1)
            print(strspace + strfill)

    @staticmethod
    def pyramid(no_of_rows: int, fill: str) -> None:
        total_string_length = (2 * no_of_rows) - 1
        for i in range(1, no_of_rows + 1):
            str_fill = ((fill + " ") * i)[:-1]
            str_pre_post_fill = " " * ((total_string_length - len(str_fill)) // 2)
            print(str_pre_post_fill + str_fill + str_pre_post_fill)

    @staticmethod
    def diamond(no_of_rows: int, fill: str) -> None:
        total_string_length = (2 * no_of_rows) - 1
        diamond_list: list = [''] * no_of_rows

        if no_of_rows % 2 != 0:
            no_of_rows += 1

        for i in range(1, (no_of_rows // 2) + 1):
            str_fill = ((fill + " ") * i)[:-1]
            str_pre_post_fill = " " * ((total_string_length - len(str_fill)) // 2)
            str_row = str_pre_post_fill + str_fill + str_pre_post_fill
            diamond_list[i-1], diamond_list[-i] = str_row, str_row

        for i in diamond_list:
            print(i)

    @staticmethod
    def downward_triangle(no_of_rows: int, fill: str) -> None:
        for i in range(1, no_of_rows + 1):
            str_row = ((fill + " ") * (no_of_rows + 1 - i))[:-1]
            print(str_row)

    @staticmethod
    def reverse_pyramid(no_of_rows: int, fill: str) -> None:
        for i in range(1, no_of_rows + 1):
            str_pre_post_fill = (" " * (i-1))
            str_row = str_pre_post_fill + ((fill + " ") * (no_of_rows + 1 - i))[:-1] + str_pre_post_fill
            print(str_row)

    @staticmethod
    def right_down_mirror(no_of_rows: int, fill: str) -> None:
        no_of_character = (2 * no_of_rows) - 1
        for i in range(1, no_of_rows + 1):
            strfill = ((" " + fill) * (no_of_rows - i + 1))[1:]
            strrow = (" " * (no_of_character - len(strfill))) + strfill
            print(strrow)
        pass

    @staticmethod
    def right_pascal_triangle(no_of_rows: int, fill: str) -> None:
        pattern_list: list = [""] * (2 * no_of_rows - 1)
        for i in range(1, no_of_rows + 1):
            strrow = ((fill + " ") * i).strip()
            if i == no_of_rows+1:
                pattern_list[no_of_rows] = strrow
            else:
                pattern_list[i-1] = pattern_list[2*no_of_rows-i-1] = strrow

        for item in pattern_list:
            print(item)

    @staticmethod
    def left_pascal_triangle(no_of_rows: int, fill: str) -> None:
        pattern_list: list = [""] * (2 * no_of_rows - 1)
        for i in range(no_of_rows):
            strrow: str = (" " * (2 * no_of_rows - (i * 2) - 2)) + ((fill + " ") * (i + 1))[:-1]
            if i == no_of_rows-1:
                pattern_list[no_of_rows-1] = strrow
            else:
                pattern_list[i] = pattern_list[(2 * no_of_rows - i - 2)] = strrow

        for item in pattern_list:
            print(item)


if __name__ == '__main__':
    a = 1
    # Pattern.right_triangle(5, '%')
    # Pattern.left_triangle(5, '+')
    # Pattern.pyramid(5, '#')
    # Pattern.diamond(9, '+')
    # Pattern.downward_triangle(5, '*')
    # Pattern.reverse_pyramid(5, 'X')
    # Pattern.right_down_mirror(5, '+')
    # Pattern.right_pascal_triangle(5, "+")
    Pattern.left_pascal_triangle(7, "~")
