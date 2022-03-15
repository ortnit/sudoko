class Sudoko:
    fields: list = []

    def __init__(self):
        self._build_fields()

    def _build_fields(self):
        self.fields = [[list(range(1, 10)) for y in range(0, 9)] for x in range(0, 9)]

    def output(self):
        for column in self.fields:
            for x, field in enumerate(column):
                if x % 3 == 0:
                    print("|", end="")
                str_list = [str(i) for i in field]
                print(f"{','.join(str_list)}", end="|")
            print()

    def set(self, x: int, y: int, value: int):
        x = x - 1
        y = y - 1

        self._set(x, y, value)

    def _set(self, x: int, y: int, value: int):
        print(f"x: {x + 1}; y: {y + 1}; value: {value};")

        self.fields[y][x] = [value]

        self.check_row(y, value)

        self.check_column(x, value)

        self.check_block(x, y, value)

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
            self._set(x, y, field[0])

