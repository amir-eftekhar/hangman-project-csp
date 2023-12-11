import turtle as t
import random
# Theme  == chrismas

writer = t.Turtle()
writer.speed(0)
writer.penup()
writer.hideturtle()
writer.goto(-260, -300)
wn = t.Screen()
Christmas_words = [
    "Snowflake", "Reindeer", "Mistletoe", "Sleigh", "Santa", "Elf", "Gingerbread", "Ornament", 
    "Stocking", "Chimney", "Presents", "Wreath", "Candy cane", "Christmas tree", "Snowman", 
    "Icicle", "Frost", "Cookies", "Eggnog", "Tinsel", "Yule log", "Fairy lights", "Hot chocolate", 
    "Jingle bells", "Garland", "Winter", "Festival", "Celebration", "Gifts", "Carols", 
    "December", "Fireplace", "Snowball", "Holiday", "Pinecone", "Star", "Ribbon", "Sled", 
    "North Pole", "Frosty", "Mittens", "Scarf", "Sweater", "Cider", "Feast", "Family", 
    "Friends", "Joy", "Peppermint", "Toys", "Workshop", "Nutcracker", "Snow globe", "Holly", 
    "Jolly", "Bell", "Bow", "Candle", "Card", "Chestnuts", "Chill", "Chocolate", "Cold", 
    "Comet", "Cozy", "Cracker", "Dasher", "Decorations", "Delight", "Dinner", "Donner", 
    "Elves", "Fairy tale", "Festive", "Figgy pudding", "Fir", "Frosting", "Fruitcake", 
    "Gala", "Gathering", "Ginger", "Glee", "Glitter", "Glow", "Gold", "Green", "Greetings", 
    "Grinch", "Happiness", "Harmony", "Hat", "Hearth", "Igloo", "Ivy", "Jack Frost", "Joyful", 
    "Krampus", "Lights", "Love", "Magic", "Merry", "Mince pies", "Mittens", "Muffler", "Music", 
    "Nativity", "Naughty", "Nice", "Nutmeg", "Ornate", "Package", "Pageant", "Parade", "Party", 
    "Penguin", "Pie", "Pine", "Plum pudding", "Poinsettia", "Polar", "Pomander", "Prancer", 
    "Pudding", "Red", "Rejoice", "Relax", "Ribbon", "Rudolph", "Santa's hat", "Scarf", "Season", 
    "Shiver", "Silver", "Skates", "Skiing", "Sleigh bells", "Sleigh ride", "Snow boots", "Snowfall", 
    "Snowsuit", "Sparkle", "Spirit", "Stockings", "Sugarplum", "Surprise", "Sweater", "Sweet", 
    "Toboggan", "Tradition", "Train", "Tree", "Twinkle", "Vacation", "Vixen", "Warmth", "White", 
    "Winter solstice", "Wish", "Wonder", "Wonderland", "Wrap", "Wreath", "Yuletide", "Zest", 
    "Angel", "Bauble", "Blizzard", "Blitzen", "Boxing Day", "Brandy", "Cabin", "Candy", 
    "Caroling", "Celebration", "Cherish", "Chill", "Chocolate", "Cinnamon", "Coal", "Comfort", 
    "Cranberry", "Cuddle", "Cupcake", "Dance", "Decoration", "Delight", "Dessert", "Dove", 
    "Dream", "Drum", "Eggnog", "Embrace", "Eve", "Evergreen", "Excitement", "Family", "Festivity", 
    "Firework", "Flake", "Fleece", "Flicker", "Flurry", "Frostbite", "Fruitcake", "Fun", "Garland", 
    "Gift wrap", "Gingerbread man", "Glee", "Glisten", "Glitter", "Gloves", "Goodwill", "Goose", 
    "Greetings", "Happy", "Hearth", "Holiday", "Hug", "Icicle", "Illumination", "Jingle", "Joy", 
    "Kringle", "Laugh", "Laurel", "Lights", "Log", "Love", "Magic", "Merry", "Mince"]
christmas_words = [i.lower() for i in Christmas_words]
space_l = ["asdads asdasd asdad ", "asd asd asd ", "d d d" ]
print(len(christmas_words))

def generate_words_o(len_list, list):
    sutible_l = []
    lenn = random.choice(len_list)
    for i in list:
        if len(i)== lenn:
            sutible_l.append(i)
    if len(sutible_l) > 0:
        return random.choice(sutible_l)
    else:
        print("sorry no words in this list had that many chatacters")
        
def generate_word_r(list):
    return random.choice(list)
letter_ts = {}
turtles = []
vailid_letters = "abcdefghijklmnopqrstuvwxyz"
def draw_word(word):
    #word = generate_word_r(christmas_words)
    for i in range(len(word)): 
        if word[i] in vailid_letters:
            writer.write("_", font=("Arial", 50, "normal"))
            letter_ts[f"letter_t{i}"] = "char"
            writer.forward(50)
        else:
            letter_ts[f"letter_t{i}"] = "space"
            writer.forward(50)
    for index, key in enumerate(letter_ts):
        turt = t.Turtle()
        turtles.append(turt)
        turt.penup()
        turt.hideturtle()
        if letter_ts[key] == "char":
            
            turt.speed(0)
            turt.goto(-257 + (index * 50), -290)
            turt.write("*", font=("Arial", 50, "normal"))
    print(turtles)

def write_full_word(word):
    for i in range(len(word)):
        turtles[i].clear()
        turtles[i].write(word[i], font=("Arial", 50, "normal"))
def checkword(word, char):
    ll = []
    for i in word:
        if i ==char:
            ll.append(i)
    return ll
def get_correct_count(word, char):
    num = 0
    for i in word:
        if i ==char:
            num+=1
    return num       

        