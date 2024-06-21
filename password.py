# It supposed to create a password and update it in the .txt file
# when you open locked file, it will open GUI asking you for password, if right -> go, else close the menu
import os
import datetime
from tkinter import *


def was_file_opened_recently(filepath) -> bool:
    """
    Check if a file was opened within the last 'threshold_minutes' minutes.

    :param filepath: Path to the file
    :param threshold_minutes: Time threshold in minutes
    :return: True if the file was opened within the threshold, False otherwise
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")

    # Get the current time
    current_time = datetime.datetime.now()

    # Get the file's last access time
    last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(filepath))

    # Calculate the time difference in minutes
    time_difference = (current_time - last_access_time).total_seconds()
    print(time_difference)
    # Check if the file was accessed within the threshold
    if time_difference < 1:
        return True
    return False


# Implementing GUI
root = Tk()
root.geometry("1640x1900")
root.title("Password")


def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    # if input == password
    if (INPUT == "120"):
        pass


l = Label(text="What is the password?")
inputtxt = Text(root, height=10,
                width=25,
                bg="light yellow")

Display = Button(root, height=2,
                 width=20,
                 text="Continue",
                 command=lambda: Take_input())

l.pack()
inputtxt.pack()
Display.pack()

def on_minimize(event):
    # Restore the window if it is minimized
    if root.state() == 'iconic':
        root.after(1, root.deiconify)

def lock_position():
    # Continuously reset window position to (100, 100)
    x, y = 0, 0
    root.geometry(f"+{x}+{y}")
    root.after(100, lock_position)

def on_closing():
    # Do nothing when trying to close the window
    pass
root.protocol("WM_DELETE_WINDOW", on_closing)

root.bind('<Unmap>', on_minimize)

lock_position()

root.resizable(False, False)

mainloop()
print("hello")  # this is here for no reason

"""if was_file_opened_recently("C:/Users/Admin/OneDrive/Desktop/Novus me.docx") == True:
    
"""
