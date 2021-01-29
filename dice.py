import random
from tkinter import *
import urllib.request
from PIL import Image
from io import BytesIO



root = Tk()
root.geometry("700x250")
root.config(bg='white')
root.title("Roll the Dices")
root.resizable(0, 0)






option = Listbox(root,height=2)
option.insert(1,"Single")
option.insert(2,"Double")

option.place(x=100,y=10)
option.pack()




l1 = Label(root)



def roll(type):
	number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	if type == "Single":
		l1.config(text = f'{random.choice(number)}',font=("", 200), bg = 'white')

	else:
		l1.config(text = f'{random.choice(number)}{random.choice(number)}',font=("", 200),bg = 'white')	

	l1.pack()





def choice():
	try:
		selection = option.get(option.curselection())
	except Exception as e:
		selection = "Single"




		
	mode = Label(root)
	mode.config(text = selection,font=("", 8),bg = 'white')
	mode.place(x=50,y=5)






	bt = Button(root,text="Roll it...", bg='red',state = NORMAL,command= lambda: roll(selection), fg = 'white')

	bt.place(x=450, y = 5)



head = Label(root)
head.config(text = f'Mode : ',font=("", 8,'bold'),bg = 'white')
head.place(x=10,y=5)




act_bt = Button(root,text ="Activate",bg='blue',fg = 'white', command=choice)

act_bt.place(x=200, y = 5)





	









root.mainloop()
