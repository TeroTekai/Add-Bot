import tkinter as tk

# Creating base window.
root = tk.Tk()
icon = tk.PhotoImage(file='icon_small.png')
root.geometry("900x600")
root.iconphoto(False, icon)
root.configure(bg="black")
root.title("AddBot")


def end():
    pass  # Makes Add bot button do nothing without greying it out.


def start():

    button.config(command=end)
    label.config(text="AddBot", justify="left")
    text_var.set("")
    add_text = text_var.get()
    add_text += ">My Name is AddBot! Whats your name?: "  # Changes text without overwriting
    text_var.set(add_text)

    canvas = tk.Canvas(root, width=200, height=200, bg="black", bd="0", relief="sunken")
    canvas.place(x=50, y=250)  # canvas contains clickable items

    can_label = tk.Label(root, text="Enter name!", bg="black", fg="green3", font=("terminal", 10))
    canvas.create_window(100, 20, window=can_label)

    text_box = tk.Entry(root)
    canvas.create_window(100, 40, window=text_box)

    def get_name():  # Function pulls name from input and sets next click to a new command
        name = text_box.get()
        add_name = text_var.get()
        add_name += f"\r>Nice to meet you {name}! \r>Do you want me to add something for you?"
        text_var.set(add_name)
        name_button.config(command=question)
        can_label.config(text="Yes or No?", bg="black", fg="green3", font=("terminal", 10))
        text_box.delete(0, tk.END)

    def question():
        answer = text_box.get().capitalize()
        try:
            if answer == "Yes":
                text_box.delete(0, tk.END)
                request_addend = text_var.get()
                request_addend += f"\r>Cool! Enter the numbers in the box please!"
                text_var.set(request_addend)
                can_label.config(text="First Number?", bg="black", fg="green3", font=("terminal", 10))
                name_button.config(command=math_1)
            elif answer == "No":
                text_box.delete(0, tk.END)
                rejection = text_var.get()
                rejection += f"\r>i tHOuGht We weRe BESTIES!!!!! :( "
                text_var.set(rejection)
        except ValueError:
            text_box.delete(0, tk.END)
            error = text_var.get()
            error += "\r>That's not a number silly!"
            text_var.set(error)
        finally:
            pass

    addends = []

    def math_1():
        addends.append(float(text_box.get()))
        name_button.config(command=math_2)
        can_label.config(text="Second Number?",  bg="black", fg="green3", font=("terminal", 10))
        first = text_var.get()
        first += f"\r>Good Choice! And the other?"
        text_var.set(first)
        text_box.delete(0, tk.END)

    def math_2():
        addends.append(float(text_box.get()))
        text_box.delete(0, tk.END)
        second = text_var.get()
        second += f"\r>Excellent. Now press Enter to solve!"
        text_var.set(second)
        name_button.config(command=solution)
        can_label.config(text="Solve", bg="black", fg="green3", font=("terminal", 10))

    def solution():
        final_number = sum(addends)
        final = text_var.get()
        final += f"\r>Your number is {final_number} We did it!\r" \
                 f">Your so smart new best friend!"
        text_var.set(final)
        restart_button = tk.Button(root, text="Restart?", command=start,)
        canvas.create_window(100,100, window=restart_button)
        name_button.destroy()
        can_label.config(text="Restart?")


    name_button = tk.Button(root, text='Enter', command=get_name, bg='grey', fg='black',
                            font=('terminal', 9, 'bold'))
    canvas.create_window(100, 65, window=name_button)


label = tk.Label(root, text="Welcome. Press button to start.",
                 font=("Terminal", 25), bg="black", fg="green3")
label.place(x=50, y=0)
button = tk.Button(root, text="Add-Bot", height=120, width=100,
                   image=icon, bg="black", fg="green3",
                   activebackground="black",
                   activeforeground="green3",
                   state=tk.ACTIVE, compound="bottom", command=start)
button.place(x=100, y=100)
text_var = tk.StringVar()
label_2 = tk.Label(root, textvariable=text_var, borderwidth=3, bg="black", fg="green3",
                   font=("Terminal", 16), relief="sunken", width=55, anchor="w", justify="left")
label_2.place(x=300, y=100)

root.mainloop()
