from tkinter import *

window = Tk()

window.title('BMI Calculator')
window.geometry("400x400")
window.configure(bg='lightcyan')

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height * height)
    bmi = round(bmi, 1)
    name = username.get()

    msg = ""

    if bmi<=18.4:
        msg = "Under weight"
    elif bmi>18.4 and bmi<=24.9:
        msg = "Normal weight"
    elif bmi>24.9 and bmi<=29.9:
        msg = "Over weight"
    elif bmi>29.9 and bmi<=34.9:
        msg = "Obese"
    elif bmi>34.9:
        msg = "Highly Obese"
    else:
        msg = "Something Went Wrong"      

    output_message = Label(window,text=name + ", your BMI is " + str(bmi) + " and you are " +msg,bg="lightcyan",fg="red",font=("Calibri", 12,"bold"))
    output_message.place(x=20, y=315)

app_label = Label(window,text="BMI CALCULATOR",fg="black",bg="lightcyan",font=("Calibri", 20,"bold"),bd=5)
app_label.place(x=50, y=20)

name_label = Label(window,text="Your Name",fg="black",bg="lightcyan",font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username = Entry(window, text="", bd=2, width=22)
username.place(x=170, y=92)

height_label = Label(window,text="Enter Height (m)",fg="black",bg="lightcyan",font=("Calibri", 12))
height_label.place(x=20, y=140)

height_entry = Entry(window, text="", bd=2, width=15)
height_entry.place(x=170, y=142)

weight_label = Label(window,text="Enter Weight (Kg)",fg="black",bg="lightcyan",font=("Calibri", 12))
weight_label.place(x=20, y=185)

weight_entry = Entry(window, text="", bd=2, width=15)
weight_entry.place(x=170, y=187)

calculate_button = Button(window,text="CALCULATE",fg="black",bg="cyan",bd=4,command=calculate_bmi)
calculate_button.place(x=20, y=245)

result_label = Label(window,text="Result",bg="lightcyan",fg="red",font=("Calibri", 12,"bold"))
result_label.place(x=20, y=290)

window.mainloop()