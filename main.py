from lib.sudoko import Sudoko

"""
    rows = y
    columns = x
    
    first level rows
    second level columns
    
"""


def main():
    sudoko = Sudoko()

    sudoko.set(3, 2, 7)
    sudoko.set(3, 3, 4)

    sudoko.set(4, 1, 5)
    sudoko.set(5, 1, 6)
    sudoko.set(4, 2, 3)
    sudoko.set(6, 2, 2)
    sudoko.set(5, 3, 9)

    sudoko.set(8, 1, 2)
    sudoko.set(7, 2, 9)
    sudoko.set(8, 3, 8)
    sudoko.set(9, 3, 3)

    sudoko.set(3, 4, 9)
    sudoko.set(2, 6, 5)

    sudoko.set(4, 5, 7)
    sudoko.set(6, 5, 4)

    sudoko.set(7, 4, 1)
    sudoko.set(9, 6, 4)

    sudoko.set(1, 7, 9)
    sudoko.set(2, 7, 8)
    sudoko.set(1, 8, 2)

    sudoko.set(5, 8, 5)
    sudoko.set(6, 8, 1)

    sudoko.set(7, 9, 8)
    sudoko.set(8, 9, 7)
    sudoko.set(9, 9, 1)
    sudoko.output()


if __name__ == '__main__':
    main()
