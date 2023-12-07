import turtle as t
import random
import threading
import images as im
import wordfunctions as wf
draw_words = wf.draw_words 
check_word = wf.checkword
writer  = wf.writer
draw_word = wf.draw_word
words = wf.christmas_words

def start_game(mode, word):
    if mode =="console":
        draw_word(word)
        valid_g = "abcdefghijklmnopqrstuvwxyz "
        guess1 = input("Welcome to hangman Christman edition! please select your first letter:  ")
        if guess1 not in valid_g:
            print("please enter a valid letter")
            while guess1 not in valid_g:
                guess1 = input("Welcome to hangman Christman edition! please select your first letter:  ")
        corrects = check_word(word, guess1)
        