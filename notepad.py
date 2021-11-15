from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f = open(file, "r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitles.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file =="":
            file = None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+" - Notepad")
    
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()



def quitApp():
    root.destroy()

def FileMenu():
    pass

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Title","Notepad by Biswambhar")





if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("icon_file.ico")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root,font="times 15")
    file = None
    TextArea.pack(expand=True,fill=BOTH)
    ##~~~~~~~~~~~lets create a menubar~~~~~~~~~##
    Menubar = Menu(root)
    ##------File Menu Starts------##
    FileMenu = Menu(Menubar,tearoff=0)
    #To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already exixting file
    FileMenu.add_command(label = "Open", command = openFile)

    #To save the current file
    FileMenu.add_command(label = "Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label = "File",menu = FileMenu)
    #File Menu Ends#

    ##------Edit Menu Starts------##
    EditMenu = Menu(Menubar,tearoff=0)
    #TO Give a menu of cut,copy,paste
    EditMenu.add_command(label="cut",command = cut)
    EditMenu.add_command(label="copy",command = copy)
    EditMenu.add_command(label="paste",command = paste)
    
    Menubar.add_cascade(label = "Edit",menu = EditMenu)
    #File Menu Ends#

    ##------Help Menu Starts------##
    HelpMenu = Menu(Menubar,tearoff=0)
    #TO Give a menu of cut,copy,paste
    HelpMenu.add_command(label="About Notepad",command = about)
    
    Menubar.add_cascade(label = "Help",menu = HelpMenu)
    #Help Menu Ends#
    root.config(menu=Menubar)

    #Adding Scrollbar
    Scroll= Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()