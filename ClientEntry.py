# ClientEntry.py

# Import utilities
#   
import tkinter as tk            # you can access tkinter function using the abreviation tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creates the window called root
root = tk.Tk()                  # creates a window instance called root.  you used the tk set above instead of tkinter.Tk()
root.geometry('300x220')        # Initial size of window root
root.resizable(True, True)      # Allows to resize horiz, vert
root.title('Client Entry')      # Frame (window) title


# This runs the main window
root.mainloop()