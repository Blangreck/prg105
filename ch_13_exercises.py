"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)


# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2

class MyGUI2():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Kylie Costello')
        self.label.pack()

        tkinter.mainloop()


# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

sampleGUI1 = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)


# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3

class MyGUI3():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Kylie Costello')
        self.label2 = tkinter.Label(self.top_frame, text='Associates in General Education')
        self.label3 = tkinter.Label(self.bottom_frame, text='PRG 105')
        self.label4 = tkinter.Label(self.bottom_frame, text='WEB 105')
        self.label5 = tkinter.Label(self.bottom_frame, text='BIO 157')
        self.label6 = tkinter.Label(self.bottom_frame, text='HFE 120')

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='left')
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI

import tkinter.messagebox


class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(text='What did the pig say at the beach on a hot summers day?')
        self.button = tkinter.Button(self.main_window, text='IDK Y', command=self.wakkaWakka)

        self.label1.pack(side='top')
        self.button.pack(side='top')

        tkinter.mainloop()

    def wakkaWakka(self):
        tkinter.messagebox.showinfo('Answer', 'I\'m Bakin!')


fozzi = MyGUI4()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)


# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters

class MyGUI5:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a measurement in inches: ')
        self.inch_entry = tkinter.Entry(self.top_frame, width=20)

        self.prompt_label.pack(side='left')
        self.inch_entry.pack(side='left')

        self.value = tkinter.StringVar()

        self.descript_label = tkinter.Label(self.mid_frame, text='Converted to centimeters: ')
        self.centi_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        self.descript_label.pack(side='left')
        self.centi_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        inch = float(self.inch_entry.get())
        centi = inch * 2.54
        self.value.set(centi)

        # tkinter.messagebox.showinfo('Results', str(inch) + ' inches is equal to ' + str(centi) + ' Centimeters.')


inches = MyGUI5()
