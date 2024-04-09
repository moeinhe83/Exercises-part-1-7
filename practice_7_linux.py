# Practice_6

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 7', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value Input
name = input('Enter Name ===> ')

# Start Code 
print(name[-1:] + name[1:-1] + name[:1])

# Finish
# Create By Moein Heshmati
