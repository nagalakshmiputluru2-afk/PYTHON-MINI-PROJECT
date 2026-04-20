from tkinter import *
import time

# create window
root = Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.resizable(False, False)

# function to update time
def update_time():
   current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# label to show time
clock_label = Label(
    root,
    font=("Arial", 50),
    background="black",
    foreground="cyan"
)
clock_label.pack(expand=True)

update_time()
root.mainloop()
