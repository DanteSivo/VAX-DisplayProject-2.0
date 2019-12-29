from tkinter import *
# Let's create the Tkinter window.
window = Tk()
window.title("GUI")
window.geometry("800x480")

label = Label(window,text=("Event name here"),anchor= 's', height = 13) #set your text
label.pack()
labels.append(label) #appends the label to the list for further use

label2 = Label(window,text="Event time here",anchor= 'n', height = 13) #set your text
label2.pack()
labels.append(label2) #appends the label to the list for further use

mainloop()