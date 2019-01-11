import sys, time, random, secrets

User_Name = "LeyCone@sidramail.gam"
Rec_lib = ["MelissaAn1335"]
name_first = ["Anne", "Arissa", "Becky", "Belle", "Courtney", "Charli", "Deidre", "Daisy", "Eliza", "Edith", "Francis", "Flora", "Gabriella", "Georgia", "Hannah", "Hayley", "Isabella", "Iris", "Jacquoline", "Jane", "Kara", "Kenzie", "Linda", "Lorraine", "Maria", "Mandy", "Nadia", "Nora", "Olia", "Onia", "Pipi", "Pamela", "Quora", "Quadora", "Rana", "Ria", "Sonata", "Sharryn", "Talia", "Terrissa", "Umbrion", "Ultia", "Veronica", "Velma", "Wendy", "Wilma", "Xandria", "Xyla", "Yiole", "Yandera", "Zora", "Zelda"]
name_first_male = ["Axel", "Aron", "Brandon", "Brick", "Cody", "Corbon", "Daniel", "Drake", "Eric", "Erikson", "Frank", "Ford", "Greg", "Garret", "Harvey", "Hank", "Irc", "Indica", "Jack", "James", "Kahn", "Kira", "Larry", "Link", "Mac", "Mark", "Noel", "Noah", "Orion", "Orwell", "Pat", "Perry", "Quinn", "Qarl", "Randy", "Rick", "Steve", "Soma", "Thomas", "Timothy", "Urden", "Ukon", "Victor", "Vann", "Will", "Warren", "Xander", "Xerx", "Yoda", "Yuki", "Zork", "Zane"]
last_name = ["Acron", "Arner", "Borgiue", "Bandie", "Cordel", "Carissman", "Doriday", "Denvido", "Evangelon", "Ericovan", "Faraday", "Feaux", "Gexic", "Grandure", "Harrison", "Hordich", "Indorcatna", "Icoruz", "Joshatan", "Juvaz", "Kinderstan", "Kenku", "Loric", "Lando", "Michaels", "Mandrid", "Novac", "Nurra", "Oviccarius", "Ophilia", "Pander", "Packitosh", "Qutil", "Qasmer", "Rosenplat", "Rose", "Stevens", "Smith", "Thorinson", "Torik", "Uvalisa", "Uda", "Vikson", "Victinstil", "Warrez", "Wack", "Xuvasch", "Xil", "Yoranda", "Yikumachi", "Zerra", "Zenia"]
address_space_lib = ["@Gizman.io", "@Mayzon.gm", "@ArcSub.lan", "@NSArc.gov", "@Bastion.io", "@ZanSen.edu", "@Potanra.ru"]
global web_address
web_address = ''
gender = ["Male", "Female"]

def name_gen():
    #random.seed(1)
    global name_first
    global name_first_male
    global last_name
    global address_space_lib
    global web_address
    for i in range(1000):
        v1 = random.randint(0, len(name_first)-1)
        v2 = random.randint(0, len(name_first_male)-1)
        v3 = random.randint(0, len(last_name)-1)
        v4 = random.randint(0, len(address_space_lib)-1)
        if str(str(name_first[v1]) + " " + str(last_name[v3]) + str(address_space_lib[v4])) in web_address or str(str(name_first_male[v2]) + " " + str(last_name[v3]) + str(address_space_lib[v4])) in web_address:
            return
        elif str(str(name_first[v1]) + " " + str(last_name[v3]) + str(address_space_lib[v4])) not in web_address or str(str(name_first_male[v2]) + " " + str(last_name[v3]) + str(address_space_lib[v4])) not in web_address:
            web_address.append(str(name_first[v1]) + str(last_name[v3]) + str(address_space_lib[v4]))
            web_address.append(str(name_first_male[v2]) + str(last_name[v3]) + str(address_space_lib[v4]))
        else:
            print("Interpreter Error")

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
    elif a == "Female":
        b = secrets.choice(name_first)
        c = secrets.choice(last_name)
        d = secrets.choice(address_space_lib)
        web_address = str(b) + str(c) + str(d)
    else:
        print("Interpreter Error")
    #print(web_address)


def name_out():
    with open("file.txt", 'w') as f:
        for n in web_address:
            f.write(str(n) + "\n")

def name_in():
    with open("file.txt", "r") as f:
        for line in f:
            web_address.append(line.strip())

def word_coret(stub, sen, stubz, sens, stubs): # Stationary title with a natural typing statement, needs to be 89 characters
    marker = 0
    print(stub, end='')
    marker += int(len(stub))
    sys.stdout.flush()  # Needed for Unix based systems
    time.sleep(0.3)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()  # Needed for Unix based systems
        marker += 1
        time.sleep(.01)
    while marker != 45:
        marker += 1
        print(" ", end='')
    temp = int(len(User_Name)) + int(len(address_space_lib)) + int(len(Rec_lib)) #Must be -8, lim, 92
    temp2 = 92 - temp
    for letters in stubz:
        print(letters, end='')
        sys.stdout.flush()
        marker += 1
        time.sleep(0.01)
    while marker != int(temp2):
        if marker > 92:
            input()
        marker += 1
        print(" ", end='')
    for letterz in sens:
        print(letterz, end='')
        sys.stdout.flush()
        marker += 1
        time.sleep(0.01)
    while marker != 97:
        marker += 1
        print(" ", end='')
    print(stubs, end='')

def mail():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@                                                                                             @@@")
    print("@@@@                                                                                             @@@")
    print("@@@@ @          @; `@@@@@@@  `@@@@@@@@ ;@      @; @@@@@@@@                                       @@@")
    print("@@@@ @@        @@+ @@:::::@@ @@::::::: ;@      @; @:::::::                                       @@@")
    print("@@@@ @@@      @@@+ @      ;@ @# @@@@@@ ;@      @; @::::::                                        @@@")
    print("@@@@ @ @@    @@ @+ @::::::+@ @# @@@@@@ ;@      @; @@@@@@@@.          @@@@@@@@@@@@@@@@@@          @@@")
    print("@@@@ @  @@  @@  @+ @@@@@@@@@ @#      @ ;@      @;        @#         ` @@@@@@@@@@@@@@@@           @@@")
    print("@@@@ @   @@#@   @+ @      ;@ @#      @ ;@      @;        @#         @` #@@@@@@@@@@@@@  @         @@@")
    print("@@@@ @    @@    @+ @      ;@ +@@@@@@@@  @@@@@@@@  @@@@@@@@`         @@: '@@@@@@@@@@@  @@         @@@")
    print("@@@@                                                                @@@' '@@@@@@@@@  @@@         @@@")
    print("@@@@                                                                @@@@' :@@@@@@@  @@@@         @@@")
    print("@@@@                                                                @@@@@# `@@@@@  @@@@@         @@@")
    print("@@@@                                                                @@@@@@   @@@  `@@@@@         @@@")
    print("@@@@                                                                @@@@@  @ `@ `@ `@@@@         @@@")
    print("@@@@                   @;         #@  @@@@@@@. .@ :@                @@@@  @@@  `@@@  @@@         @@@")
    print("@@@@                   @@:       +@@ @@:::::@@ .@ :@                @@@  @@@@@:@@@@@  @@         @@@")
    print("@@@@                   @+@.     ;@+@ @+      @ .@ :@                @@  @@@@@@@@@@@@@  @         @@@")
    print("@@@@                   @:;@`   :@.;@ @#::::::@ .@ :@                @  @@@@@@@@@@@@@@@           @@@")
    print("@@@@                   @: +@` .@: ;@ @@@@@@@@@ .@ :@                 `@@@@@@@@@@@@@@@@@          @@@")
    print("@@@@                   @:  +@`@:  ;@ @+      @ .@ :@                                             @@@")
    print("@@@@                   @:   #@'   ;@ @+      @ .@ :@@@@@@                                        @@@")
    print("@@@@                                                                                             @@@")
    print("@@@@                                                                                             @@@")
    print("@@@@                                                                                             @@@")
    print("@@@@                                                                                             @@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@                                                                                             @@@")
    print("@@@@                                                                                             @@@")

def basic_mail_box():
    rand = random.randint(0, len(Rec_lib))
    rand2 = random.randint(0, len(address_space_lib))
    mail()
    print("@@@@                                                                                             @@@")
    word_coret("@@@@     ", User_Name, "     ****",Rec_lib[rand] + address_space_lib[rand2], "@@@")

#basic_mail_box()
#print(len("@@@@                                                                                             @@@"))
#name_gen()
#name_in()
name_gen_2()
print(web_address)
#name_out()