import time, sys, secrets, S1, os, WordCore, Name, Clear, Loading

User_Name = Name.User_Name
global web_address
web_address = Name.web_address
pool = ['S1']
global used_story
used_story = ''

def mail_num_gen():
    text_value = secrets.choice(pool)
    global used_story
    used_story = text_value

def arc_1():
    arc1 = S1.text
    arc2 = S1.text2
    arc3 = S1.text3
    global web_address
    web_address = "XX/YY/ZZ"
    print("@@@                                                                                              @@@")
    WordCore.word_coreg("@@@  >>> ", arc1, web_address, "@@@\n")
    print("@@@                                                                                              @@@")
    WordCore.word_coreg("@@@  >>> ", arc2, web_address, "@@@\n")
    print("@@@                                                                                              @@@")
    WordCore.word_coreg("@@@  >>> ", arc3, web_address, "@@@\n")

def main_menu():
    mail()

def basic_mail_box():
    mail()
    import Address_Space
    Address_Space.name_gen_2()
    import Name
    global web_address
    web_address = Name.web_address
    print("@@@                                                                                              @@@")
    Loading.loading("@@@   ", "Securing Connection", "....","                                                            Done!   @@@\n")
    print("@@@                                                                                              @@@")
    WordCore.word_coret("@@@      ", User_Name, "    ****", web_address, "@@@\n")
    arc_1()

basic_mail_box()
Clear.clear()