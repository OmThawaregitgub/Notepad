import tkinter as tk
from tkinter import ttk
import os

class Notpad:
    def __init__(self):
        self.tab_count = 1
        self.root = tk.Tk()
        self.root.title(os.getcwd())
        self.root.geometry("600x400")
        # self.root.resizable(False,False)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill="both")
        self.AddingTab()

    def menu(self):
        menubar = tk.Menu(self.root) 

        file = tk.Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='File', menu = file) 
        file.add_command(label ='Open New Tab', command = self.AddingTab) 
        file.add_command(label ='New File', command = None) 
        file.add_command(label ='Open...', command = None) 
        file.add_command(label ='Save', command = None) 
        file.add_separator() 
        file.add_command(label ='Exit', command = self.root.destroy) 

        edit = tk.Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Edit', menu = edit) 
        edit.add_command(label ='Cut', command = None) 
        edit.add_command(label ='Copy', command = None) 
        edit.add_command(label ='Paste', command = None) 
        edit.add_command(label ='Select All', command = None) 
        edit.add_separator() 
        edit.add_command(label ='Find...', command = None) 
        edit.add_command(label ='Find again', command = None) 

        help_ = tk.Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Help', menu = help_) 
        help_.add_command(label ='Tk Help', command = None) 
        help_.add_command(label ='Demo', command = None) 
        help_.add_separator() 
        help_.add_command(label ='About Tk', command = None) 

        self.root.config(menu = menubar) 
        
    def AddingTab(self):
        self.frames = ttk.Frame(self.notebook)
        self.notebook.add(self.frames, text=f"Tab {self.tab_count}")
        self.text_area = tk.Text(self.frames, wrap="word", width=40, height=15)
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)
        self.tab_count += 1
        



    def main(self):    
        self.root.mainloop() 

if __name__ == "__main__":
    n = Notpad()
    n.menu()
    n.main()
        