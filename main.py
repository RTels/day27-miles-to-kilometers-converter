import tkinter


def calculate():
    result = int(input.get()) * 1.609
    answer.config(text=f"{result}")


# Window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# Label

label_1 = tkinter.Label(text="Miles", font=("Arial", 11,))
label_1.grid(column=2, row=0)
label_2 = tkinter.Label(text="is equal to", font=("Arial", 11))
label_2.grid(column=0, row=1)
label_3 = tkinter.Label(text="Km", font=("Arial", 11))
label_3.grid(column=2, row=1)
answer = tkinter.Label(text=f"0", font=("Arial", 11))
answer.grid(column=1, row=1)


# Entry

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)


# Button

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)




window.mainloop()
