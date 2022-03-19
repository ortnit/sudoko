from lib.sudoku import Sudoku
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')

board: list[list[int]] = [
    [0, 0, 5, 0, 0, 7, 0, 0, 0],
    [6, 0, 0, 3, 4, 0, 1, 0, 0],
    [0, 0, 1, 0, 6, 0, 2, 0, 0],
    [3, 0, 4, 9, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 5, 0, 6],
    [4, 0, 0, 6, 8, 5, 0, 0, 0],
    [1, 2, 0, 0, 0, 4, 9, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 7, 0],
]


def main():
    sudoko = Sudoku(board)
    print('start board:')
    sudoko.show_board()

    sudoko.solve()

    print()
    print('result:')

    sudoko.show_board()


if __name__ == '__main__':
    main()
