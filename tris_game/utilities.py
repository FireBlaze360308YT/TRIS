import os
import time
import random as rm
from typing import Callable

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

            if is_winner_line(row, root.sign_1) or is_winner_line(col, root.sign_1):
                return "User won!"
            if is_winner_line(row, root.sign_2) or is_winner_line(col, root.sign_2):
                return "Computer won!"

        # Diagonals
        diagram1 = [board[i][i] for i in range(n)]
        diagram2 = [board[i][n - i - 1] for i in range(n)]

        if is_winner_line(diagram1, root.sign_1) or is_winner_line(diagram2, root.sign_1):
            return "User won!"
        if is_winner_line(diagram1, root.sign_2) or is_winner_line(diagram2, root.sign_2):
            return "Computer won!"

        # Draw
        if not root.free_tiles:
            return "Draw!"
        return None

    @staticmethod
    def win_check_and_handler(root) -> bool:
        if not (winner := Winning.check_winner(root)):
            return False

        GameUtilities.clear_screen()
        print(root)
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
        banner: str = "°°°°°°°°°°°°°°°\nWELCOME TO TRIS\n°°°°°°°°°°°°°°°"
        print(banner)
        time.sleep(1)
        GameUtilities.clear_screen()

    @staticmethod
    def score_logging() -> None:
        pass

class UserInteraction:

    @staticmethod
    def get_user_input(prompt: str, root) -> None:
        while True:
            choice = input(prompt).strip()

            if not (position := root.tiles.get(choice)):
                print("Invalid input!")
                continue

            x, y = position
            if root.is_free(x=x, y=y):
                root.make_move(sign=root.sign_1, x=x, y=y)
                return None
            else:
                print("You can't go there!")

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

    @staticmethod
    def game_signs(players: tuple[str, str]) -> tuple[str, str]:
        GameUtilities.clear_screen()
        if input("If u want to choose the signs type 1, any other value to skip.\n>>> ").strip() == "1":
            sign_1: str = input(f"Enter {players[0]}'s sign: ").strip().upper()[0]
            sign_2: str = input(f"Enter {players[1]}'s sign: ").strip().upper()[0]
            while sign_1 == sign_2:
                print("Invalid input!")
                time.sleep(1)
                sign_2: str = input(f"Enter {players[1]}'s sign: ").strip().lower()[0]
            return sign_1, sign_2
        else:
            return "O", "X"

    @staticmethod
    def get_game_mode(game_modes) -> tuple[Callable, tuple[str, str]]:
        """
        The user chooses the game mode
        :param game_modes: Game_modes is the class that contains the different game modes
        :return: the user chosen game_mode corresponding function and the two players that will be competing in the chosen game mode
        """
        while (choice := input("Enter the game mode u want:\n0 for standard mode\n1 for local versus mode\n2 for only cpu mode\n>>> ").strip()) not in {"0", "1", "2"}:
            print("Invalid choice. Please try again.")
            time.sleep(2)
            GameUtilities.clear_screen()
        return getattr(game_modes, f"function_{choice}"), [("User", "Computer"), ("User_1", "User_2"), ("Computer_1", "Computer_2")][int(choice)]

    @staticmethod
    def who_starts(starters: tuple[str, str]) -> str:
        """
        The user either chooses the player that will start the round or makes rm.choice choose
        :param starters: a tuple[str, str] that contains the two players that will be participating in the game
        :return: the function either returns one of the starters at random or by user choice
        """
        if input("Do u want to choose the starting order? Type 1, any other value for random selection!\n>>> ").strip() == "1":
            while (first := input(f"Type the name of the player u want to start {starters}.\n>>> ").strip()) not in starters:
                print("Invalid choice. Please try again.")
                time.sleep(2)
                GameUtilities.clear_screen()
            return first
        return rm.choice(starters)

    @staticmethod
    def get_difficulty(algorithms) -> Callable:
        while (difficulty := input("Enter difficulty (0,1,2,3,4): ").strip()) not in {"0", "1", "2", "3", "4"}:
            print("\nInvalid difficulty")
            time.sleep(1)
            GameUtilities.clear_screen()
        return getattr(algorithms, f"function_{difficulty}")

if __name__ == "__main__":
    pass
