import tkinter as tk
import os, Test, Test2, MailBox
#import numpy as np
#import matplotlib.pyplot as plt
# "." and "|" have same pixel width

root = tk.Tk()  # declare root in global scope for simplicity

global df
df = [57, 66, 77]


class new_button:

    def __init__(self, A_id):

        self.id = A_id
        but = tk.Button(root, text=self.id, command=self.new_window)
        but.pack(side="top", padx=5, pady=5)

    def new_window(self):

        if self.id == "Menu":
            top = tk.Toplevel(root)
            top.title('text')
            text = MailBox.mail()
            label = tk.Label(top, text=text, fg='red')
            label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        elif self.id == "value":
            top = tk.Toplevel(root)
            top.title('word')
            top.configure(background='black')
            #value = os.system("py -3 Test.py")
            Test2.randommizer()
            value2 = Test2.inf3
            Test.randommizer()
            value3 = Test.inf2
            value = "\n" + str(value3) + "\n" + str(value2)
            label = tk.Label(top, text=str(value), fg='green', bg='black')
            #label = tk.Label(top, text=str(value2), fg='green', bg='black')
            label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        else:
            top = tk.Toplevel(root)
            top.title('fail')
            label = tk.Label(top, text="Some text", fg='pink')
            label.pack(side="top", fill="both", expand=True, padx=20, pady=20)


if __name__ == "__main__":
    name = ["Menu", "value", "curio"]
    for i in range(3):  # df['AccountId']:##for each id create a button

        butt = new_button(A_id=name[i-1])

    root.mainloop()