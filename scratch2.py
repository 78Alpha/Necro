import threading, time, Loading, Clear, sys, secrets, UniData


class DoThis(threading.Thread):

    def __init__( self ):
        threading.Thread.__init__( self )

        self.stop = False

    def run(self):
        global uni
        while not self.stop:
            w = int(float(uni / limit) * 100)
            Clear.clear()
            b = "["
            for i in range(w):
                b += "|"
            for i in range(100 - int(w)):
                b += "."
            b2 = str(b) + "]" + str(w) + "% Complete"
            print(b2)
            print(uni)
            uni += 11
            with open('UniData.py', 'r') as file:
                data = file.readlines()
            data[27] = "uni = " + str(uni) + "\n"
            with open("UniData.py", 'w') as file:
                file.writelines(data)
            time.sleep(1)

with open('UniData.py', 'r') as file:
    data = file.readlines()
data[27] = "uni = " + str(1) + "\n"
with open("UniData.py", 'w') as file:
    file.writelines(data)
a = None
#global uni

uni = UniData.uni
limit = 100

def r():
    while True:
        c = input("'start' or 'stop': ")
    #global uni
        import UniData
        d = UniData.uni
        if c == "start":
            Clear.clear()
            a = DoThis()
            a.start()
        if c == "stop":
            Clear.clear()
            a.stop = True
            a.join()
            a = None
            print("Manual Stop")
        if uni >= 100 or d >= 100:
            Clear.clear()
            a.stop = True
            a.join()
            a = None
            print("Loading Complete")

def load_reset():
    v = uni
    if v > 1:
        with open('UniData.py', 'r') as file:
            data = file.readlines()
        data[27] = "uni = " + str(1) + "\n"
        with open("UniData.py", 'w') as file:
            file.writelines(data)
        import UniData
        r()
    elif v == 1:
        r()
    elif v < 1:
        with open('UniData.py', 'r') as file:
            data = file.readlines()
        data[27] = "uni = " + str(1) + "\n"
        with open("UniData.py", 'w') as file:
            file.writelines(data)
        import UniData
        r()
    else:
        print("Error")

load_reset()