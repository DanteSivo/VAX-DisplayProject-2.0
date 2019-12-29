from tkinter import *
# Let's create the Tkinter window.
window = Tk()
window.title("GUI")
window.geometry("800x480")
window.config(bg = '#024889')

eventLabel = Label(window,text=("Event name here"),anchor= 's', height = 10) #set your text
timeLabel = Label(window,text="Event time here",anchor= 'n', height = 10, pady = 17.5) #set your text
eventLabel.pack()
timeLabel.pack()

eventLabel.config(font=("Courier", 20), fg='#fcd200')
timeLabel.config(font=("Courier", 20), fg='#fcd200' )

mainloop()