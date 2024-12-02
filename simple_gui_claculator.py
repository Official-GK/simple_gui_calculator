import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.display = tk.Entry(root, font=('Arial', 20), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)
        self.create_buttons()

        # Initialize variables
        self.current_input = ''
        self.operator = ''

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, width=10, height=3, command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                self.current_input = str(eval(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.current_input)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.current_input = ''
        elif char == 'C':
            self.current_input = ''
            self.display.delete(0, tk.END)
        else:
            self.current_input += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_input)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()