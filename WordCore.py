import sys, time
#from MB2 import web_address as web_address
from Name import web_address as web_address

def word_core(sen, sec):
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()   
        time.sleep(sec)

def word_coreg(stub, stubz, sens, stubs):
    global web_address
    web_address = "XX/YY/ZZ"
    marker = 0
    print(stub, end='')
    marker += int(len(stub))
    sys.stdout.flush()   
    time.sleep(0.3)
    temp = int(len(web_address))
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

def word_coret(stub, sen, stubz, sens, stubs):
    marker = 0
    print(stub, end='')
    marker += int(len(stub))
    sys.stdout.flush()   
    time.sleep(0.3)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()   
        marker += 1
        time.sleep(.01)
    while marker != 45:
        marker += 1
        print(" ", end='')
    temp = int(len(web_address))
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

def word_corey(stub, sen, stubs):
    marker = 0
    print(stub, end='')
    marker += int(len(stub))
    sys.stdout.flush()   
    time.sleep(0.2)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()   
        marker += 1
        time.sleep(.01)
    while marker != 97:
        marker += 1
        print(" ", end='')
    print(stubs, end='')

def word_corey_c(stub, sen, stubs):
    marker = 0
    print(stub, end='')
    marker += int(len(stub))
    sys.stdout.flush()
    time.sleep(0)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()
        marker += 1
        time.sleep(0)
    while marker != 116:
        marker += 1
        print(" ", end='')
    print(stubs, end='')

def word_corex(stub, sen):
    print(stub + " ", end='')
    sys.stdout.flush()   
    time.sleep(0.5)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()   
        time.sleep(.01)

def word_corez(sen):
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()   
        time.sleep(0)
