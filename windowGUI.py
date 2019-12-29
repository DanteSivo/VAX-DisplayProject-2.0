from tkinter import *
# Let's create the Tkinter window.
window = Tk()
window.title("GUI")
window.geometry("800x480")
window.config(bg = '#024889')

photo = PhotoImage(file="images\sprocket150.png")
w = Label(window, image=photo, bg = '#024889')
w.photo = photo

eventLabel = Label(window,text=("Marvel Mondays! - Endgame"))
timeLabel = Label(window,text="Event time here")

eventLabel.config(font=("Courier", 26), fg='#fcd200', bg = '#024889')
timeLabel.config(font=("Courier", 20), fg='#fcd200', bg = '#024889')

#w.grid(row=0, column=0, sticky=N+W, pady=25, padx = 25)
w.place(x=30, y=30)
eventLabel.place(x=400,y=225, anchor="center")
timeLabel.place(x=400,y=275, anchor="center")


mainloop()