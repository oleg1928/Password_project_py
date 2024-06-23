# It supposed to create a password and update it in the .txt file
# when you open locked file, it will open GUI asking you for password, if right -> go, else close the menu
import os
import datetime
import time
from tkinter import *
import random
from time import sleep

class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath
    def was_file_opened_recently(self) -> bool:
        """
        Check if a file was opened within the last 'threshold_minutes' minutes.

        :param filepath: Path to the file
        :param threshold_minutes: Time threshold in minutes
        :return: True if the file was opened within the threshold, False otherwise
        """
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"The file {self.filepath} does not exist.")

        # Get the current time
        current_time = datetime.datetime.now()

        # Get the file's last access time
        last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(self.filepath))

        # Calculate the time difference in minutes
        time_difference = (current_time - last_access_time).total_seconds()
        # print(time_difference)
        # Check if the file was accessed within the second
        if time_difference < 10:
            return True
        return False

class ImplGUI:
    def __init__(self, passfile):
        self.passfile = passfile
        self.root = Tk()
        self.root.geometry("1640x1900")
        self.root.title("Password")
        self.set_gui()

    def set_gui(self):
        self.l = Label(text="What is the password?")
        self.inputtxt = Text(self.root, height=10,width=25,bg="light yellow")
        self.display = Button(self.root, height=2,width=20,text="Continue",command=lambda: self.Take_input())
        self.l.pack()
        self.inputtxt.pack()
        self.display.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind('<Unmap>', self.on_minimize)
        self.lock_position()
        self.root.resizable(False, False)
        self.root.mainloop()




    def Take_input(self):
        """time.sleep(5)
        open("C:/Users/Admin/OneDrive/Desktop/password.txt", "w").close()"""
        INPUT = self.inputtxt.get("1.0", "end-1c")
        with open(self.passfile, 'r') as file:
            saved_password = file.read().strip()
        # if input == password
        if (INPUT == password):
            print("Password is correct")
            self.root.destroy()






    def on_minimize(self, event):
        # Restore the window if it is minimized
        if self.root.state() == 'iconic':
            self.root.after(1, self.root.deiconify)

    def lock_position(self):
        # Continuously reset window position to (100, 100)
        x, y = 0, 0
        self.root.geometry(f"+{x}+{y}")
        self.root.after(100, self.lock_position)

    def on_closing(self):
        # Do nothing when trying to close the window
        pass


class Passw:
    def __init__(self, passfile):
        self.passfile = passfile

    # Creates a password
    def create_password(self):
        alphab = list(map(chr, range(97, 123)))
        high_alphab = list(map(chr, range(65, 90)))

        pasw = ""
        for i in range(16):
            num = random.randint(1, 3)
            # if num is 1 insert number
            if num == 1:
                pasw += str(random.randint(1,9))
            elif num == 2:
                pasw += alphab[random.randint(0, 25)]
            elif num == 3:
                pasw += high_alphab[random.randint(0, 24)]
        with open(self.passfile, "w") as file:
            file.write(pasw)
        print(pasw)

        return pasw

passfille = "C:/Users/Admin/OneDrive/Desktop/password.txt"



passmanager = Passw(passfille)
password = passmanager.create_password()
fileman = FileManager("C:/Users/Admin/OneDrive/Desktop/Novus me.docx")
if fileman.was_file_opened_recently() == True:
    ImplGUI(passfille)


