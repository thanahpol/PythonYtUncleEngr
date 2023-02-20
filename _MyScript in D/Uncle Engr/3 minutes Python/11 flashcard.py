#flashcard.py

from tkinter import *
from tkinter import ttk
import random

GUI = Tk()
GUI.geometry('500x300')

v_eng = StringVar()
v_thai = StringVar()

L1 = ttk.Label(GUI,textvariable=v_eng,'')
L1.pack(pady=10)

L2 = ttk.Label(GUI,textvariable=v_thai)
L2.pack(pady=10)

vocab = {'cat':'แมว', 'dog':'สุนัข', 'chicken':'ไก่'}
vocabeng = list(vocab.keys())

def English():
    v_eng.set(random.choice(vocabeng))


def Thai():
    v_thai.set(vocab[v_eng.get()])

B1 = ttk.Button(GUI,text='Eng',command=English)
B1.pack()

B2 = ttk.Button(GUI,text='ไทย',command=Thai)
B2.pack()

GUI.mainloop()



    




