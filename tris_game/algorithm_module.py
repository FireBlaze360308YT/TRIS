import random as rm

class Algorithms:

    @staticmethod
    def noob_mode(root) -> None:
        pass

    @staticmethod
    # Easiest mode, the cpu selects the nearest empty tile
    def easy_mode(root) -> None:
        x, y = 0, 0
        while True:
            if root.is_free(x=x, y=y):
                root.make_move(sign=root.computer_sign, x=x, y=y)
                break
            x += 1
            if x > 2:
                x = 0
                y += 1

    @staticmethod
    # Medium mode, the cpu selects a tile randomly
    def medium_mode(root) -> None:
        while True:
            x = rm.randint(0, 2)
            y = rm.randint(0, 2)
            if root.is_free(x=x, y=y):
                root.make_move(sign=root.computer_sign, x=x, y=y)
                break

    #TODO correct hard_mode func
    @staticmethod
    # Pretty hard mode, the cpu plays well but randomly makes a mistake
    def hard_mode(root, mistake_chance: float = 0.25) -> None:
        if rm.random() < mistake_chance:
            Algorithms.medium_mode(root=root)
            return None

        row_1 = list(root.board[0])
        row_2 = list(root.board[1])
        row_3 = list(root.board[2])
        column_1 = [root.board[i][0] for i in range(len(root.board))]
        column_2 = [root.board[i][1] for i in range(len(root.board))]
        column_3 = [root.board[i][2] for i in range(len(root.board))]
        diagonal_1 = [root.board[i][i] for i in range(len(root.board))]
        diagonal_2 = [root.board[i][len(root.board) - i - 1] for i in range(len(root.board))]

        def safe_move(tile_key):
            if tile_key in root.tiles:
                x_1, y_1 = root.tiles[tile_key]
                if root.is_free(x_1, y_1):
                    root.make_move(sign=root.computer_sign, x=x_1, y=y_1)
                    return True
            return False

        lines = [
            row_1, row_2, row_3,
            column_1, column_2, column_3,
            diagonal_1, diagonal_2
        ]

        for line in lines:
            if line.count(root.computer_sign) == 2 and line.count(root.user_sign) == 0:
                free_tiles = [cell for cell in line if cell not in (root.user_sign, root.computer_sign)]
                if free_tiles:
                    if safe_move(free_tiles[0]):
                        return None

        for line in lines:
            if line.count(root.user_sign) == 2 and line.count(root.computer_sign) == 0:
                free_tiles = [cell for cell in line if cell not in (root.user_sign, root.computer_sign)]
                if free_tiles:
                    if safe_move(free_tiles[0]):
                        return None

        if root.is_free(x=1, y=1):
            root.make_move(sign=root.computer_sign, x=1, y=1)
            return None

        for (x, y) in rm.sample([(0, 0), (2, 0), (2, 2), (0, 2)], k=4):
            if root.is_free(x, y):
                root.make_move(sign=root.computer_sign, x=x, y=y)
                return None

        if root.free_tiles:
            x, y = rm.choice(list(root.free_tiles))
            root.make_move(sign=root.computer_sign, x=x, y=y)
        return None

    @staticmethod
    # The cpu will always make the best move, so the game will either be a win for the cpu or a draw
    def impossible_mode(root) -> None:
        mistake_chance: float = 0.0
        Algorithms.hard_mode(root=root, mistake_chance=mistake_chance)
