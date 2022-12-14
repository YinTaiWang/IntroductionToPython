# This file is provided by Vrije Universiteit Amsterdam

import wordlelib

# this variable hold the userinterface
# in case of testing, this is set to
# to a dummy implemenation which repeats
# the input in the test and checks if
# you program behave correctly
#
# This is a global variable, such that you
# can also use it outside of play_wordle function
ui = None


def find_index(elem, list):
    """Gives the index of the first occurrence of elem in list
     or -1 if elem is not in the list"""
    for i in range(len(list)):
        if list[i] == elem:
            return i
    return -1


def string_to_list_of_chars(st):
    return [c for c in st]
    # The above is shorthand for:
    # res = []
    # for c in st :
    #     res.append(c)
    # return res


def play_wordle(init_ui):
    global ui
    ui = init_ui

    secret = ui.get_random_word()
    print(f"Psstt... Secret word is {secret}, do not tell anyone!")
    done = False
    while not done:
        word = ui.get_next_guess()
        # If the next guess is None, the user pressed the X mark or the test ended.
        if word is None:
            done = True
            break
        # this means green, yellow, gray , gray , gray.
        coloring = [ui.CORRECT, ui.WRONG_POSITION, ui.WRONG, ui.WRONG, ui.WRONG]
        # Todo: Use the right colors (use a function for this to not clutter up this function)
        ui.set_coloring(coloring)

        # Todo: Decide when the player has lost or won and let the UI know
        # ui.set_game_over() # <- use this to indicate that the user lost after 6 guesses
        # ui.set_win() # <- use this to indicate that the user won if the guess is correct

    ui.stay_open() # this function call takes until the user closes the window
    # This ensures that the window is not immediately closed after the end of the game


# The code below is only run when running this file,
# it is not run when running the test
if __name__ == "__main__":
    ui = wordlelib.WordleUserInterface(2.0)
    play_wordle(ui)
