import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from os import listdir
from os.path import isfile, join
from shutil import copy
from tkinter.ttk import Progressbar


window = tk.Tk()
window.geometry("600x300")
window.resizable(width=False, height=False)

frame1 = tk.Frame(master=window, width=100, height=100, bg="blue")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=500, bg="white")
frame2.pack(fill=tk.Y, side=tk.LEFT)

def clicked():
    global files
    global num_files
    filepath = askdirectory(
    )
    imgdirlbl.configure(text="Path: " + filepath)
    onlyfiles = [join(filepath, f) for f in listdir(filepath) if isfile(join(filepath, f))]
    files = onlyfiles
    num_files = len(onlyfiles)
    print(num_files)

def clicked2():
    global tgtdir1
    filepath = askdirectory(
    )
    targetdir1lbl.configure(text="Path: " + filepath)
    tgtdir1 = filepath

def clicked3():
    global tgtdir2
    filepath = askdirectory(
    )
    targetdir2lbl.configure(text="Path: " + filepath)
    tgtdir2 = filepath

def copy_command():
    increment = 100/num_files
    global button_active
    button_active = Flase
    print(increment)
    for file in files:
        currentfilelbl.configure(text=file)
        bar['value'] =33
        window.update()
        file_name = file.rsplit("/", 1)[-1]
        print(file_name)
        if file_name not in listdir(tgtdir1):
            copy(file, tgtdir1)
        else:
            file_name_striped = file_name.rsplit(".", 1)[0]
            print(file_name_striped)
            data_type = file_name.rsplit(".",1)[-1]
            print(data_type)
            alt_tgtdir1 = tgtdir1 +"/"+ file_name_striped + "_new." + data_type
            print(alt_tgtdir1)
            copy(file, alt_tgtdir1)
        bar['value'] = 66
        window.update()
        #copy(file, tgtdir2)
        bar['value'] = 0
        bar2["value"] += increment
        window.update()
    currentfilelbl.configure(text="All files copied")
    bar["value"] = 100
    button_active = True


imgdirlbl = tk.Label(frame2, text="Imgdir")
targetdir1lbl = tk.Label(frame2, text="Targetdir1")
targetdir2lbl = tk.Label(frame2, text="Targetdir2")
currentfilelbl = tk.Label(frame2, text="")

bar = Progressbar(frame2, length=400)
bar2 = Progressbar(frame2, length=400)
bar['value'] = 0
bar2['value'] = 0

button_1 = PhotoImage(file = "/Users/fabian.baiersdoerfer/pyDriveManager/pyDriveManager/button.png")

imgdir = tk.Button(frame2, text="Select", command=clicked)
targetdir1 = tk.Button(frame2, text="Select", command=clicked2)
targetdir2 = tk.Button(frame2, text="Select", command=clicked3)
button = tk.Button(frame2, image = button_1, command=copy_command)

imgdirlbl.grid(column=0, row=0)
imgdir.grid(column=0, row=1)
targetdir1.grid(column=0, row=3)
targetdir1lbl.grid(column=0, row=2)
targetdir2.grid(column=0, row=5)
targetdir2lbl.grid(column=0, row=4)
button.grid(column=0, row=6)
currentfilelbl.grid(column=0, row=7)
bar.grid(column=0, row=8)
bar2.grid(column=0, row=9)


window.mainloop()