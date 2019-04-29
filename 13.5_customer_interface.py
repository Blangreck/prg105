import tkinter


class IceCreamShopGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Ice cream Creator')
        self.main_window.geometry('400x400')

        self.top_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.instl = tkinter.Label(self.top_frame, text = 'First select the base flavor that you would like: ')
        self.vanilla = tkinter.Radiobutton(self.top_frame, text = 'Vanilla ($3.00', variable = self.radio_var, value = 1)
        self.chocolate = tkinter.Radiobutton(self.top_frame, text = 'Chocolate ($3.00', variable = self.radio_var, value = 2)
        self.strawberry = tkinter.Radiobutton(self.top_frame, text = 'Strawberry ($2.50', variable = self.radio_var, value = 3)
        self.cookie = tkinter.Radiobutton(self.top_frame, text = 'Cookies and Cream ($3.50', variable = self.radio_var, value = 4)

        self.inst2 = tkinter.Label(self.top_frame, text = 'Then select any toppings: ')

        self.sprinkles_var = tkinter.IntVar()
        self.sprinkles_var.set(0)
        self.sprinkles = tkinter.Checkbutton(self.top_frame, text = 'Sprinkles ($0.50)', variable = self.sprinkles_var)

        self.chips_var = tkinter.IntVar()
        self.chips_var.set(0)
        self.chips = tkinter.Checkbutton(self.top_frame, text = 'Chocolate Chips ($1.00)', variable = self.chips_var)

        self.fudge_var = tkinter.IntVar()
        self.fudge_var.set(0)
        self.fudge = tkinter.Checkbutton(self.top_frame, text = 'Hot Fudge ($1.50)', variable = self.fudge_var)

        self.caramel_var = tkinter.IntVar()
        self.caramel_var.set(0)
        self.caramel = tkinter.Checkbutton(self.top_frame, text = 'Caramel Syrup ($1.50)', variable = self.caramel_var)

        self.dough_var = tkinter.IntVar()
        self.dough_var.set(0)
        self.dough = tkinter.Checkbutton(self.top_frame, text = 'Cookie Dough ($1.50)', variable = self.dough_var)

        self.fudge_var = tkinter.IntVar()
        self.fudge_var.set(0)
        self.fudge = tkinter.Checkbutton(self.top_frame, text = 'Hot Fudge ($1.50', variable = self.fudge_var)

        self.scoop_var = tkinter.IntVar()
        self.scoop_var.set(0)
        self.scoop = tkinter.Checkbutton(self.top_frame, text = 'Extra Scoop ($1.50)', variable = self.scoop_var)

        self.instl.pack()
        self.vanilla.pack(ancho = 'w')
        self.chocolate.pack(anchor = 'w')
        self.strawberry.pack(anchor = 'w')
        self.cookie.pack(anchor = 'w')

        self.inst2.pack()

        self.sprinkles.pack(anchor = 'w')
        self.chips.pack(anchor = 'w')
        self.fudge.pack(anchor = 'w')
        self.caramel.pack(anchor = 'w')
        self.dough.pack(anchor = 'w')
        self.scoop.pack(anchor = 'w')

        self.drink_cost = tkinter.StringVar()
        self.cost_label = tkinter.Label(self.button_frame, textvariale = self.drink_cost)
        self.inst3 = tkinter.Label(self.button_frame, text = "Finally click 'Calculate Order' to get the total cost: ")
        self.calc_button = tkinter.Button(self.button_frame, text = 'Calculate Order', command = self.calc_menu)
        self.quit_button = tkinter.Button(self.button_frame, text = 'Quit', command = self.main_window.destroy)

        self.inst3.pack()
        self.cost_label.pack()
        self.calc_button.pack(side = 'left', padx = 3, pady = 3)
        self.quit_button.pack(side = 'right')

        self.top_frame.pack(padx = 10, pady = 10)
        self.button_frame.pack()

        tkinter.mainloop()





