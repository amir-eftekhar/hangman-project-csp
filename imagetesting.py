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
resize_image(santa_head, 195, 220, "320")
resize_image(santa_body, 195, 270, "180")
resize_image(santa_right_arm, 220,280, "180")
resize_image(santa_both_arms, 255, 280, "180")
resize_image(santa_full, 255, 330, "180")
santa_full = "images/fullsanta_180.gif"
santa_both_arms = "images/bothlegsanta_180.gif"
santa_right_arm = "images/right-arm_180.gif"

santa_body = "images/santa_bod_180.gif"
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
    santa.shape(santa_hat)
    welcome_t = t.Turtle()
    welcome_t.speed(0)
    welcome_t.penup()
    welcome_t.goto(-50, 370)
    welcome_t.shape(welcome)
set_up_visuals()

santa_images = [santa_hat,santa_head, santa_body, santa_right_arm, santa_both_arms, santa_full]
santa_addjustments = [[0,0], [0, -45], [0, -65], [8, -70],[-5,-70 ], [-7, -91] ]
santa_num = 0
def change_santa_image():
    global santa_addjustments
    global santa_num
    santa.speed(0)
    santa.setheading(270)
    santa.goto((31+santa_addjustments[santa_num%len(santa_addjustments)][0]), (75+santa_addjustments[santa_num%len(santa_addjustments)][1]))
    print("changing santa image")
    san_image_num = santa_num%len(santa_images)
    santa.shape(santa_images[san_image_num])
    santa_num += 1
wn.onkeypress(change_santa_image, "a")
wn.listen()
wn.mainloop()