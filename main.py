import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=250)


def bmi():
    Weight = float(my_entry_1.get())
    Height = float(my_entry_2.get())
    m = Height / 100
    B = round(float(Weight / m ** 2), 1)
    my_label_3.config(text=B)

    if B <= 18.5:
        my_label_3.config(text="Underweight")
    elif (B > 18.5) and (B <= 25):
        my_label_3.config(text="Normal")
    elif (B > 25) and (B <= 30):
        my_label_3.config(text="Overweight")
    else:
        my_label_3.config(text="Health is at risk!\n Need to lose")


# label
my_label_1 = tkinter.Label(text="Enter Your Weight (kg)")
my_label_1.place(x=75, y=30)

my_label_2 = tkinter.Label(text="Enter Your Height (cm)")
my_label_2.place(x=75, y=90)

my_label_3 = tkinter.Label(window)
my_label_3.place(x=100, y=180)

# button

my_button_1 = tkinter.Button(text="Calculate", command=bmi)
my_button_1.place(x=100, y=150)

# entry
my_entry_1 = tkinter.Entry(width=15)
my_entry_1.place(x=75, y=60)

my_entry_2 = tkinter.Entry(width=15)
my_entry_2.place(x=75, y=120)

window.mainloop()
