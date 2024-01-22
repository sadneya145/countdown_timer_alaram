from tkinter import *
from playsound import playsound
import time

def update_clock():
    current_time_str = time.strftime('%I:%M:%S %p')
    current_time.config(text=current_time_str)
    current_time.after(1000, update_clock)

def start_timer():
    # Get the values from the Spinboxes
    hours = int(hours_var.get())
    minutes = int(minutes_var.get())
    seconds = int(seconds_var.get())

    # Convert everything to seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Start the countdown
    countdown(total_seconds)

def countdown(seconds):
    if seconds > 0:
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)

        seconds_var.set("{:02d}".format(second))
        minutes_var.set("{:02d}".format(minute))
        hours_var.set("{:02d}".format(hour))

        root.after(1000, countdown, seconds - 1)
    else:
        playsound("ringtone.mp3")
        seconds_var.set("00")
        minutes_var.set("00")
        hours_var.set("00")

# GUI setup
root = Tk()
root.title("Timer")
root.geometry("400x400")
root.config(bg="#000")

# Clock
current_time = Label(root, font=("arial", 15, "bold"), text="", fg="#fff", bg="#000")
current_time.pack(pady=10)
update_clock()

# Timer input
Label(root, text="Set Timer:", font="arial 15 bold", bg="#000", fg="#fff").pack(pady=10)

hours_var = IntVar()
Spinbox(root, textvariable=hours_var, from_=0, to=23, width=2, font="arial 20", bg="#000", fg="#fff", bd=0).pack(side=LEFT)
Label(root, text="hours", font="arial 12", bg="#000", fg="#fff").pack(side=LEFT)

minutes_var = IntVar()
Spinbox(root, textvariable=minutes_var, from_=0, to=59, width=2, font="arial 20", bg="#000", fg="#fff", bd=0).pack(side=LEFT)
Label(root, text="min", font="arial 12", bg="#000", fg="#fff").pack(side=LEFT)

seconds_var = IntVar()
Spinbox(root, textvariable=seconds_var, from_=0, to=59, width=2, font="arial 20", bg="#000", fg="#fff", bd=0).pack(side=LEFT)
Label(root, text="sec", font="arial 12", bg="#000", fg="#fff").pack(side=LEFT)

Button(root, text="Start Timer", command=start_timer, bg="#ea3548", bd=0, fg="#fff", font="arial 10 bold").pack(pady=20)

# Main loop
root.mainloop()
