import random as rm

class Algorithms:

    @staticmethod
    def function_0(root) -> None:
        #Noob mode
        pass

    @staticmethod
    # Easiest mode, the cpu selects the nearest empty tile
    def function_1(root) -> None:
        #Easy mode
        for y in range(3):
            for x in range(3):
                if root.is_free(x=x, y=y):
                    root.make_move(sign=root.sign_2, x=x, y=y)
                    return None
        return None

    @staticmethod
    # Medium mode, the cpu selects a tile randomly
    def function_2(root) -> None:
        #Random Mode
        x, y = rm.choice(list(root.free_tiles))
        root.make_move(sign=root.sign_2, x=x, y=y)

    #TODO correct hard_mode func
    @staticmethod
    # Pretty hard mode, the cpu plays well but randomly makes a mistake
    def function_3(root, mistake_chance: float = 0.25) -> None:
        #Hard mode
        if rm.random() < mistake_chance:
            return Algorithms.function_2(root=root)

        n: int = len(root.board)

        row_1 = list(root.board[0])
        row_2 = list(root.board[1])
        row_3 = list(root.board[2])
        column_1 = [root.board[i][0] for i in range(n)]
        column_2 = [root.board[i][1] for i in range(n)]
        column_3 = [root.board[i][2] for i in range(n)]
        diagonal_1 = [root.board[i][i] for i in range(n)]
        diagonal_2 = [root.board[i][n - i - 1] for i in range(n)]

        def safe_move(tile_key):
            if tile_key in root.tiles:
                x_1, y_1 = root.tiles[tile_key]
                if root.is_free(x_1, y_1):
                    root.make_move(sign=root.sign_2, x=x_1, y=y_1)
                    return True
            return False

        lines = [
            row_1, row_2, row_3,
            column_1, column_2, column_3,
            diagonal_1, diagonal_2
        ]

        for line in lines:
            if line.count(root.sign_2) == 2 and line.count(root.sign_1) == 0:
                free_tiles = [cell for cell in line if cell not in (root.sign_1, root.sign_2)]
                if free_tiles:
                    if safe_move(free_tiles[0]):
                        return None

        for line in lines:
            if line.count(root.sign_1) == 2 and line.count(root.sign_2) == 0:
                free_tiles = [cell for cell in line if cell not in (root.sign_1, root.sign_2)]
                if free_tiles:
                    if safe_move(free_tiles[0]):
                        return None

        if root.is_free(x=1, y=1):
            root.make_move(sign=root.sign_2, x=1, y=1)
            return None

        for (x, y) in rm.sample([(0, 0), (2, 0), (2, 2), (0, 2)], k=4):
            if root.is_free(x, y):
                root.make_move(sign=root.sign_2, x=x, y=y)
                return None

        if root.free_tiles:
            x, y = rm.choice(list(root.free_tiles))
            root.make_move(sign=root.sign_2, x=x, y=y)
        return None

    @staticmethod
    # The cpu will always make the best move, so the game will either be a win for the cpu or a draw
    def function_4(root) -> None:
        #Impossible Mode
        Algorithms.function_3(root=root, mistake_chance=0.0)
