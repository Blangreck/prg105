import tkinter
import random

class NumberGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid1_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text = 'Choose a number at random: ')
        self.num_entry = tkinter.Entry(self.top_frame, width = 10)

        #Top Frame
        self.prompt_label.pack(side = 'left')
        self.num_entry.pack(side = 'left')

        #Middle Frame
        self.value = tkinter.StringVar()
        self.response_label = tkinter.Label(self.mid1_frame, textvariable = self.value)

        self.response_label.pack(side = 'left')

        #Bottom Frame
        self.continue_button = tkinter.Button(self.bottom_frame, text = 'Continue', command = self.response)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        self.continue_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #Pack Frames
        self.top_frame.pack()
        self.mid1_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def response(self):
        try:
            number = int(self.num_entry.get())
            if int(number) == 69:
                self.value.set("Nice...")
            elif int(number) == 21:
                self.value.set("9 + 10")
            elif int(number) == 8675309:
                self.value.set("Hey, this is Jenny")
            elif int(number) == 300:
                self.value.set("This is SPARTA!!!")
            elif int(number) == 2:
                self.value.set("Gotta take a #2?")
            elif int(number) == 25:
                self.value.set("I get it, its funnier than 24...")
            elif int(number) == 23:
                self.value.set("MJ BABY!!")
            else:
                num = random.randint(1,3)
                if num == 1:
                    self.value.set("That's a good number.")
                elif num == 2:
                    self.value.set("That number is pretty decent.")
                elif num == 3:
                    self.value.set("That number is just extraordinary.")
        except ValueError:
            self.value.set("That's not a number, silly.")

num_gui = NumberGUI()
