# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# this means to import scripts from different files.

from news_extract import *
from news_nlp import *
from news_scrape import *
import time


print("The Newspaper Scrape Project \nBuilt to give the user access to articles for specific news sources. "
      "\nCan also detect negative or positive language in text.")
print()
name = input("Enter your name to get started!:")

