from tkinter import *
from tkinter.filedialog import askopenfilename
import sys
import os
import tkinter
from mainCode import * 

def save_info():
    DeviceName_info = Device.get()
    Description_info = Description.get()
    Version_info = c.get()
    #print(DeviceName_info, Description_info)

    file1 = open("logs1.txt", "w")
    space = str("\n")
    file1.write("Device Name  :" + DeviceName_info )
    file1.write(space)
    file1.write("Description  :" + Description_info)
    file1.write(space)
    file1.write("Version  :" + Version_info)
    file1.write(space)
    file1.close()
   
    filenames = ['logs1.txt','result.txt']
    outfile =  open('log.txt', 'w')
    for fname in filenames:
            infile =  open(fname)
            outfile.write(infile.read())
    outfile.close()
            

    #Device_entry.delete(0, END)
    #Description_entry.delete(0, END)

def call_back():
   os.system('python3 Process.py %s' % PATHFILE)


def inputfile():
    global PATHFILE
    PATHFILE = askopenfilename()

    


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x500')
    root.title("UnPass v1.0")

    Header = Label(root, text="Gathering Information",width=20,font=("bold", 20))
    Header.place(x=90,y=53)
   

    #Device
    Device = Label(root, text="Device Name",width=20,font=("bold", 10))
    Device.place(x=80,y=130)
    Device = StringVar()
    Device_entry = Entry(textvariable=Device)#### textvariable merupakan variable untuk input
    Device_entry.place(x=240,y=130)

    #Description
    Description = Label(root, text="Description",width=20,font=("bold", 10))
    Description.place(x=68,y=180)
    Description = StringVar()
    Description_entry = Entry(textvariable=Description) ###
    Description_entry.place(x=240,y=180)

    #Version
    Version = Label(root, text="Version",width=20,font=("bold", 10))
    Version.place(x=70,y=230)

    list1 = ['Kitkat','Lolipop','Marshmellow'];
    c=StringVar()
    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=15)
    c.set('select your version') 
    droplist.place(x=240,y=230)

    #Button
    
   
    Button(root, text='Input File', width=20, bg='orange', fg='white', command=inputfile).place(x=180,y=300)
    Button(root, text='Hack', width=20, bg='green', fg='white', command=call_back).place(x=180,y=330)
    Button(root, text='PrintInfo',width=20,bg='blue',fg='white',command=save_info).place(x=180,y=360)
    Button(root, text='Quit', width=20, bg='red', fg='white', command=root.quit).place(x=180,y=390)


    root.mainloop()
