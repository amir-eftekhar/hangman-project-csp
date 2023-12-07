import turtle as t
import random
# Theme  == chrismas

writer = t.Turtle()
writer.speed(0)
writer.penup()
writer.hideturtle()
writer.goto(-250, -300)
wn = t.Screen()
christmas_words = [
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
print(len(christmas_words))

def generate_words_o(len, list):
    sutible_l = []
    for i in list:
        if len(i)== len:
            sutible_l.append(i)
    if sutible_l:
        return random.choice(sutible_l)
    else:
        print("sorry no words in this list had that many chatacters")
        
def generate_word_r(list):
    return random.choice(list)
letter_t = []
def draw_word(word):
    word = generate_word_r(christmas_words)
    letter_ts = []
    for i in range(len(word)):
        writer.write("_", font=("Arial", 50, "normal"))
        writer.forward(50)
        letter_ts.append(f"letter_t{i}")
    for index, turt in enumerate(letter_ts):
        turt = t.Turtle()
        turt.penup()
        turt.hideturtle()
        turt.speed(0)
        turt.penup()
        turt.hideturtle()
        turt.goto(-245 + (index * 50), -290)
        turt.write("*", font=("Arial", 50, "normal"))

def checkword(word, char):
    ll = []
    for i in word:
        if i ==char:
            ll.append(i)
    return ll
def start_game(mode, word):
    if mode =="console":
        draw_word(word)
        welcome = input("Welcome to hangman Christman edition! please slect your first letter:  ")
        