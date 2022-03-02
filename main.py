class Sudoko:
    fields: list = []

    def __init__(self):
        self._build_fields()

    def _build_fields(self):
        self.fields = [[list(range(1, 10)) for y in range(0, 9)] for x in range(0, 9)]

    def output(self):
        for column in self.fields:
            for field in column:
                str_list = [str(i) for i in field]
                print(f"{','.join(str_list)}", end=" ")
            print()

    def set(self, x: int, y: int, value: int):
        x = x - 1
        y = y - 1

        print(f"x: {x + 1}; y: {y + 1}; value: {value};")

        self.fields[y][x] = [value]

        self.check_row(y, value)

        self.check_column(x, value)

        self.check_block(x, y, value)

        # self.output()
        # print('-------------')

    def check_row(self, y: int, value: int):
        for x_index, field in enumerate(self.fields[y]):
            self._remove_from_field(x_index, y, value)

    def check_column(self, x: int, value: int):
        for y_index, row in enumerate(self.fields):
            self._remove_from_field(x, y_index, value)

    def check_block(self, x: int, y: int, value: int):
        for y_offset in range(0, 3):
            y_index = y - (y % 3) + y_offset
            for x_offset in range(0, 3):
                x_index = x - (x % 3) + x_offset
                self._remove_from_field(x_index, y_index, value)

    def _remove_from_field(self, x: int, y: int, value: int):
        field = self.fields[y][x]
        if value not in field or len(field) <= 1:
            return
        field.remove(value)
        self.fields[y][x] = field

        if len(field) == 1:
            print(f"solved x: {x + 1}; y: {y + 1}; value: {field[0]};")
            # exit(0)
            self.set(x + 1, y + 1, field[0])


"""
    rows = x
    columns = y
    
    first level rows
    second level columns
    
    y|x
    
    1,1 1,1 1,1
    
"""


def main():
    sudoko = Sudoko()

    sudoko.set(1, 1, 4)
    sudoko.set(2, 1, 2)
    sudoko.set(3, 1, 7)
    sudoko.set(3, 2, 5)
    sudoko.set(3, 3, 3)
    sudoko.set(1, 3, 6)

    sudoko.set(4, 1, 1)
    sudoko.set(6, 2, 6)

    sudoko.set(8, 1, 6)
    sudoko.set(9, 1, 8)
    sudoko.set(7, 2, 3)
    sudoko.set(7, 3, 1)

    sudoko.set(1, 4, 2)
    sudoko.set(1, 5, 3)
    sudoko.set(2, 5, 4)
    sudoko.set(1, 6, 8)
    sudoko.set(3, 6, 1)

    sudoko.set(5, 4, 1)
    sudoko.set(5, 5, 6)
    sudoko.set(5, 6, 5)
    sudoko.set(6, 5, 7)

    sudoko.set(7, 4, 4)
    sudoko.set(8, 5, 5)
    sudoko.set(9, 5, 1)
    sudoko.set(8, 6, 2)

    sudoko.set(2, 7, 9)
    sudoko.set(1, 8, 7)
    sudoko.set(3, 8, 4)
    sudoko.set(2, 9, 3)
    sudoko.set(3, 9, 2)

    sudoko.set(4, 8, 3)
    sudoko.set(5, 9, 9)
    sudoko.set(6, 9, 4)

    sudoko.set(7, 7, 7)
    sudoko.set(8, 7, 3)
    sudoko.set(7, 8, 2)
    sudoko.set(9, 8, 9)
    sudoko.set(7, 9, 6)

    sudoko.output()


if __name__ == '__main__':
    main()
