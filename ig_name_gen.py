import random
import tkinter as tk
BG = "#0b032d"        # deep purple / night sky
CARD = "#120458"      # arcade cabinet purple
ACCENT = "#f72585"    # neon pink
ACCENT2 = "#4cc9f0"   # cyan blue
TEXT = "#f1faee"      # soft white
BTN = "#7209b7"       # purple button
BTN_ACTIVE = "#560bad"
LIST_BG = "#03071e"   # CRT screen black
LIST_FG = "#4cc9f0"   # neon cyan text

an = [
    "dog", "cat", "cow", "goat", "sheep", "horse", "donkey", "pig", "rabbit", "rat",
    "mouse", "lion", "tiger", "elephant", "deer", "monkey", "bear", "fox", "wolf", "camel",
    "zebra", "giraffe", "buffalo", "ox", "yak", "leopard", "cheetah", "panther", "hippo", "rhino",
    "kangaroo", "koala", "panda", "squirrel", "bat", "otter", "beaver", "mole", "hedgehog", "sloth",
    "dogfish", "shark", "whale", "dolphin", "seal", "octopus", "squid", "crab", "lobster", "shrimp",
    "fish", "eel", "frog", "toad", "snake", "lizard", "crocodile", "alligator", "turtle", "tortoise",
    "chicken", "hen", "rooster", "duck", "goose", "turkey", "pigeon", "sparrow", "crow", "eagle",
    "parrot", "peacock", "owl", "hawk", "vulture", "penguin", "swan", "flamingo", "butterfly",
    "bee", "ant", "fly", "mosquito", "spider", "snail", "worm", "beetle", "grasshopper", "ladybug"
]
po = [
    "good", "nice", "kind", "happy", "calm", "brave", "smart", "sweet", "clean", "friendly",
    "fun", "cool", "warm", "soft", "bright", "fair", "true", "safe", "fresh", "quiet",
    "gentle", "helpful", "honest", "polite", "lovely", "cheerful", "strong", "quick", "lucky", "neat",
    "simple", "eachsy", "active", "free", "clear", "pure", "peaceful", "playful", "young", "cute",
    "beautiful", "pretty", "fit", "kindly", "merry", "glad", "ready", "wise", "open", "giving",
    "patient", "humble", "bright", "nice", "safe", "fair", "loyal", "proud", "smiling", "trusty",
    "useful", "warmhearted", "welcome", "hopeful", "stronghearted", "lively", "truthful", "joyful",
    "tender", "sunny", "goodhearted", "thankful", "careful", "stable", "steady", "faithful",
    "positive", "relaxed", "secure", "sweet", "supportive", "thoughtful", "kind",
    "amazing", "awesome", "great", "perfect", "special", "golden", "ideal", "nice"
]
qui = [
    "odd", "weird", "funny", "strange", "silly", "goofy", "zany", "kooky", "wacky",
    "bizarre", "peculiar", "quirky", "comic", "absurd", "playful", "cheeky", "jolly", "giddy", "merry",
    "droll", "snappy", "spunky", "funky", "jazzy", "snazzy", "flashy", "lively", "quirk", "oddity",
    "weirdness", "humor", "frolic", "giggle", "mischief", "prankish", "antics", "banter", "jest", "tease",
    "clownish", "daft", "madcap", "loony", "whimsy", "curious", "offbeat", "eccentric", "knotty", "quirkiness",
    "random", "chaotic", "cosmic", "surreal", "unusual", "unique", "rare", "wild", "free", "bold",
    "clever", "quick", "sharp", "bright", "loud", "nosy", "sneaky", "tricky", "crafty", "cunning",
    "fearless", "reckless", "play", "joke", "laugh", "spark", "twist", "curve", "zigzag", "bounce",
    "flip", "spin", "wink", "grin", "smirk", "teeter", "tilt", "quirk"
]
ver=[
    "running", "walking", "jumping", "sitting", "standing", "sleeping", "eating", "drinking",
    "reading", "writing", "speaking", "listening", "hearing", "seeing", "watching", "looking",
    "thinking", "knowing", "learning", "teaching", "playing", "working", "studying", "helping",
    "making", "building", "creating", "breaking", "fixing", "moving", "stopping", "starting",
    "opening", "closing", "pushing", "pulling", "carrying", "holding", "throwing", "catching",
    "buying", "selling", "paying", "giving", "taking", "sending", "receiving", "finding",
    "losing", "keeping", "feeling", "loving", "liking", "trying","busy"
    "choosing", "deciding", "hoping", "waiting", "calling", "asking", "answering", "telling",
    "saying", "talking", "smiling", "laughing", "crying", "singing", "dancing", "drawing",
    "painting", "driving", "riding", "traveling", "arriving", "leaving", "growing", "changing",
    "staying", "living", "winning", "planning", "sharing", "trusting", "exploring", "coding"
]
cart = [
    "pow", "bam", "zap", "zing", "zang", "bang", "boom", "pop", "snap", "clap",
    "slam", "wham", "thud", "plop", "poof", "puff", "boop", "beep", "ding", "dong",
    "ping", "pong", "tick", "tock", "buzz", "fizz", "eek", "ack", "ow", "gah",
    "aha", "hah", "hee", "hoho", "nom", "mew", "purr", "bark", "woof", "meow",
    "oink", "moo", "baa", "quak", "honk", "hoot", "ring", "clap", "clik", "clak",
    "crak", "snip", "zip", "zoom", "whiz", "zizz", "blur", "flip", "spin", "dash",
    "skid", "trip", "jump", "bop", "bip", "zap", "pow", "bam", "buzz", "fizz",
    "boop", "ding", "pong", "snap", "slam", "thud", "plop", "puff"
]
foods = [
    "cupcake", "donut", "muffin", "brownie", "cookie", "marshmallow", "pancake", "waffle",
    "jellybean", "gummy", "pudding", "custard", "truffle", "toffee", "caramel", "lollipop",
    "popsicle", "sundae", "parfait", "smoothie", "milkshake", "cocoa", "latte", "mocha",
    "macaron", "croissant", "brioche", "bagel", "pretzel", "biscuit", "shortcake",
    "cheesecake", "tiramisu", "churro", "beignet", "crepe", "cereal", "granola", "yogurt",
    "strawberry", "blueberry", "raspberry", "blackberry", "pineapple", "mango", "papaya",
    "banana", "peach", "apricot", "cherry", "plum", "kiwi", "melon", "watermelon",
    "cantaloupe", "honeydew", "apple", "pear", "grape", "orange", "clementine",
    "tangerine", "mandarin", "lemon", "lime", "coconut", "avocado", "dumpling", "noodle",
    "ramen", "udon", "sushi", "tempura", "onigiri", "takoyaki", "bento", "kimchi",
    "bibimbap", "gnocchi", "pierogi", "spaetzle", "gelato", "sorbet", "panna",
    "cottoncandy", "mochi", "dango", "dorayaki", "taiyaki", "falafel", "hummus",
    "shawarma", "quesadilla", "empanada", "arepa", "cannoli", "profiterole",
    "eclair", "fudge", "acai"
]

#---------------------------------GUI-----------------------------
comm=["_","."," "]
com=["_",".",]
f=set()
root=tk.Tk()
icon=tk.PhotoImage(file="igg.png")
root.iconphoto(True,icon)
root.title( "CUTE IG HANDLE GENERATOR")
#root.bell()

#root.geometry("520x560")
root.resizable(False,False)
root.configure(bg=BG)
card=tk.Frame(root, bg=CARD, highlightbackground=ACCENT, highlightthickness=3)
card.pack(padx=20,pady=20, fill="both", expand=True)
title=tk.Label(card, text="GENERATE YOUR IG USERNAME", bg=CARD,fg="#f72585",font=("Courier New",20,"bold"))
title.pack(pady=20)
recent_patterns=set()
#---------------------------------FUNCTIONS------------------------------
def rando():
    f.clear()
    lb.delete(0, tk.END) 
    while len(f)<20:
        s=f"{random.choice(qui)}{random.choice(['_','.'])}{random.choice(an)}{random.choice(comm)}_{random.randint(10,99)}"
        if s not in f:
            f.add(s)
        else:
            continue
    for u in sorted(f):
        lb.insert(tk.END,u)
def is_valid(username, name=""):
    # basic checks
    if not username:
        return False
    if len(username) < 4 or len(username) > 15:
        return False
    if "__" in username or ".." in username or "  " in username:
        return False
    if not username[0].isalpha():
        return False

    # ---- diversity rules ----

    # avoid direct repetition like jhjh
    if name and username.startswith(name * 2):
        return False

    # avoid too many names ending with the same short name
    if name and username.endswith(name):
        pattern = f"endswith_{name}"
        if pattern in recent_patterns:
            return False
        recent_patterns.add(pattern)

    # avoid repeated prefix patterns (first 4 chars)
    prefix = username[:4]
    if prefix in recent_patterns:
        return False
    recent_patterns.add(prefix)

    return True

    
def named():
    un=set()
    name=na.get().strip().lower()
    if not name:
        return
    lb.delete(0,tk.END)
    while len(un)<20:
        ch=(1,2,3,4,5,6)
        o=random.choice(ch)
        if o==1:
             if len(name) > 2 and name[2] not in "aeiou":
                 st=name[0:3]+"iee"
             else:
                 st=f"{random.choice(po)}{name}{random.choice(comm)}"
        elif o==2:
            
            st=f"{random.choice(qui)}{random.choice(com)}{name}{random.choice(comm)}"
        elif o==3:
            if len(name) > 4 and name[3] in "eilmnopr" and name[2] not in "jhg":
                 st=name[0:3]*2+ str(random.randint(10,99))
             
            else:
                if len(name)>3 and name[2] not in "jh" and name[3]  in "aeiounp":
                    st=f"{name[:4]}{random.choice(po)}{random.choice(comm)}"
                 
                else:
                    st=name[::-1]+random.choice(com)+random.choice(cart)
                    
            
        elif o==4:
            st=f"{name}_is{random.choice(ver)}{random.choice(com)}{random.choice(['now','later','tmrw'])}"
        elif o==5:
            if len(name) > 3:
                if name[2] in "eilmnopr" and name[3]  in "jhgr":
                    st=f"{name[0:3]}{random.choice(cart)}{random.choice(com)}{random.randint(10,99)}"
            else:
                st=f"{name[0:3]}{random.choice(cart)}{random.choice(com)}{random.randint(10,99)}"
        #if is_valid(st,name):
        elif o==6:
            st=name[::-1]+name+random.choice(com)+random.choice(cart)+random.choice(com)+str(random.randint(10,99))
        un.add(st)
    for u in sorted(un):
        lb.insert(tk.END,u)
def arca(parent, text, command):
    return tk.Button(
        parent, text=text, command=command, bg="yellowgreen",fg=BG, font=("Courier New", 11, "bold"),
        relief="flat",
        activebackground="yellow",
        cursor="hand2")
def arcade_beep():
    import winsound
    winsound.Beep(400, 100)

def clipb(event):
    sel=lb.curselection()
    if sel:
        text=lb.get(sel[0])
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        arcade_beep()
#-------------------------------------GUI START-----------------------------------------------
tk.Label(
    card,
    text="ENTER NAME",
    bg=CARD,
    fg=ACCENT2,
    font=("Courier New", 12, "bold")
).pack(pady=(10, 4))    
na=tk.Entry( card,
    bg=LIST_BG,
    fg="#9457EB",
    insertbackground=LIST_FG,
    font=("Courier New", 14),
    justify="center",
    relief="flat")
na.pack(pady=6,ipadx=10,ipady=6)
lb=tk.Listbox(card, width=40, height=12,bg=LIST_BG,
    fg="#8ECF09",
    font=("Courier New", 11),
    selectbackground=ACCENT,
    relief="flat")
lb.bind("<<ListboxSelect>>",clipb)
lb.pack(pady=15)
btn_ran=arca(card, text="generate random username", command=rando) #write a fn for random generator
btn_ran.pack(pady=20)
btn_nam=arca(card, text="generate with nickname", command=named)
btn_nam.pack(pady=20)
ex=tk.Button(root, text="  exit   ",bg=ACCENT, fg=BG, command=root.destroy)
ex.pack(pady=10)



