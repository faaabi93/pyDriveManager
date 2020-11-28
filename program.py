import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from os import listdir
from os.path import isfile, join
from shutil import copy
from tkinter.ttk import Progressbar


class Copy:
    def __init__(self, master):

        files=[]

        self.master = master
        self.frame1 = tk.Frame(self.master, width=100, height=100, bg="blue")
        self.frame1.pack(fill=tk.Y, side=tk.LEFT)

        self.frame2 = tk.Frame(self.master, width=500, bg="white")
        self.frame2.pack(fill=tk.Y, side=tk.LEFT)

        self.label1 = tk.Label(self.frame2, text="Select Source Folder")
        self.label1.grid(column=0, row=0)

        self.button1 = tk.Button(self.frame2, text="Select", width = 25, command = self.select_source)
        self.button1.grid(column=0, row=1)

        self.label2 = tk.Label(self.frame2, text="Select Target-Folder 1")
        self.label2.grid(column=0, row=2)

        self.button2 = tk.Button(self.frame2, text="Select", width= 25, command = self.set_target1)
        self.button2.grid(column=0, row=3)

        self.label3 = tk.Label(self.frame2, text="Select Target-Folder 2")
        self.label3.grid(column=0, row=4)

        self.button3 = tk.Button(self.frame2, text="Select", width= 25, command = self.set_target2)
        self.button3.grid(column=0, row=5)

        self.label4 = tk.Label(self.frame2, text="")
        self.label4.grid(column=0, row = 6)

        self.bar = Progressbar(self.frame2, length=500)
        self.bar2 = Progressbar(self.frame2, length=500)
        self.bar["value"] = 0
        self.bar2["value"] = 0
        self.bar.grid(column=0, row=7)
        self.bar2.grid(column=0, row=8)

        self.button4 = tk.Button(self.frame2, text="Start Copying", width= 25, command = self.copy_command)
        self.button4.grid(column=0, row=9)

    def select_source(self):
        global files
        global num_files
        filepath = askdirectory()
        files = [join(filepath, f) for f in listdir(filepath) if isfile(join(filepath, f))]
        self.label1.configure(text="Source: " + filepath)
        num_files = len(files)

    def set_target1(self):
        global target1
        target1 = askdirectory()
        self.label2.configure(text="Source: " + filepath)
    
    def set_target2(self):
        global target2
        target2 = askdirectory()
        self.label3.configure(text="Source: " + filepath)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def copy_command(self):
        increment = 100/num_files
        for file in files:
            file_name = file.rsplit("/", 1)[-1]
            file_name_stripped = file_name.rsplit(".", 1)[0]
            data_type = file_name.rsplit(".",1)[-1]
            self.label4.configure(text=file_name)
            self.bar["value"] = 25
            self.bar.update()
            if file_name not in listdir(target1):
                copy(file, target1)
            else:
                alt_target1 = target1 +"/"+ file_name_stripped + "_new." + data_type
                copy(file, alt_target1)
            self.bar["value"] = 50
            self.bar.update()
            if file_name not in listdir(target2):
                copy(file, target2)
            else:
                alt_target2 = target2 +"/"+ file_name_stripped + "_new." + data_type
                copy(file, alt_target2)
            self.bar["value"] = 75
            self.bar2["value"] += increment
            self.bar.update()
        self.label4.configure(text="All files copied")
        self.bar["value"] = 100
        self.bar.update()




def main(): 
    root = tk.Tk()
    root.geometry("600x400")
    root.resizable(width=False, height=False)
    app = Copy(root)
    root.mainloop()

if __name__ == '__main__':
    main()