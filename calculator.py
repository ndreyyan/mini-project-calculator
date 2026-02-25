import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_len = len(button_values) 
column_len = len(button_values[0])

orange_color = "#E2791E"
grey_color = "#706A74"
black_color = "#1A020A"
color_white = "#F7F6F2"

# Window Setup
window = tkinter.Tk()
window.title("Calculator")

window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0",
                    font=("Arial",45),
                    background=black_color,
                    foreground=color_white,
                    anchor='e',
                    width=column_len)

label.grid(row=0, column=0, columnspan=column_len ,sticky="we")

for row in range(row_len):
    for column in range(column_len):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_len-1, height=1,
                                command=lambda value=value: button_clicked(value))
        button.grid(row=row+1, column=column)

        if value in top_symbols:
            button.config(foreground=black_color,background=color_white)
        elif value in right_symbols:
            button.config(foreground=color_white,background=orange_color)
        else:
            button.config(foreground=color_white,background=grey_color)
        button.grid(row=row+1,column=column)

frame.pack()

A = "0"
operator = None
B = None

def all_clear():
    global A, B, operator
    A = "0"
    operator = None
    B = None
    return 0

def remove_float(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, label, A, operator, B

    if value in right_symbols:
        pass
    elif value in top_symbols:
        if value == "AC":
            all_clear()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_float(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_float(result)
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value


window.mainloop()