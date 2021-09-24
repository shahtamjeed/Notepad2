from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


if __name__ == '__main__':
    #Tkinter Setup
    root= Tk()
    #root.configure(background="black")
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("n.ico")
    root.geometry("700x800")

# Meathods
    #New File
    def newFile():
        global file
        root.title("New Untitled - Notepad")
        file= None
        TextArea.delete(1.0,END)

    def fileAbout():
        showinfo("Notepad","Develop by Rise India \nVersion-1.01\nLaunch Date:-Jan 29,2021")
    def openFile():
        global file
        file= askopenfilename(defaultextension=".txt",filetypes=[("All Files","."),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            root.title(os.path.basename(file) + "- Notepad")
            TextArea.delete(1.0,END)
            f= open(file,"r")
            TextArea.insert(1.0,f.read())
            f.close()

    def saveFile():
        global file
        if file== None:
            file=asksaveasfilename(initialfile="Untitled.txt", defultextension=".txt",filetype=[("All Files","*.*"),("Text Documents","*.txt")])
            if file=="":
                file=None
            else:
                # Save as new file
                f=open(file,"w")
                f.write(TextArea.get(1.0,END))
                f.close()

                root.title(os.path.basename(file) +"-Notepad")
                print("FIle Save")
        else:
            #Save the file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

    def quitApp():
        root.destroy()
    def copy():
        TextArea.event_generate(("<<Copy>>"))
    def cut():
        TextArea.event_generate(("<<Cut>>"))
    def paste():
        TextArea.event_generate(("<<Paste>>"))
    def wordWrap():
        pass
    def font():
        pass
    def noteHelp():
        showerror("Notepad","Sorry No data Available")
    def developer():
        showinfo("Notepad","Develop by Rise India \nE-mail us: shahtamjeed@gmail.com")

###################### Text Area--------------------------
    # text Area
    TextArea= Text(root, font=("times new roman",14))
    file=None
    TextArea.pack(expand=True,fill=BOTH)

######################Menu Bar--------------------------
    MenuBar=Menu(root)
    FileMenu= Menu(MenuBar, tearoff=0)
    EditMenu= Menu(MenuBar, tearoff=0)
    FormatMenu= Menu(MenuBar,tearoff=0)
    HelpMenu= Menu(MenuBar,tearoff=0)
    AboutMenu= Menu(MenuBar,tearoff=0)


###################### File Menu--------------------------

    # to open New File
    FileMenu.add_command(label="New", command=newFile)

    # To open exisitence file
    FileMenu.add_command(label="Open",command=openFile)

    # to save the current file
    FileMenu.add_command(label="Save",command=saveFile)

    #To add line
    FileMenu.add_separator()
    # To quit notepad
    FileMenu.add_command(label="Exit",command=quitApp)

###################### Edit Menu--------------------------
    # To copy
    EditMenu.add_command(label="Copy", command=copy)
    # To cut
    EditMenu.add_command(label="Cut", command=cut)
    # To paste
    EditMenu.add_command(label="Paste", command=paste)

###################### Format Menu--------------------------
    FormatMenu.add_command(label="Word Wrap",command=wordWrap)
    FormatMenu.add_command(label="Font",command=font)

###################### Help Menu--------------------------
    HelpMenu.add_command(label="Help",command=noteHelp)
    HelpMenu.add_command(label="Contact Developer",command=developer)

###################### Help Menu--------------------------
    AboutMenu.add_command(label="Info",command=fileAbout)

    #Cascade
    MenuBar.add_cascade(label="File",menu=FileMenu)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    MenuBar.add_cascade(label="Format",menu=FormatMenu)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    MenuBar.add_cascade(label="About",menu=AboutMenu)



    root.config(menu=MenuBar)

###################### Scroll Bar--------------------------
    ScrollY=Scrollbar(TextArea)
    ScrollY.pack(side=RIGHT,fill=Y)
    ScrollY.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollY.set)




    root.mainloop()
