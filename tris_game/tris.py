from typing import Callable
import time
from utilities import Winning, GameUtilities, UserInteraction
import board_module
from algorithm_module import Algorithms

class GameModes:

    @staticmethod
    def function_0(starter: str, root, selected_mode) -> None:
        #Standard Mode
        if starter == "User":
            GameUtilities.clear_screen()
            print(root)
            UserInteraction.get_user_input(prompt="Enter your choice: ", root=root)
        while True:
            if Winning.win_check_and_handler(root=root):
                break
            GameUtilities.clear_screen()
            selected_mode(root=root)
            if Winning.win_check_and_handler(root=root):
                break
            time.sleep(0.25)
            print(root)
            time.sleep(0.25)
            UserInteraction.get_user_input(prompt="Enter your choice: ", root=root)
            if Winning.win_check_and_handler(root=root):
                break

            GameUtilities.clear_screen()

    @staticmethod
    def function_1(starter: str, root, selected_mode) -> None:
        #Versus mode
        exit(f"\033[31m{"INCOMPLETE FUNCTION"}\033[0m")

    @staticmethod
    def function_2(starter: str, root, selected_mode) -> None:
        #Cpu mode
        exit(f"\033[31m{"INCOMPLETE FUNCTION!"}\033[0m")

#Main function
def main() -> None:
    #Clears screen for nice view
    GameUtilities.clear_screen()

    #TODO add selection of game length!
    #TODO add challenge mode with time, score and name logging!
    #TODO add ability to choose the color of the signs!
    #TODO add advanced customization option.
    #TODO fix color by adding them at the beginning, because using colored characters to modify the board will make then not be recognised anymore!

    #Gets the game mode of the match
    game_mode, starters = UserInteraction.get_game_mode(GameModes)

    #This player will start
    first_in_line = UserInteraction.who_starts(starters=starters)

    GameUtilities.welcome_screen()

    sign_1, sign_2 = UserInteraction.game_signs(players=starters)

    selected_mode: Callable = UserInteraction.get_difficulty(Algorithms)

    GameUtilities.clear_screen()

    root = board_module.Board(sign_1=sign_1, sign_2=sign_2)

    if selected_mode is Algorithms.function_4:
        first_in_line = "Computer"
        print("You have dared to select the secret impossible mode! Prepare to suffer!")
    else:
        #TODO fix selected_mode.__name__
        print(f"The selected mode is {selected_mode.__name__} and the {first_in_line} will start with '{root.get_sign(first_in_line)}'!")

    time.sleep(3)
    GameUtilities.clear_screen()

    game_mode(starter=first_in_line, root=root, selected_mode=selected_mode)

if __name__ == "__main__":
    main()
