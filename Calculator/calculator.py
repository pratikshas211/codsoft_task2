import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
       
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return
       
        label_result.config(text=f"Result: {result}")  
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")  

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")


label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root, width=30)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root, width=30)
entry_num2.pack(pady=5)


operation_var = tk.StringVar(root)
operation_var.set("+") 

operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=10)


calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)


label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=20)


root.mainloop()
