import tkinter as tk 
from sys_stats import *

#Intializing the screen with  title and specific dimensions

win = tk.Tk()
win.title("task manager clone".title())
win.geometry("800x600")

win.update()

win_height,win_width = win.winfo_height(),win.winfo_width()


def quit_window(event): 

   win.destroy()
   print("\033[31m Tkinter GUI window exited due to the exit q key being pressed.\033[0m\n")



win.bind("q",quit_window)
win.mainloop()
