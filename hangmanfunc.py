import turtle as t
import random
import threading
import images as im
import wordfunctions as wf
import images.image_resize as imr
import tkinter as tk
from tkinter import simpledialog, messagebox

resize_image = imr.resize_image
draw_words = wf.draw_word
check_word = wf.checkword
writer  = wf.writer
draw_word = wf.draw_word
christmas_words = wf.christmas_words
letter_ts = wf.letter_ts
vailid_letters = wf.vailid_letters
get_correct = wf.get_correct_count
generate_word_o = wf.generate_words_o
turtles = wf.turtles
write_full = wf.write_full_word
wn = t.Screen()

hangman_stand = "images/hangmanStand.gif"
santa_hat = "images/santahat.gif"
santa_head = "images/santahead.gif"
santa_body = "images/santa_bod.gif"
santa_right_arm = "images/right-arm.gif"
santa_both_arms = "images/bothlegsanta.gif"
santa_full = "images/fullsanta.gif"
welcome = "images/welcome-to.gif"
resize_image(santa_hat, 220, 130, "130")
resize_image(santa_head, 220, 220, "320")
santa_head = "images/santahead_320.gif"
santa_hat = "images/santahat_130.gif"
wn.register_shape(welcome)
wn.register_shape(hangman_stand)
wn.register_shape(santa_hat)
wn.register_shape(santa_head)
wn.register_shape(santa_body)
wn.register_shape(santa_right_arm)
wn.register_shape(santa_both_arms)
wn.register_shape(santa_full)
def add_corrects(letter, word):
    print("adding corrects")
    for index, i in enumerate(word):
        if letter == i:
            print(turtles[index])
            turtles[index].clear()
            turtles[index].write(letter, font=("Arial", 50, "normal"))

def start_game(mode, word):
    if mode =="console":
        draw_word(word)
        valid_g = "abcdefghijklmnopqrstuvwxyz "
        guess1 = input("Welcome to hangman Christman edition! please select your first letter:  ")
        if guess1 not in valid_g:
            print("please enter a valid letter")
            while guess1 not in valid_g:
                guess1 = input("Welcome to hangman Christman edition! please select your first letter:  ")
                
        correct = add_corrects(guess1, word)
        if not correct:
            print("sorry your letter was not in the word")
        num_guesses = len(word)
        guessed = 0
        while guessed < num_guesses:
            guess = input("enter your next letter guess")
def console_word(word):
    console_word = ""
    for i in word:
            if i in vailid_letters:
                console_word += "_"
            elif i == " ":
                console_word += " "
            else:
                console_word += i
    return console_word
'''def change_console_word(word, char):
    cons_w = ''
    for i in word:
        if i == char:
            cons_w += char
        elif i in vailid_letters:
            cons_w += "_"
        elif i == " ":
            cons_w += " "
    return cons_w'''
def add_corrects_to_word(letter, word):
    for i in range(len(word)):
        if letter == word[i]:
            word[i] = letter
def set_up_visuals():
    stand = t.Turtle()
    stand.speed(0)
    stand.penup()
    stand.goto(-75, 75)
    stand.shape(hangman_stand)
    santa = t.Turtle()
    santa.speed(0)
    #santa.hideturtle()
    santa.penup()
    santa.goto(31, 75)
    santa.shape(santa_head)
    welcome_t = t.Turtle()
    welcome_t.speed(0)
    welcome_t.penup()
    welcome_t.goto(-50, 370)
    welcome_t.shape(welcome)
vailid_diff = ['easy', 'medium', 'hard', 'extreme']
guessed_letters = 0
vailid_num_players = ['1', '2']
def start_gameV2(mode):
    wn.clear()
    set_up_visuals()
    
    if mode =="console":
        players = input("do you want to play 2 players or 1 player enter 1/2:  ")
        if players not in vailid_num_players:
            print("please enter a valid option")
            while players not in vailid_num_players:
                players = input("do you want to play 2 players or 1 player enter 1/2:  ")
        
        global vailid_letters
        guesses = 0
        if players == "1":
            difficulty = input("please select your difficulty easy, medium, hard, or extreme:  ")
            if difficulty not in vailid_diff:
                print("please enter a valid difficulty")
                while difficulty not in vailid_diff:
                    difficulty = input("please select your difficulty easy, medium, hard, or extreme:  ")
            if difficulty == "easy":
                len_list = [3, 4]
            elif difficulty == "medium":
                len_list = [5, 6]
            elif difficulty == "hard":
                len_list = [7, 8]
            elif difficulty == "extreme":
                len_list = [9, 10]
        guessed_letters = 0 
        if players == "1":
            word = generate_word_o(len_list, christmas_words)
        elif players == "2":  
            word = input("player 1 please enter the word:  ")
        draw_word(word)
        guess1= input(f"Welcome to hangman Christman edition! please select your first letter for the word:  ")
        if guess1 not in vailid_letters:
            print("please enter a valid letter ")
            while guess1 not in vailid_letters:
                guess1 = input("Welcome to hangman Christman edition! please select your first letter:  ")
        correct = get_correct(word, guess1)
        vailid_letters = vailid_letters.replace(guess1, '')
        if correct ==0:
            print("sorry your letter was not in the word")
            guesses +=1
            
        else:
            print(f"your letter was in the word {correct} times")
            guessed_letters += correct
            guesses +=1
            add_corrects(guess1, word)
        word_minus_spaces = word.replace(" ", "")
            
        while guesses <= 8:
            print(guessed_letters)
            print(len(word))
            if guessed_letters == len(word_minus_spaces):
                print("Win! you guessed the word!")
                write_full(word)
                break
            guess = input("enter your next letter guess for the word :  ").lower()
            if guess not in vailid_letters:
                print("please enter a valid letter that you have not chose yet ")
                while guess not in vailid_letters:
                    guess = input(f"enter your next letter guess for the word :  ")
            correct = get_correct(word, guess)
            if correct ==0:
                print("sorry your letter was not in the word")
                guesses +=1
            
            else:
                print(f"your letter was in the word {correct} times")
                guesses +=1
                add_corrects(guess, word)
                guessed_letters += correct
                #Console_word = change_console_word(word, guess)
            if guessed_letters == len(word_minus_spaces):
                print("Win! you guessed the word!")
                write_full(word)
                break
        
        if guessed_letters < len(word_minus_spaces):
            print(f"you lost! the word was {word}")   
            write_full(word)
    elif mode == "tkinter":
        def play_game_tkinter():
            global word, guessed_letters, guesses
            word_minus_spaces = word.replace(" ", "")
            if guesses > 8 or guessed_letters >= len(word_minus_spaces):
                end_game_tkinter()
                return

            guess = simpledialog.askstring("Guess", "Enter your next letter guess for the word:")
            guess = guess.lower() if guess else ''
            while guess not in vailid_letters:
                guess = simpledialog.askstring("Guess", "Please enter a valid letter that you have not chosen yet:")
                guess = guess.lower() if guess else ''

            correct = get_correct(word, guess)
            if correct == 0:
                messagebox.showinfo("Result", "Sorry, your letter was not in the word")
                guesses += 1
            else:
                guessed_letters += correct
                messagebox.showinfo("Result", f"Your letter was in the word {correct} times")
                guesses += 1
                add_corrects(guess, word)

            play_game_tkinter()

        def end_game_tkinter():
            global word, guessed_letters
            word_minus_spaces = word.replace(" ", "")
            if guessed_letters >= len(word_minus_spaces):
                messagebox.showinfo("Game Over", "Win! You guessed the word!")
            else:
                messagebox.showinfo("Game Over", f"You lost! The word was {word}")
            write_full(word)

        def start_game_tkinter():
            global word, guessed_letters, guesses
            wn.clear()
            set_up_visuals()

            players = simpledialog.askstring("Players", "Do you want to play 2 players or 1 player? Enter 1/2:")
            while players not in vailid_num_players:
                players = simpledialog.askstring("Players", "Please enter a valid option (1 or 2):")

            guesses = 0
            guessed_letters = 0
            if players == "1":
                difficulty = simpledialog.askstring("Difficulty", "Please select your difficulty (easy, medium, hard, extreme):")
                while difficulty not in vailid_diff:
                    difficulty = simpledialog.askstring("Difficulty", "Please enter a valid difficulty (easy, medium, hard, extreme):")
                len_list = {
                    "easy": [3, 4],
                    "medium": [5, 6],
                    "hard": [7, 8],
                    "extreme": [9, 10]
                }[difficulty]
                word = generate_word_o(len_list, christmas_words)
            elif players == "2":
                word = simpledialog.askstring("Word Input", "Player 1, please enter the word:")

            draw_word(word)
            play_game_tkinter()

        # Tkinter setup
        root = tk.Tk()
        root.withdraw()  # Hides the main window

        # Start the Tkinter version of the game
        start_game_tkinter()   