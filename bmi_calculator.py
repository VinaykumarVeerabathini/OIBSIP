import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if unit.get() == 'Metric':
            bmi = weight / (height ** 2)
        else:
            height_m = height * 0.3048  
            weight_kg = weight * 0.453592 
            bmi = weight_kg / (height_m ** 2)
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")
root = tk.Tk()
root.title("BMI Calculator")
tk.Label(root, text="Weight:").grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, text="Height:").grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)
unit = tk.StringVar(value='Metric')
tk.Radiobutton(root, text="Metric (kg, meters)", variable=unit, value='Metric').grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Imperial (lbs, feet)", variable=unit, value='Imperial').grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
