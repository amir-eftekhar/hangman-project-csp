import turtle as t
import images as im
import hangmanfunc as hf
import wordfunctions as wf
checkword = wf.checkword
writer  = wf.writer
draw_word = wf.draw_word
words = wf.christmas_words
wn = t.Screen()

word = "  "
draw_word(word)

wn.mainloop()