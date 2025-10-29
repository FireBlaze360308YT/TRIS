class Board:
    def __init__(self, sign_1: str, sign_2: str) -> None:
        self.board: list[list[str]] = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
        self.sign_1: str = sign_1
        self.sign_2: str = sign_2
        self.tiles: dict[str, tuple[int, int]] = {str(i + 1): divmod(i, 3) for i in range(9)}
        self.free_tiles: set[tuple[int, int]] = set(self.tiles.values())
        self.number_of_free_tiles: int = len(self.free_tiles)

    def __str__(self) -> str:
        horizontal_line = "+-------------+-------------+-------------+"
        empty_row = "|             |             |             |"
        lines = [horizontal_line]

        for row in self.board:
            lines.append(empty_row)
            lines.append("|" + "|".join(f"      {cell}      " for cell in row) + "|")
            lines.append(empty_row)
            lines.append(horizontal_line)

        return "\n".join(lines)

    def make_move(self, sign: str, x: int, y: int) -> None:
        #TODO to fix color add it ad beginning.
        #Colors f"\033[32m{sign}\033[0m" if sign == self.sign_2 else f"\033[31m{sign}\033[0m"
        self.board[x][y] = sign
        self.number_of_free_tiles -= 1
        self.free_tiles.remove((x, y))

    def is_free(self, x: int, y: int) -> bool:
        return (x, y) in self.free_tiles

    def reset(self):
        self.__init__(sign_1=self.sign_1, sign_2=self.sign_2)

    def get_sign(self, player: str) -> str:
        if player == "Computer":
            return self.sign_2
        return self.sign_1

if __name__ == '__main__':
    pass
