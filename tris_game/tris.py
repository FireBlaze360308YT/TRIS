import typing as tg
import time
from utilities import Winning, GameUtilities, UserInteraction
import board_module
from algorithm_module import Algorithms

#Main function
def main() -> None:
    #TODO add selection of game length
    #TODO add possibility to choose the sign of cpu and player
    #TODO add challenge mode with time, score and name logging

    modes: dict[str, tg.Callable] = {"1":Algorithms.easy_mode, "2":Algorithms.medium_mode, "3":Algorithms.hard_mode, "-1":Algorithms.impossible_mode, "0":Algorithms.noob_mode}
    selected_mode: None = None
    GameUtilities.welcome_screen()

    while True:
        difficulty: str = input("Enter difficulty (1,2,3): ").strip()
        if difficulty not in modes.keys():
            print("\nInvalid difficulty")
            time.sleep(0.5)
            GameUtilities.clear_screen()
            continue
        selected_mode: tg.Callable = modes[difficulty]
        break

    GameUtilities.clear_screen()

    if selected_mode != Algorithms.impossible_mode:
        starter: str = GameUtilities.choose_starter()
        print(f"The selected mode is {selected_mode.__name__} and the {starter} will start with \"X\"!")

        user_sign: str = "X" if starter == "User" else "M"
        computer_sign: str = "X" if starter == "Computer" else "M"

        time.sleep(3)
        GameUtilities.clear_screen()
    else:
        starter: str = "Computer"
        print("U have dared to select the secret impossible mode! Prepare to suffer!")
        user_sign: str = "M"
        computer_sign: str = "X"
        time.sleep(3)
        GameUtilities.clear_screen()

    root = board_module.Board(user_sign=user_sign, computer_sign=computer_sign)

    if starter == "User":
        GameUtilities.clear_screen()
        root.print_board()
        UserInteraction.get_user_input(prompt="Enter your choice: ", root=root)
    while True:
        if Winning.win_check_and_handler(root=root):
            break
        GameUtilities.clear_screen()
        selected_mode(root=root)
        if Winning.win_check_and_handler(root=root):
            break
        time.sleep(0.25)
        root.print_board()
        time.sleep(0.25)
        UserInteraction.get_user_input(prompt="Enter your choice: ", root=root)
        if Winning.win_check_and_handler(root=root):
            break

        GameUtilities.clear_screen()

if __name__ == "__main__":
    main()
