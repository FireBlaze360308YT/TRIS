import os
import time
import random as rm

class Winning:
    @staticmethod
    def check_winner(root) -> str | None:
        board = root.board
        n = len(board)

        def is_winner_line(line: list[str], sign: str) -> bool:
            return all(cell == sign for cell in line)

        # Rows and columns
        for i in range(n):
            row = board[i]
            col = [board[j][i] for j in range(n)]

            if is_winner_line(row, root.user_sign) or is_winner_line(col, root.user_sign):
                return "User won!"
            if is_winner_line(row, root.computer_sign) or is_winner_line(col, root.computer_sign):
                return "Computer won!"

        # Diagonals
        diagram1 = [board[i][i] for i in range(n)]
        diagram2 = [board[i][n - i - 1] for i in range(n)]

        if is_winner_line(diagram1, root.user_sign) or is_winner_line(diagram2, root.user_sign):
            return "User won!"
        if is_winner_line(diagram1, root.computer_sign) or is_winner_line(diagram2, root.computer_sign):
            return "Computer won!"

        # Draw
        if not root.free_tiles:
            return "Draw!"

        return None

    @staticmethod
    def win_check_and_handler(root) -> bool:
        winner = Winning.check_winner(root)
        if not winner:
            return False

        GameUtilities.clear_screen()
        root.print_board()
        print(f"\n{winner}\n")
        return True

class GameUtilities:
    @staticmethod
    #Function that clears the cmd
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    #Prints the welcome screen
    def welcome_screen() -> None:
        GameUtilities.clear_screen()
        print("°°°°°°°°°°°°°°°")
        print("WELCOME TO TRIS")
        print("°°°°°°°°°°°°°°°")
        time.sleep(1)
        GameUtilities.clear_screen()

    @staticmethod
    # Select the starting player
    def choose_starter() -> str:
        return rm.choice(["User", "Computer"])

class UserInteraction:

    @staticmethod
    #Gets the user input, check for correction and handles problems
    def get_user_input(prompt: str, root) -> None:

        while True:
            choice: str = input(prompt).strip()
            if choice in root.tiles.keys():
                x, y = root.tiles[choice]
                if root.is_free(x=x, y=y):
                    root.make_move(sign=root.user_sign, x=x, y=y)
                    break
                else:
                    print("You can't go there!")
            else:
                print("Invalid input!")

    @staticmethod
    #TODO complete this func
    #Allows to select the length of the game
    def choose_between_finite_and_infinite() -> None:
        """
        super finite = 1 game
        finite = n games + point counter
        infinite = continuous + point counter
        """
        pass

if __name__ == "__main__":
    pass
