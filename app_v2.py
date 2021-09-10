#This is a basic programme which genrates multiplication tables when users put there number
#This is can generate an Table 

#Importing Stuff
import tkinter as tk

#Function to calculate the Table and to Display it
def calculate(canvas):
    value = textField.get()
    
    product_1 = int(value) * 1
    product_2 = int(value) * 2
    product_3 = int(value) * 3
    product_4 = int(value) * 4
    product_5 = int(value) * 5
    product_6 = int(value) * 6
    product_7 = int(value) * 7
    product_8 = int(value) * 8
    product_9 = int(value) * 9
    product_10 = int(value) * 10

    display1 = str(value) + " ×" + " 1" + " = " + str(product_1)
    display2 = str(value) + " ×" + " 2" + " = " + str(product_2)
    display3 = str(value) + " ×" + " 3" + " = " + str(product_3)
    display4 = str(value) + " ×" + " 4" + " = " + str(product_4)
    display5 = str(value) + " ×" + " 5" + " = " + str(product_5)
    display6 = str(value) + " ×" + " 6" + " = " + str(product_6)
    display7 = str(value) + " ×" + " 7" + " = " + str(product_7)
    display8 = str(value) + " ×" + " 8" + " = " + str(product_8)
    display9 = str(value) + " ×" + " 9" + " = " + str(product_9)
    display10 = str(value) + " ×" + " 10" + " = " + str(product_10)

    label1.config(text = display1)
    label2.config(text = display2)
    label3.config(text = display3)
    label4.config(text = display4)
    label5.config(text = display5)
    label6.config(text = display6)
    label7.config(text = display7)
    label8.config(text = display8)
    label9.config(text = display9)
    label10.config(text = display10)


#GUI Code
canvas = tk.Tk()
canvas.geometry("550x550")
canvas.title("Multiplication Table Generator")
canvas.wm_iconbitmap("favicon.ico")

#Font
f = ("Comfortaa", 15)
t = ("Comfortaa", 25)

#heading
head = tk.Label(canvas, font = t, text = "Multiplication Table Generator")
head.pack()

#Text Field to get number (input)
textField = tk.Entry(canvas, justify='center', width = 15, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', calculate)

#Labels to set number (output) 
label1 = tk.Label(canvas, font=f)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

label3 = tk.Label(canvas, font=f)
label3.pack()

label4 = tk.Label(canvas, font=f)
label4.pack()

label5 = tk.Label(canvas, font=f)
label5.pack()

label6 = tk.Label(canvas, font=f)
label6.pack()

label7 = tk.Label(canvas, font=f)
label7.pack()

label8 = tk.Label(canvas, font=f)
label8.pack()

label9 = tk.Label(canvas, font=f)
label9.pack()

label10 = tk.Label(canvas, font=f)
label10.pack()

canvas.mainloop()