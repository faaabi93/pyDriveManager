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



        #self.frame1 = tk.Frame(self.master, width=100, height=100, bg="lightgrey")
        #self.frame1.pack(fill=tk.Y, side=tk.LEFT)

        self.frame2 = tk.Frame(self.master, width=600, bg="white")
        self.frame2.pack(fill=tk.Y, side=tk.LEFT)
        #base64 encode:
        #with open("/Users/fabian.baiersdoerfer/pyDriveManager/pyDriveManager/button.png", "rb") as img_file:
        #...     my_string=base64.b64encode(img_file.read())
        base64 = b'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'
        self.filename = PhotoImage(data=base64, master=master)
        self.background_label = Label(self.frame2, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.label1 = tk.Label(self.frame2, text="Select Source Folder")
        self.label1.grid(column=0, row=0, pady=5)

        self.button1 = tk.Button(self.frame2, text="Select", width = 25, command = self.select_source)
        self.button1.grid(column=0, row=1, pady=3)
        #self.img = tk.PhotoImage(file="/Users/fabian.baiersdoerfer/pyDriveManager/pyDriveManager/button.png", master=master)
        #self.button1.config(image=self.img, compound=tk.RIGHT)


        self.label2 = tk.Label(self.frame2, text="Select Target-Folder 1")
        self.label2.grid(column=0, row=2, pady=10)

        self.button2 = tk.Button(self.frame2, text="Select", width= 25, command = self.set_target1)
        self.button2.grid(column=0, row=3, pady=3)

        self.label3 = tk.Label(self.frame2, text="Select Target-Folder 2")
        self.label3.grid(column=0, row=4, pady=10)

        self.button3 = tk.Button(self.frame2, text="Select", width= 25, command = self.set_target2)
        self.button3.grid(column=0, row=5, pady=5)

        self.label4 = tk.Label(self.frame2, text="")
        self.label4.grid(column=0, row = 6, pady=10)



        self.bar = Progressbar(self.frame2, length=600)
        self.bar2 = Progressbar(self.frame2, length=500)
        self.bar["value"] = 0
        self.bar2["value"] = 0
        self.bar.grid(column=0, row=7, pady=12)
        self.bar2.grid(column=0, row=8)

        self.button4 = tk.Button(self.frame2, text="Start Copying", width= 25, command = self.copy_command)
        self.button4.grid(column=0, row=9, pady=5)

    def select_source(self):
        global files
        global num_files
        global filepath
        filepath = askdirectory()
        files = [join(filepath, f) for f in listdir(filepath) if isfile(join(filepath, f))]
        self.label1.configure(text="Source: " + filepath, fg="black")
        num_files = len(files)

    def set_target1(self):
        global target1
        target1 = askdirectory()
        if target1 == filepath:
            self.button4["state"] = "disabled"
            self.label2.configure(text="Directory {} already selected".format(target1), fg="red")
        elif target1:
            self.label2.configure(text="Source: " + target1, fg="black")
        else:
            self.label2.configure(text="Select Folder 1", fg="black")
    
    def set_target2(self):
        global target2
        target2 = askdirectory()
        if target2 == filepath or target2 == target1:
            self.button4["state"] = "disabled"
            self.label3.configure(text="Directory {} already selected".format(target2), fg="red")
        elif target1:
            self.label3.configure(text="Source: " + target2, fg="black")
        else:
            self.label3.configure(text="Select Folder 2", fg="black")

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def copy_command(self):
        self.button4["state"] = "disabled"
        increment = 100/num_files
        for file in files:
            self.bar["value"] = 100
            self.bar.update()
            file_name = file.rsplit("/", 1)[-1]
            file_name_stripped = file_name.rsplit(".", 1)[0]
            data_type = file_name.rsplit(".",1)[-1]
            self.label4.configure(text=file_name)
            if file_name not in listdir(target1):
                copy(file, target1)
            else:
                alt_target1 = target1 +"/"+ file_name_stripped + "_new." + data_type
                copy(file, alt_target1)
            self.bar["value"] = 33
            self.bar.update()
            if file_name not in listdir(target2):
                copy(file, target2)
            else:
                alt_target2 = target2 +"/"+ file_name_stripped + "_new." + data_type
                copy(file, alt_target2)
            self.bar["value"] = 66
            self.bar2["value"] += increment
            self.bar.update()
        self.label4.configure(text="All files copied")
        self.bar["value"] = 100
        self.bar.update()
        self.button4["state"] = "normal"




def main(): 
    root = tk.Tk(className="pyCopy")
    root.geometry("600x400")
    root.resizable(width=False, height=False)
    app = Copy(root)
    root.mainloop()

if __name__ == '__main__':
    main()