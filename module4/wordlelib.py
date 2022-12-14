# This file is provied by Vrije Universiteit Amsterdam

import textwrap
import tkinter as _tk
import tkinter.font

from abc import ABC, abstractmethod

import queue as _Queue
import time as _time
import random as _random
import os as _os

WORD_LENGTH = 5
MAX_GUESSES = 6

UNCHECKED = -1
WRONG = 0
WRONG_POSITION = 1
CORRECT = 2


class _IPyException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


def _verify_input(value_var, string_var, minimum=None, maximum=None):
    if minimum is None:
        minimum = float('-inf')
    if maximum is None:
        maximum = float('inf')
    if value_var >= minimum:
        if value_var <= maximum:
            return
    value = "%s is out of bounds, expected range: %s to %s, got: %s" % (string_var, minimum, maximum, value_var)
    raise _IPyException(value)


def _verify_int(value_var, string_var, minimum=None, maximum=None):
    if not isinstance(value_var, int):
        value = "%s not an int for %s, got %s" % (value_var, string_var, str(type(value_var))[1:-1])
        raise _IPyException(value)
    _verify_input(value_var, string_var, minimum, maximum)


def _verify_str(value_var, string_var):
    if not isinstance(value_var, str):
        value = "%s is not a string for %s, got %s" % (value_var, string_var, str(type(value_var))[1:-1])
        raise _IPyException(value)


class _Factory:
    def __init__(self):
        self.mainroot = _tk.Tk()
        self.mainroot.withdraw()
        self.mainroot.update()


_ui_factory = _Factory()


class WordleInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_random_word(self):
        """Gets a random five letter word"""
        pass

    @abstractmethod
    def get_next_guess(self):
        """Gets the user's next guess"""
        pass

    @abstractmethod
    def set_coloring(self, coloring):
        """Sets the coloring of the current word. The colors can be either UNCHECKED, WRONG, WRONG_POSITION, or
        CORRECT."""
        pass

    @abstractmethod
    def set_game_over(self):
        """Display the game over screen"""
        pass

    @abstractmethod
    def set_win(self):
        """Display the win screen"""
        pass

    @abstractmethod
    def stay_open(self):
        """Force the window to remain open.
        Only has effect on Mac OS to prevent the window from closing after the execution finishes.

        Make sure that this is the last statement you call when including it because the code does NOT continue after this.
        """
        pass


class Frame:
    def __init__(self, word, colors):
        self.word = word
        self.colors = colors


class SpecialFrame:
    def __init__(self, win=False, game_over=False):
        self.win = win
        self.game_over = game_over


class WordleTestInterface(WordleInterface):
    def __init__(self, test_file_name):
        super().__init__()

        self.WORD_LENGTH = 5
        self.MAX_GUESSES = 6

        self.UNCHECKED = -1
        self.WRONG = 0
        self.WRONG_POSITION = 1
        self.CORRECT = 2

        hint, self.secret_word, self.frames = self.read_wordle_game(test_file_name)
        self.error_msg = ""
        if hint != "":
            wrapped_hint = textwrap.fill("Hint: " + hint, width=80)
            self.error_msg += wrapped_hint + "\n\n"

        self.error_msg += "secret:  " + str(self.secret_word) + "\n"
        self.colors = [[self.UNCHECKED for _ in range(self.WORD_LENGTH)] for _ in range(self.MAX_GUESSES)]
        self.row = 0

        self.game_over = False
        self.win = False

        self.test_succeeded = False

    def printerr(self, s, end='\n'):
        self.error_msg += s + end

    def get_random_word(self):
        if self.test_succeeded:
            raise _IPyException("The test has already finished, but your code didn't stop")

        if self.secret_word is None:
            # depending on their implementation, this might or might not work, so give them a different "word" we
            # never test on
            return "you asked for a second secret word, not what we expected"

        secret = self.secret_word
        self.secret_word = None

        return secret

    def get_next_guess(self):
        if self.test_succeeded:
            return None

        if isinstance(self.frames[0], SpecialFrame):
            if(self.frames[0].game_over):
                self.printerr("Want".ljust(len("GameOver")) + " " + "Got".ljust(self.WORD_LENGTH))
                self.printerr("GameOver Asked for next guess")

                raise _IPyException("The game was gameover, but your code didn't stop\n" + self.error_msg)
            if (self.frames[0].win):
                self.printerr("Want".ljust(self.WORD_LENGTH) + " " + "Got".ljust(self.WORD_LENGTH))
                self.printerr("Win Asked for next guess")

                raise _IPyException("The game was won, but your code didn't stop\n" + self.error_msg)


        if not self.frames:
            return None

        guess = self.frames[0].word

        self.printerr(guess)
        self.frames[0].word = None

        return guess




    def set_coloring(self, coloring):
        if self.test_succeeded:
            raise _IPyException("The test has already finished, but your code didn't stop\n" + self.error_msg)

        self.colors[self.row] = coloring
        self.row += 1

        # check frame
        frame = self.frames[0]
        self.printerr("Want".ljust(self.WORD_LENGTH) + " " + "Got".ljust(self.WORD_LENGTH))
        for i in range(MAX_GUESSES):
            self.printerr(self.coloring_to_ascii(frame.colors[i]) + " " + self.coloring_to_ascii(self.colors[i]))

        self.printerr("")

        if frame.colors != self.colors:
            raise _IPyException("Colors didn't match\n" + self.error_msg)

        self.frames = self.frames[1:]

        if not self.frames:
            self.test_succeeded = True

    def set_game_over(self):
        if self.test_succeeded:
            return
            # raise _IPyException("The test has already finished, but your code didn't stop\n" + self.error_msg)

        self.game_over = True

        self.printerr("Want".ljust(self.WORD_LENGTH) + " " + "Got".ljust(self.WORD_LENGTH))

        if not isinstance(self.frames[0], SpecialFrame):
            frame = self.frames[0]
            self.printerr(self.coloring_to_ascii(frame.colors[0]) + " GameOver")
            for i in range(1, MAX_GUESSES):
                self.printerr(self.coloring_to_ascii(frame.colors[i]) + " " + " " * self.WORD_LENGTH)
            raise _IPyException("You set the game over state, but weren't supposed to\n " + self.error_msg)

        elif not self.frames[0].game_over:
            frame = self.frames[0]
            self.printerr("Win".ljust(self.WORD_LENGTH) + " GameOver")
            raise _IPyException("You set the game over state, but aren't supposed to\n " + self.error_msg)

        self.printerr("GameOver".ljust(self.WORD_LENGTH) + " GameOver")
        self.frames = self.frames[1:]

        if not self.frames:
            self.test_succeeded = True

    def set_win(self):
        if self.test_succeeded:
            return
            # raise _IPyException("The test has already finished, but your code didn't stop\n" + self.error_msg)

        self.win = True

        self.printerr("Want".ljust(self.WORD_LENGTH) + " " + "Got".ljust(self.WORD_LENGTH))
        frame = self.frames[0]
        if not isinstance(self.frames[0], SpecialFrame):
            self.printerr(self.coloring_to_ascii(frame.colors[0]) + " Win")
            for i in range(1, MAX_GUESSES):
                self.printerr(self.coloring_to_ascii(frame.colors[i]) + " " + " " * self.WORD_LENGTH)
            raise _IPyException("You set the win state, but aren't supposed to\n" + self.error_msg)

        if not self.frames[0].win:
            self.printerr("GameOver".ljust(self.WORD_LENGTH) + " Win")
            raise _IPyException("You set the win state, but aren't supposed to\n" + self.error_msg)

        self.frames = self.frames[1:]

        if not self.frames:
            self.test_succeeded = True

    def stay_open(self):
        pass

    def read_wordle_game(self, test_file_name):
        with open(test_file_name) as file:
            hint = file.readline().strip()
            secret_word = file.readline().strip()

            frames = []

            can_read = True

            while can_read:
                frames.append(self.read_wordle_frame(file))

                if file.readline() == "end test":
                    can_read = False

            return hint, secret_word, frames

    def read_wordle_frame(self, file):
        word = file.readline().strip()

        if word == "*win":
            return SpecialFrame(win=True)
        elif word == "*gameover":
            return SpecialFrame(game_over=True)

        file.readline()  # delimiter

        colors = []

        for _ in range(self.MAX_GUESSES):
            color = file.readline().strip()

            colors.append([self.ascii_to_color(c) for c in color])

        return Frame(word, colors)

    def coloring_to_ascii(self,coloring):
        res = ""
        for i in coloring:
            if i == self.WRONG :
                res += "x"
            elif i == self.WRONG_POSITION:
                res += "c"
            elif i == self.CORRECT:
                res += "o"
            elif i == self.UNCHECKED :
                res += "."
            else :
                res += "?"
        return res

    def ascii_to_color(self, character):
        if character == '.':
            return self.UNCHECKED
        elif character == 'x':
            return self.WRONG
        elif character == 'c':
            return self.WRONG_POSITION
        elif character == 'o':
            return self.CORRECT
        else:
            raise _IPyException("Invalid test file, cannot parse %s" % character)

    def color_to_string(self, color):
        if color == self.UNCHECKED:
            "no color"
        elif color == self.WRONG:
            "gray"
        elif color == self.WRONG_POSITION:
            "yellow"
        elif color == self.CORRECT:
            "green"
        else:
            raise _IPyException("Invalid color, cannot parse %d" % color)


class Event(object):
    def __init__(self, name, data):
        """This class holds the name and data for each event in their respective variables.
		Variables:
		- name
		- data

		Example to access with WordleUserInterface:

		ui = WordleUserInterface()
		your_variable = ui.get_event() # code will block untill an event comes
		# your_variable now points to an event
		print your_variable.name, your_variable.data

		List of events:
		- name: letter
		  data: the letter that got pressed
			  generated when the user presses on a letter (a to z; will always be lowercase)
		"""
        self.name = name
        self.data = data

    def __str__(self):
        return self.name + " : " + self.data

    def __repr__(self):
        return self.name + " : " + self.data


class WordleUserInterface(WordleInterface):
    def __init__(self, scale):
        super().__init__()

        self.WORD_LENGTH = 5
        self.MAX_GUESSES = 6

        self.UNCHECKED = -1
        self.WRONG = 0
        self.WRONG_POSITION = 1
        self.CORRECT = 2

        self.guesses = _Queue.Queue(maxsize=0)

        self.words = ["" for _ in range(self.MAX_GUESSES)]
        self.colors = [[self.UNCHECKED for _ in range(self.WORD_LENGTH)] for _ in range(self.MAX_GUESSES)]

        self.row = 0

        self.game_over = False
        self.win = False

        # ui
        global _ui_factory
        self.root = _tk.Toplevel(_ui_factory.mainroot)
        self.root.title("WordleUserInterface")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.bind("<Escape>", self.close)
        self.root.resizable(False, False)

        # calculate sizes
        self.scale = scale

        self.text_height = int(100 * self.scale)

        # create main frame
        self.frame = _tk.Frame(self.root, width=250 * self.scale,
                               height=250 * self.scale + self.text_height)
        self.frame.pack_propagate(0)
        self.frame.pack()

        self.canvas_width = 250 * self.scale
        self.canvas_height = 250 * self.scale
        # create and fill the canvas --> paintable area
        self.c = _tk.Canvas(self.frame, width=self.canvas_width,
                            height=self.canvas_height, bg="black", bd=0, highlightthickness=0)
        self.c.pack()

        # create the textholder
        self.scrollbar = _tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=_tk.RIGHT, fill=_tk.Y)
        self.textarea = _tk.Text(self.frame, yscrollcommand=self.scrollbar.set)
        self.textarea.pack(side=_tk.LEFT, fill=_tk.BOTH)
        self.scrollbar.config(command=self.textarea.yview)
        self.textarea.config(state=_tk.DISABLED)

        self.interval = 100  # 0.1 seconds
        self.alarm_speed = 0

        self.font = _tk.font.Font(family='TkDefaultFont', size=int(16 * self.scale), weight='bold')

        self.bind_events()

        _ui_factory.mainroot.update()

    def get_random_word(self):
        words = [
            "acute", "agent", "alias", "angle", "aside", "basic", "bench", "blend", "bowed", "brink",
            "camel", "canal", "catch", "cedar", "chant", "cheer", "chill", "cloak", "close", "cocoa",
            "cough", "cream", "crisp", "drift", "earth", "event", "fined", "flung", "found", "fresh",
            "fried", "frown", "given", "grass", "groom", "grown", "hindi", "house", "humor", "hurry",
            "idiom", "imply", "index", "joked", "light", "lodge", "medal", "minor", "mummy", "nurse",
            "owner", "peace", "pearl", "piece", "pinky", "plain", "prank", "price", "query", "quest",
            "quick", "quill", "ridge", "ripen", "rural", "saint", "sauce", "scary", "sense", "shook",
            "sized", "skirt", "sleep", "slimy", "smash", "smell", "smith", "speed", "spied", "sport",
            "stale", "stalk", "steel", "still", "sting", "stink", "stole", "study", "sweep", "swing",
            "table", "taunt", "tense", "threw", "title", "trace", "tried", "trunk", "viola", "water"
        ]

        return words[_random.randrange(len(words))]

    def set_coloring(self, coloring):
        _verify_int(len(coloring), "len(coloring)", minimum=5, maximum=5)

        for index in coloring:
            _verify_int(coloring[index], "coloring[index]", minimum=-1, maximum=2)

        self.colors[self.row] = coloring
        self.row += 1
        self.show()

    def set_game_over(self):
        if self.win:
            raise _IPyException("Cannot set game over when win is also set")

        self.game_over = True
        self.show()

    def set_win(self):
        if self.game_over:
            raise _IPyException("Cannot set win when game over is also set")

        self.win = True
        self.show()

    def get_next_guess(self):
        # no more guesses if the game has ended
        if self.game_over or self.win or self.row == self.MAX_GUESSES:
            return None

        global _ui_factory
        _ui_factory.mainroot.update()
        while True:
            try:
                guess = self.guesses.get_nowait()
                return guess
            except _Queue.Empty:
                wait_time = min(self.interval, 10)
                self.wait(wait_time)
                _ui_factory.mainroot.update()

    def show(self):
        for row in range(self.MAX_GUESSES):
            for character in range(self.WORD_LENGTH):
                x0 = self.canvas_width / 6 * (character + 1) - 16 * self.scale
                y0 = self.canvas_height / 7 * (row + 1) - 16 * self.scale
                x1 = x0 + 32 * self.scale
                y1 = y0 + 32 * self.scale

                if self.colors[row][character] == self.UNCHECKED:
                    color = 'black'
                elif self.colors[row][character] == self.WRONG:
                    color = 'gray'
                elif self.colors[row][character] == self.WRONG_POSITION:
                    color = '#C0C000'  # actual 'yellow' makes the text unreadable
                elif self.colors[row][character] == self.CORRECT:
                    color = 'green'
                else:
                    raise _IPyException("Invalid color specified %d" % self.colors[row][character])

                self.c.create_rectangle(x0, y0, x1, y1, fill=color)

        for row in range(self.MAX_GUESSES):
            for character in range(len(self.words[row])):
                self.c.create_text(self.canvas_width / 6 * (character + 1),
                                   self.canvas_height / 7 * (row + 1),
                                   fill="white", text=self.words[row][character].upper(), font=self.font)

        if self.game_over:
            self.c.create_rectangle(self.canvas_width / 2 - 64 * self.scale,
                                    self.canvas_height / 2 - 16 * self.scale,
                                    self.canvas_width / 2 + 64 * self.scale,
                                    self.canvas_height / 2 + 16 * self.scale, fill="white")
            self.c.create_text(self.canvas_width / 2, self.canvas_height / 2, fill="red", text="Game over!",
                               font=self.font)
        elif self.win:
            self.c.create_rectangle(self.canvas_width / 2 - 48 * self.scale,
                                    self.canvas_height / 2 - 16 * self.scale,
                                    self.canvas_width / 2 + 48 * self.scale,
                                    self.canvas_height / 2 + 16 * self.scale, fill="white")
            self.c.create_text(self.canvas_width / 2, self.canvas_height / 2, fill="green", text="You win!",
                               font=self.font)

        global _ui_factory
        _ui_factory.mainroot.update()

    def stay_open(self):
        global _ui_factory
        _ui_factory.mainroot.mainloop()

    def close(self, event=None):
        self.root.destroy()
        _os._exit(0)

    def wait(self, ms):
        try:
            _time.sleep(ms * 0.001)
        except:
            self.close()

    def key_event(self, event):
        # don't accept input when the game has ended
        if self.game_over or self.win or self.row == self.MAX_GUESSES:
            return

        if event.char == event.keysym:
            if ord('a') <= ord(event.char) <= ord('z'):
                self.words[self.row] += event.char
                self.words[self.row] = self.words[self.row][:self.WORD_LENGTH]

                self.show()
            elif ord('A') <= ord(event.char) <= ord('Z'):
                self.words[self.row] += event.char.lower()
                self.words[self.row] = self.words[self.row][:self.WORD_LENGTH]

                self.show()
        elif event.keysym == "BackSpace":
            self.words[self.row] = self.words[self.row][:-1]

            self.show()
        elif event.keysym == "Return":
            if len(self.words[self.row]) == self.WORD_LENGTH:
                self.guesses.put(self.words[self.row])

    def bind_events(self):
        self.c.focus_set()
        self.c.bind("<Key>", self.key_event)

