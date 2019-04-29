import tkinter


class InfoGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.name_value = tkinter.StringVar()
        self.address_value = tkinter.StringVar()

        self.name_label = tkinter.Label(self.info_frame, textvariable = self.name_value)
        self.address_label = tkinter.Label(self.info_frame, textvariable = self.address_value)

        self.name_label.pack()
        self.address_label.pack()

        self.calc_button = tkinter.Button(self.button_frame, text = 'show info', command = self.show)
        self.quit_button = tkinter.Button(self.button_frame, text = 'quit', command = self.main_window.destroy)

        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.info_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def show(self):
        self.name_value.set('Brandon Langreck')
        self.address_value.set('4204 East Dr')


my_gui = InfoGUI()
