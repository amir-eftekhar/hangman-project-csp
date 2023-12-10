import turtle as t
import images as im
import hangmanfunc as hf
import wordfunctions as wf
import tkinter as tk
from tkinter import simpledialog, messagebox

checkword = wf.checkword
writer  = wf.writer
draw_word = wf.draw_word
words = wf.christmas_words
start = hf.start_gameV2
guessed_letters = hf.guessed_letters
wn = t.Screen()

start("tkinter")
wn.mainloop()