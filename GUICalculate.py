from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Function for store a program

def calprofit():
	at = int(alltank.get()) # .get() is a pulling data out from box
	cal_sell = at*30
	cal_cost = at*20
	profit = cal_sell - cal_cost
	rolex = profit*1000000//350000
	textshow = 'I have profit: {:,d} million\n'.format(profit)
	textshow2 = 'You can buy Rolex: {:,d} pieces'.format(rolex)	
	messagebox.showinfo('My Profit', textshow+textshow2)
	#print(at*5)

GUI = Tk()
GUI.geometry('500x480+0+600')
GUI.title('Tank Profit Calculation')

'''
BCal = Button(GUI,text='Calculate')
BCal.pack()
'''

bg = PhotoImage(file='D:/OneDrive - b-tu.de/Work from Home/_Python1/tank.png').subsample(3)

tankpic = ttk.Label(GUI,image=bg)
tankpic.pack(pady=10)

# Text for user
tanktext = ttk.Label(GUI,text = 'Fill the number of selling tank!', font = ('Trebuchet MS', 18))
tanktext.pack(pady=10)

#Text box
alltank = StringVar()

Etank = ttk.Entry(GUI,textvariable = alltank, font = ('Trebuchet MS', 18))
Etank.pack(pady=20)

BCal2 = ttk.Button(GUI,text='Calculate',command = calprofit)
BCal2.pack(ipadx=20, ipady=10)

GUI.mainloop()
