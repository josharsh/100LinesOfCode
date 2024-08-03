import tkinter as tk

class Calculator:
    def __init__(self):
        self.current_expression = ""
        self.history_list = []  # Liste pour stocker l'historique des expressions
        fen = tk.Tk()
        fen.geometry("800x700")
        fen.resizable(True, True)
        self.create_button(fen)
        self.display(fen)
        fen.mainloop()

    def create_button(self, fen):
        op_plus = tk.Button(fen, text='+', command=lambda: self.on_button_click('+'))
        op_moins = tk.Button(fen, text='-', command=lambda: self.on_button_click('-'))
        op_fois = tk.Button(fen, text='x', command=lambda: self.on_button_click('*'))
        op_div = tk.Button(fen, text='/', command=lambda: self.on_button_click('/'))
        one = tk.Button(fen, text='1', command=lambda: self.on_button_click('1'))
        two = tk.Button(fen, text='2', command=lambda: self.on_button_click('2'))
        three = tk.Button(fen, text='3', command=lambda: self.on_button_click('3'))
        four = tk.Button(fen, text='4', command=lambda: self.on_button_click('4'))
        five = tk.Button(fen, text='5', command=lambda: self.on_button_click('5'))
        six = tk.Button(fen, text='6', command=lambda: self.on_button_click('6'))
        seven = tk.Button(fen, text='7', command=lambda: self.on_button_click('7'))
        eight = tk.Button(fen, text='8', command=lambda: self.on_button_click('8'))
        nine = tk.Button(fen, text='9', command=lambda: self.on_button_click('9'))
        zero = tk.Button(fen, text='0', command=lambda: self.on_button_click('0'))
        clear = tk.Button(fen, text='C', command=self.clear_display)
        equal = tk.Button(fen, text='=', command=self.calculate_result)
        decimal = tk.Button(fen, text='.', command=lambda: self.on_button_click('.'))
        history = tk.Button(fen, text='History', command=self.show_history)  # Bouton pour afficher l'historique
        
        one.grid(row=1, column=0, sticky='nsew')
        two.grid(row=1, column=1, sticky='nsew')
        three.grid(row=1, column=2, sticky='nsew')
        four.grid(row=1, column=3, sticky='nsew')
        five.grid(row=2, column=0, sticky='nsew')
        six.grid(row=2, column=1, sticky='nsew')
        seven.grid(row=2, column=2, sticky='nsew')
        eight.grid(row=2, column=3, sticky='nsew')
        nine.grid(row=3, column=0, sticky='nsew')
        zero.grid(row=3, column=1, sticky='nsew')
        decimal.grid(row=3, column=2, sticky='nsew')
        equal.grid(row=3, column=3, sticky='nsew')
        clear.grid(row=0, column=4, sticky='nsew')
        history.grid(row=0, column=5, sticky='nsew')
        op_plus.grid(row=1, column=4, sticky='nsew')
        op_div.grid(row=2, column=4, sticky='nsew')
        op_fois.grid(row=3, column=4, sticky='nsew')
        op_moins.grid(row=4, column=4, sticky='nsew')

        for i in range(5):
            fen.grid_rowconfigure(i, weight=1)
        for j in range(5):
            fen.grid_columnconfigure(j, weight=1)

    def display(self, fen):
        self.screen = tk.Entry(fen, textvariable=tk.StringVar(), border=4)
        self.screen.grid(row=0, column=0, columnspan=4, sticky='nsew')

    def on_button_click(self, char):
        self.current_expression += str(char)
        self.update_display()

    def update_display(self):
        self.screen.delete(0, tk.END)
        self.screen.insert(0, self.current_expression)

    def clear_display(self):
        self.current_expression = ""
        self.update_display()

    def calculate_result(self):
        try:
            result = str(eval(self.current_expression))
            self.current_expression = result
            self.history_list.append(self.current_expression)
        except Exception as e:
            self.current_expression = "Error"
        self.update_display()

    def show_history(self):
        if self.history_list:
            history_window = tk.Toplevel()
            history_window.title("History")
            history_window.geometry("300x200")
            history_text = tk.Text(history_window)
            history_text.pack(expand=True, fill='both')
            for expression in self.history_list:
                history_text.insert(tk.END, expression + '\n')
            history_text.config(state=tk.DISABLED)

calc = Calculator()
