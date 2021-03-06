"""
A game launcher for EX-54. Written using Tkinter, this menu will display two drop down lists, difficulty and level.
Level is used to select the background and sprites for the game, while difficulty will mandate the intensity of
missile rounds.
"""
from tkinter import *
import maingame

launcher = Tk()
launcher.configure(bg='#1E0032')
launcher.title('EX-54')

title = Label(launcher, text='EX-54', font=('Helvetica', 32), bg='#1E0032', fg='#ffffff')
title.pack()

sub_title = Label(launcher, text='Stealth Fighter', font=('Helvetica', 24), bg='#1E0032', fg='#ffffff')
sub_title.pack()

variable_levels = StringVar(launcher)
variable_levels.set("Levels") # default value

levels = OptionMenu(launcher, variable_levels, 'mars', 'ocean', 'earth', )
levels.configure(bg='#024A00', borderwidth=0, fg='#ffffff')
levels.pack()

variable_diff = StringVar(launcher)
variable_diff.set("Difficulty") # default value

difficulty = OptionMenu(launcher, variable_diff, 'easy', 'medium', 'hard', 'death')
difficulty.configure(bg='#024A00', borderwidth=0, fg='#ffffff')
difficulty.pack()


start_game_button = Button(launcher, text='Launch Game!', command=lambda: start_game(variable_levels.get(),
                                                                                     variable_diff.get()))
start_game_button.configure(bg='#024A00', borderwidth=5, fg='#ffffff')
start_game_button.pack()

def start_game(selected_level, selected_difficulty):
    """
    Creates a MainGame instance with the selected options.
    :param selected_level: Selected level from the levels OptionMenu
    :param selected_difficulty: Selected difficulty from the difficulty OptionMenu
    :return: None
    """
    maingame.MainGame(selected_level, selected_difficulty)

mainloop()

