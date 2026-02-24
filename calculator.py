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


orange_color = "#E2791E"
grey_color = "#706A74"
black_color = "#1A020A"

#Window Setup
window = tkinter.Tk()
window.title("Calculator")

frame = tkinter.Frame(window)
label = tkinter.Label(frame)

window.mainloop()