import tkinter


class MPGGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid1_frame = tkinter.Frame()
        self.mid2_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.gallons_label = tkinter.Label(self.top_frame, text='Enter how many gallons your car holds:')
        self.gallon_entry = tkinter.Entry(self.top_frame, width=10)

        self.gallons_label.pack(side='left')
        self.gallon_entry.pack(side='left')

        self.miles_label = tkinter.Label(self.mid1_frame, text='How many miles have you traveled?')
        self.miles_entry = tkinter.Entry(self.mid1_frame, width=10)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid2_frame, text='Miles per Gallon:')

        self.value = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mid2_frame, textvariable=self.value)

        self.descr_label.pack(side='left')
        self.mpg_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid1_frame.pack()
        self.mid2_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        gallons = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles / gallons
        mpg = format(mpg, '.2f')
        self.value.set(mpg)


kilo_conv = MPGGUI()
