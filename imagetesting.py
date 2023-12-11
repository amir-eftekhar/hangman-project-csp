import turtle as t

import images as im
import images.image_resize as imr
resize_image = imr.resize_image

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
stand = t.Turtle()
santa = t.Turtle()
stand.speed(0)
stand.penup()
santa.speed(0)
santa.penup()
def set_up_visuals():
    
    
    stand.goto(-75, 75)
    stand.shape(hangman_stand)
    
    
    santa.goto(31, 75)
    santa.shape(santa_head)
    welcome_t = t.Turtle()
    welcome_t.speed(0)
    welcome_t.penup()
    welcome_t.goto(-50, 370)
    welcome_t.shape(welcome)
set_up_visuals()

santa_images = [santa_head, santa_hat, santa_body, santa_right_arm, santa_both_arms, santa_full]
santa_num = 0
def change_santa_image():
    global santa_num
    print("changing santa image")
    san_image_num = santa_num%len(santa_images)
    santa.shape(santa_images[san_image_num])
    santa_num += 1
wn.onkeypress(change_santa_image, "a")
wn.listen()
wn.mainloop()