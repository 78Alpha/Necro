import os, secrets

User_Name = "LeyCone@sidramail.gam"
Rec_lib = ["MelissaAn1335"]
name_first = ["Anne", "Arissa", "Becky", "Belle", "Courtney", "Charli", "Deidre", "Daisy", "Eliza", "Edith", "Francis", "Flora", "Gabriella", "Georgia", "Hannah", "Hayley", "Isabella", "Iris", "Jacquoline", "Jane", "Kara", "Kenzie", "Linda", "Lorraine", "Maria", "Mandy", "Nadia", "Nora", "Olia", "Onia", "Pipi", "Pamela", "Quora", "Quadora", "Rana", "Ria", "Sonata", "Sharryn", "Talia", "Terrissa", "Umbrion", "Ultia", "Veronica", "Velma", "Wendy", "Wilma", "Xandria", "Xyla", "Yiole", "Yandera", "Zora", "Zelda"]
name_first_male = ["Axel", "Aron", "Brandon", "Brick", "Cody", "Corbon", "Daniel", "Drake", "Eric", "Erikson", "Frank", "Ford", "Greg", "Garret", "Harvey", "Hank", "Irc", "Indica", "Jack", "James", "Kahn", "Kira", "Larry", "Link", "Mac", "Mark", "Noel", "Noah", "Orion", "Orwell", "Pat", "Perry", "Quinn", "Qarl", "Randy", "Rick", "Steve", "Soma", "Thomas", "Timothy", "Urden", "Ukon", "Victor", "Vann", "Will", "Warren", "Xander", "Xerx", "Yoda", "Yuki", "Zork", "Zane"]
last_name = ["Acron", "Arner", "Borgiue", "Bandie", "Cordel", "Carissman", "Doriday", "Denvido", "Evangelon", "Ericovan", "Faraday", "Feaux", "Gexic", "Grandure", "Harrison", "Hordich", "Indorcatna", "Icoruz", "Joshatan", "Juvaz", "Kinderstan", "Kenku", "Loric", "Lando", "Michaels", "Mandrid", "Novac", "Nurra", "Oviccarius", "Ophilia", "Pander", "Packitosh", "Qutil", "Qasmer", "Rosenplat", "Rose", "Stevens", "Smith", "Thorinson", "Torik", "Uvalisa", "Uda", "Vikson", "Victinstil", "Warrez", "Wack", "Xuvasch", "Xil", "Yoranda", "Yikumachi", "Zerra", "Zenia"]
address_space_lib = ["@Gizman.io", "@Mayzon.gm", "@ArcSub.lan", "@NSArc.gov", "@Bastion.io", "@ZanSen.edu", "@Potanra.ru"]
global web_address
web_address = ''
gender = ["Male", "Female"]

def name_gen_2():
    global gender
    a = secrets.choice(gender)
    global web_address
    global name_first_male
    global name_first
    global last_name
    global address_space_lib
    if a == "Male":
        b = secrets.choice(name_first_male)
        c = secrets.choice(last_name)
        d = secrets.choice(address_space_lib)
        web_address = str(b) + str(c) + str(d)
        os.system("rm Name.py")
        with open("Name.py", 'w') as file:
            file.write("web_address = " + "'" + str(web_address) + "'" + "\n")
            file.write("User_Name = " + "'" + str(User_Name) + "'" + "\n")
    elif a == "Female":
        b = secrets.choice(name_first)
        c = secrets.choice(last_name)
        d = secrets.choice(address_space_lib)
        web_address = str(b) + str(c) + str(d)
        os.system("rm Name.py")
        with open("Name.py", 'w') as file:
            file.write("web_address = " + "'" + str(web_address) + "'" + "\n")
            file.write("User_Name = " + "'" + str(User_Name) + "'" + "\n")
    else:
        print("Interpreter Error")