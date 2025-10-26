class Board:
    def __init__(self, user_sign: str, computer_sign: str) -> None:
        self.board: list[list[str]] = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
        self.free_tiles: set[tuple[int, int]] = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        self.number_of_free_tiles: int = len(self.free_tiles)
        self.user_sign: str = user_sign
        self.computer_sign: str = computer_sign
        self.tiles: dict[str, tuple[int, int]] = {str(i + 1): divmod(i, 3) for i in range(9)}

    # Prints the formatted board
    def print_board(self) -> None:
        horizontal_line = "+-------------+-------------+-------------+"
        empty_row = "|             |             |             |"

        print(horizontal_line)
        for row in self.board:
            print(empty_row)
            print("|" + "|".join(f"      {cell}      " for cell in row) + "|")
            print(empty_row)
            print(horizontal_line)

    def make_move(self, sign: str, x: int, y: int) -> None:
        self.board[x][y] = sign
        self.number_of_free_tiles -= 1
        self.free_tiles.remove((x, y))

    def is_free(self, x: int, y: int) -> bool:
        return (x, y) in self.free_tiles

if __name__ == '__main__':
    pass
