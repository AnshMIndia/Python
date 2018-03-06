from tkinter import *
root = Tk()

def Nothing():
    pass

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=Nothing)
filemenu.add_command(label="Open...", command=Nothing)
filemenu.add_command(label="Save", command=Nothing)
filemenu.add_command(label="Save As...", command=Nothing)
filemenu.add_separator()
filemenu.add_command(label="Page Setup...", command=Nothing)
filemenu.add_command(label="Print...", command=Nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label=" File ", menu=filemenu)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Undo", command=Nothing)
filemenu.add_separator()
filemenu.add_command(label="Cut", command=Nothing)
filemenu.add_command(label="Copy", command=Nothing)
filemenu.add_command(label="Paste", command=Nothing)
filemenu.add_command(label="Delete", command=Nothing)
filemenu.add_separator()
filemenu.add_command(label="Find...", command=Nothing)
filemenu.add_command(label="Find Next", command=Nothing)
filemenu.add_command(label="Replace...", command=Nothing)
filemenu.add_command(label="Go To...", command=Nothing)
filemenu.add_separator()
filemenu.add_command(label="Select All", command=root.quit)
filemenu.add_command(label="Time/Date", command=root.quit)
menubar.add_cascade(label=" Edit ", menu=filemenu)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Word Wrap", command=Nothing)
filemenu.add_command(label="Font...", command=Nothing)
menubar.add_cascade(label=" Format ", menu=filemenu)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Status Bar", command=Nothing)
menubar.add_cascade(label=" View ", menu=filemenu)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="View Help", command=Nothing)
filemenu.add_separator()
filemenu.add_command(label="About Notepad", command=Nothing)
menubar.add_cascade(label=" Help ", menu=filemenu)

root.geometry('{}x{}'.format(1366, 768))
root.config(menu=menubar)
root.mainloop()
