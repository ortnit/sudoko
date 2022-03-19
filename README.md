# Readme

How to solve sudoko, brute forcing the numbers with a recursion.

For input, we take a 2 dimensional list with integers, 
representing the fields, while the value 0 represents an empty field.

The `Sudoko::solve()` function will start the solving process, in the end
solved board is stored inside the Sudoko instance and can be displayed using
`Sudoko::show_board()`.

```python
from lib.sudoko import Sudoko

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

sudoko = Sudoko(board)
sudoko.solve()
sudoko.show_board()
```

this will lead to a result like that:
```
245|197|863
678|342|195
931|568|247
-----------
354|926|781
762|851|439
819|473|526
-----------
497|685|312
126|734|958
583|219|674
```
