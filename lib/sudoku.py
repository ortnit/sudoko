import logging

logger = logging.getLogger(__name__)


class Sudoku:
    board: list[list[int]]

    def __init__(self, board):
        self.board = board

    def _number_in_row(self, y: int, number: int) -> bool:
        """
        will test if number is available in the row given at the y coordinate.
        :param y:
        :param number:
        :return:
        """
        for field in self.board[y]:
            if field == number:
                return True
        return False

    def _number_in_column(self, x: int, number: int) -> bool:
        """
        will test if number is available in the column given at the x coordinate.
        :param x:
        :param number:
        :return:
        """
        for row in self.board:
            if row[x] == number:
                return True
        return False

    def _number_in_box(self, x: int, y: int, number: int) -> bool:
        """
        will test for a certain coordinate if the number is available inside the box containing the coordinate.
        :param x:
        :param y:
        :param number:
        :return:
        """
        box_x = x - (x % 3)
        box_y = y - (y % 3)
        for y_position in range(box_y, box_y + 3):
            for x_position in range(box_x, box_x + 3):
                if self.board[y_position][x_position] == number:
                    return True
        return False

    def _number_available(self, x: int, y: int, number: int) -> bool:
        """
        tests if nummer is available at the given coordinate, testing the row, column and box.
        :param x: x-coordinate
        :param y: y-coordinate
        :param number: the number to test for availability
        :return: tests if the number is can be set and is available
        """
        return not self._number_in_box(x, y, number) \
               and not self._number_in_row(y, number) \
               and not self._number_in_column(x, number)

    def solve(self) -> bool:
        """
        solves the board bei recursively brute forcing the board. If it doesn't find
        a number for a field it will go back by recursion till it can find a new number

        :return:
        """
        for y, row in enumerate(self.board):
            for x, field in enumerate(row):
                if field == 0:
                    for number in range(1, 10):
                        if self._number_available(x, y, number):
                            logger.debug(f"setting {number} for {x}/{y}")
                            self.board[y][x] = number
                            logger.debug(f"starting recursion")
                            if self.solve():
                                return True
                            logger.debug(f"resetting {x}/{y} to 0")
                            self.board[y][x] = 0
                    logger.debug(f"no number found")
                    return False
                else:
                    logger.debug(f"skipping {x}/{y}; value: {field}")
        return True

    def show_board(self) -> None:
        """
        displays the board in its current state into the console

        :return:
        """
        for y, row in enumerate(self.board):
            if y % 3 == 0 and y != 0:
                print('-----------')
            for x, field in enumerate(row):
                if x % 3 == 0 and x != 0:
                    print('|', end='')
                print(field, end='')
            print()
