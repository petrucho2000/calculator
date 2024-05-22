import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        
        self.input_text = tk.StringVar()
        self.input_frame = self.create_input_frame()
        self.buttons_frame = self.create_buttons_frame()
        
        self.create_input_field()
        self.create_buttons()

    def create_input_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def create_input_field(self):
        input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(expand=True, fill='both')

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '%',
            '1', '2', '3', '-', '=',
            '0', '.', '+'
        ]
        
        row_val = 0
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            b = tk.Button(self.buttons_frame, text=button, font=('arial', 18, 'bold'), bd=1, relief='raised', command=action)
            b.grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        for i in range(5):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, button_value):
        if button_value == "C":
            self.expression = ""
            self.input_text.set(self.expression)
        elif button_value == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("error")
                self.expression = ""
        elif button_value == '%':
            try:
                result = str(eval(self.expression) / 100)
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("error")
                self.expression = ""
        else:
            self.expression += str(button_value)
            self.input_text.set(self.expression)

# Создаем основное окно
root = tk.Tk()
calc = Calculator(root)
root.mainloop()

# Функция для тестирования
def test_addition():
    calc.expression = "35+10"
    calc.on_button_click("=")
    assert calc.input_text.get() == "45", f"Expected 45 but got {calc.input_text.get()}"

# Выполним тест
# test_addition()

