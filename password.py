# It supposed to create a password and update it in the .txt file
# when you open locked file, it will open GUI asking you for password, if right -> go, else close the menu
import os
import datetime
import time
from tkinter import *
import random
import keyboard

class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath
    def was_file_opened_recently(self) -> bool:
        """
        Check if a file was opened within the last 'threshold_minutes' minutes.


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
        if time_difference < 4:
            return True
        return False

class ImplGUI:
    def __init__(self, passfile):
        self.passfile = passfile
        self.root = Tk()
        self.root.geometry("1600x1900")
        self.root.title("Password")
        self.root.configure(bg="gray23")
        self.set_gui()

    def set_gui(self):
        font_settings = ("Helvetica", 14)

        self.l = Label(self.root, text="What is the password?", font=font_settings, fg="white", bg="gray23")
        self.l.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.inputtxt = Text(self.root, height=1, width=25, bg="light yellow", font=font_settings, fg="black")
        self.inputtxt.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.display = Button(self.root, height=2, width=14, text="Try", font=font_settings,
                              command=lambda: self.Take_input(), bg="white")
        self.display.place(relx=0.5, rely=0.62, anchor=S)


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind('<Unmap>', self.on_minimize)
        self.lock_position()
        self.root.attributes('-topmost', True)
        self.root.resizable(False, False)
        self.root.mainloop()





    def Take_input(self):
        """time.sleep(5)
        open("C:/Users/Admin/OneDrive/Desktop/password.txt", "w").close()"""
        INPUT = self.inputtxt.get("1.0", "end-1c")
        with open(self.passfile, 'r') as file:
            saved_password = file.read().strip()
        # if input == password
        if (INPUT == saved_password):
            print("Password is correct")
            self.root.destroy()
        else:
            self.Take_input()







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

        return pasw

def main():
    passfile = "C:/Users/Admin/OneDrive/Desktop/password.txt"
    filepath = "C:/Users/Admin/OneDrive/Desktop/Novus me.docx"
    fileman = FileManager(filepath)


    while True:
        keyboard.block_key('Win')
        if fileman.was_file_opened_recently():
            passmanager = Passw(passfile)
            password = passmanager.create_password()
            time.sleep(1)
            ImplGUI(passfile)
            time.sleep(1200)
        # Check every 5 seconds
        time.sleep(3)


if __name__ == "__main__":
    main()


