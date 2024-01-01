from tkinter import *


expression = "" 



def press(num): 
	global expression 

	expression = expression + str(num) 

	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	try: 

		global expression 

		total = str(eval(expression)) 

		equation.set(total) 

		expression = "" 

	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


if __name__ == "__main__": 
    
	sagnik_root = Tk() 

	
	sagnik_root.configure(background="white") 

	
	sagnik_root.title("Sagnik's Calculator") 

	sagnik_root.geometry("300x230") 

	equation = StringVar() 
 
	expression_field = Entry(sagnik_root, textvariable=equation) 

	expression_field.grid(columnspan=6, ipadx=90)

	
	button1 = Button(sagnik_root, text=' 1 ', fg='white', bg='black', 
					command=lambda: press(1), height=2, width=7) 
	button1.grid(row=2, column=0) 

	button2 = Button(sagnik_root, text=' 2 ', fg='white', bg='black', 
					command=lambda: press(2), height=2, width=7) 
	button2.grid(row=2, column=1) 

	button3 = Button(sagnik_root, text=' 3 ', fg='white', bg='black', 
					command=lambda: press(3), height=2, width=7) 
	button3.grid(row=2, column=2) 

	button4 = Button(sagnik_root, text=' 4 ', fg='white', bg='black', 
					command=lambda: press(4), height=2, width=7) 
	button4.grid(row=3, column=0) 

	button5 = Button(sagnik_root, text=' 5 ', fg='white', bg='black', 
					command=lambda: press(5), height=2, width=7) 
	button5.grid(row=3, column=1) 

	button6 = Button(sagnik_root, text=' 6 ', fg='white', bg='black', 
					command=lambda: press(6), height=2, width=7) 
	button6.grid(row=3, column=2) 

	button7 = Button(sagnik_root, text=' 7 ', fg='white', bg='black', 
					command=lambda: press(7), height=2, width=7) 
	button7.grid(row=4, column=0) 

	button8 = Button(sagnik_root, text=' 8 ', fg='white', bg='black', 
					command=lambda: press(8), height=2, width=7) 
	button8.grid(row=4, column=1) 

	button9 = Button(sagnik_root, text=' 9 ', fg='white', bg='black', 
					command=lambda: press(9), height=2, width=7) 
	button9.grid(row=4, column=2) 

	button0 = Button(sagnik_root, text=' 0 ', fg='white', bg='black', 
					command=lambda: press(0), height=2, width=7) 
	button0.grid(row=5, column=0) 

	plus = Button(sagnik_root, text=' + ', fg='black', bg='red', 
				command=lambda: press("+"), height=2, width=7) 
	plus.grid(row=2, column=3) 

	minus = Button(sagnik_root, text=' - ', fg='black', bg='red', 
				command=lambda: press("-"), height=2, width=7) 
	minus.grid(row=3, column=3) 

	multiply = Button(sagnik_root, text=' * ', fg='black', bg='red', 
					command=lambda: press("*"), height=2, width=7) 
	multiply.grid(row=4, column=3) 

	divide = Button(sagnik_root, text=' / ', fg='black', bg='red', 
					command=lambda: press("/"), height=2, width=7) 
	divide.grid(row=5, column=3) 

	equal = Button(sagnik_root, text=' = ', fg='white', bg='green', 
				command=equalpress, height=2, width=7) 
	equal.grid(row=5, column=2) 

	clear = Button(sagnik_root, text='Clear', fg='black', bg='red', 
				command=clear, height=2, width=7) 
	clear.grid(row=5, column='1') 

	Decimal= Button(sagnik_root, text='.', fg='white', bg='black', 
					command=lambda: press('.'), height=2, width=7) 
	Decimal.grid(row=6, column=0) 

	sagnik_root.mainloop() 
