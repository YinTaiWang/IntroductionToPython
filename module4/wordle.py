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
    # done = False
    # while not done:
    #     word = ui.get_next_guess()
    #     # If the next guess is None, the user pressed the X mark or the test ended.
    #     if word is None:
    #         done = True
    #         break
    done = 6
    while done > 0:
        done -= 1
        # print(done)
        word = ui.get_next_guess()
        # If the next guess is None, the user pressed the X mark or the test ended.
        if word is None:
            done = True
            break

        # this means green, yellow, gray , gray , gray.
        # coloring = [ui.CORRECT, ui.WRONG_POSITION, ui.WRONG, ui.WRONG, ui.WRONG]
        # Todo: Use the right colors (use a function for this to not clutter up this function)
        def coloring(secret, word):
            # Assume all characters are gray(incorrect) first
            coloring = [ui.WRONG, ui.WRONG, ui.WRONG, ui.WRONG, ui.WRONG]
            secret_list = string_to_list_of_chars(secret)
            word_list = string_to_list_of_chars(word)
            # print(secret_list)
            # print(word_list)

            # Check for any correct characters and mark them as green
            for i in range(0, len(secret)):
                if word_list[i] == secret_list[i]:
                    coloring[i] = ui.CORRECT
                    # Get rid of these characters so we don't match them again
                    secret_list[i] = 'done'
                    word_list[i] = 'done'
                    # print(secret_list) 
            
            # Check for any characters in the wrong position and mark them as yellow    
            for i in range(0, len(secret)):
                if word_list[i] != secret_list[i]:
                    index = find_index(word_list[i], secret_list)   
                    if index != -1:
                        coloring[i] = ui.WRONG_POSITION
                        secret_list[index] = 'done'
                        word_list[i] = 'done'
                        
            for i in range(0, len(secret)):     
                if word_list[i] != secret_list[i]:  
                    index = find_index(word_list[i], secret_list)        
                    if index == -1:
                        coloring[i] = ui.WRONG

            return coloring
        ui.set_coloring(coloring(secret, word))

        # Todo: Decide when the player has lost or won and let the UI know
        coloring = coloring(secret, word)
        # print(coloring)
        # 0: WRONG, 1: WRONG_POSITION, 2: CORRECT
        if (0 not in coloring) and (1 not in coloring):
            ui.set_win()  
            break
        else:
            continue
    if done == 0:
        if (0 in coloring) or (1 in coloring):
            ui.set_game_over()        

            
        # ui.set_game_over() # <- use this to indicate that the user lost after 6 guesses
        # ui.set_win() # <- use this to indicate that the user won if the guess is correct

    ui.stay_open() # this function call takes until the user closes the window
    # This ensures that the window is not immediately closed after the end of the game


# The code below is only run when running this file,
# it is not run when running the test
if __name__ == "__main__":
    ui = wordlelib.WordleUserInterface(2.0)
    play_wordle(ui)