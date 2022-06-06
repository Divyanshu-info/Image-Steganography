import steno
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import *
from PIL import ImageTk, Image
import ntpath
import sys
ntpath.basename("a/b/c")


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def UploadAction(TEntry1, TEntry2, TLabel4, text):
    '''command=lambda:(gui_support.UploadAction(
    self.TEntry1, self.TEntry2, self.TLabel5, askopenfilename()))'''
    TEntry1.delete(0, 'end')
    TEntry1.insert('end', text)
    filename = path_leaf(text)
    text2 = text[0:len(text)-len(filename)] + "encoded_" + filename
    TEntry2.delete(0, 'end')
    TEntry2.insert('end', text2)
    img = Image.open(text)
    img.thumbnail((558, 271), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    TLabel4.configure(image=img)
    TLabel4.photo = img


def UploadAction2(TEntry1, TLabel3, text):
    '''command=lambda:(gui_support.UploadAction(
    self.TEntry1, self.TEntry2, self.TLabel5, askopenfilename()))'''
    TEntry1.delete(0, 'end')
    TEntry1.insert('end', text)
    img = Image.open(text)

    img.thumbnail((558, 311), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    TLabel3.configure(image=img)
    TLabel3.photo = img


def encode_gui(TEntry1, TEntry2, TEntry3, TEntry4):
    code = steno.Encode(TEntry1.get(), 
        TEntry3.get(), TEntry2.get(), TEntry4.get())
    if code == 0:
        messagebox.showinfo(
            "showinfo", "Image Encoded Successfully", parent=root_encode)
    elif code == 1:
        messagebox.showerror(
            "showinfo", "ERROR: Need larger file size", parent=root_encode)
    pass


def decode_gui(TEntry1, TEntry2):
    code = steno.Decode(TEntry1.get(), TEntry2.get())
    if code == 1:
        messagebox.showerror(
            "showinfo", "No Hidden Message Found", parent=root_decode)
    else:
        messagebox.showinfo(
            "showinfo", "Hidden Message is : " + code, parent=root_decode)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

class Toplevel_main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("600x450+368+166")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("Image Steganography")

        self.TFrame1_main = ttk.Frame(top)
        self.TFrame1_main.place(relx=0.017, rely=0.022,
                           relheight=0.967, relwidth=0.975)
        self.TFrame1_main.configure(relief='groove')
        self.TFrame1_main.configure(borderwidth="2")
        self.TFrame1_main.configure(relief="groove")

        self.TButton1_main = ttk.Button(self.TFrame1_main)
        self.TButton1_main.place(relx=0.325, rely=0.023, height=120, width=203)
        self.TButton1_main.configure(command=lambda: start_gui_encode())
        self.TButton1_main.configure(takefocus="")
        self.TButton1_main.configure(text='''Encode Image''')

        self.TButton2_main = ttk.Button(self.TFrame1_main)
        self.TButton2_main.place(relx=0.325, rely=0.322, height=120, width=203)
        self.TButton2_main.configure(command=lambda: start_gui_decode())
        self.TButton2_main.configure(takefocus="")
        self.TButton2_main.configure(text='''Decode Image''')


class Toplevel_encode:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("600x499+383+106")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("Encode Image")
        top.configure(highlightcolor="black")

        self.TFrame1_encode = ttk.Frame(top)
        self.TFrame1_encode.place(relx=0.017, rely=0.022,
                           relheight=0.968, relwidth=0.975)
        self.TFrame1_encode.configure(relief='groove')
        self.TFrame1_encode.configure(borderwidth="2")
        self.TFrame1_encode.configure(relief="groove")

        self.TLabel1_encode = ttk.Label(self.TFrame1_encode)
        self.TLabel1_encode.place(relx=0.034, rely=0.023, height=23, width=108)
        self.TLabel1_encode.configure(background="#d9d9d9")
        self.TLabel1_encode.configure(foreground="#000000")
        self.TLabel1_encode.configure(relief="flat")
        self.TLabel1_encode.configure(anchor='w')
        self.TLabel1_encode.configure(justify='left')
        self.TLabel1_encode.configure(text='''Input File Name''')

        self.TLabel2_encode = ttk.Label(self.TFrame1_encode)
        self.TLabel2_encode.place(relx=0.017, rely=0.083, height=23, width=118)
        self.TLabel2_encode.configure(background="#d9d9d9")
        self.TLabel2_encode.configure(foreground="#000000")
        self.TLabel2_encode.configure(relief="flat")
        self.TLabel2_encode.configure(anchor='w')
        self.TLabel2_encode.configure(justify='left')
        self.TLabel2_encode.configure(text='''Output File Name''')

        self.TLabel3_encode = ttk.Label(self.TFrame1_encode)
        self.TLabel3_encode.place(relx=0.108, rely=0.135, height=34, width=58)
        self.TLabel3_encode.configure(background="#d9d9d9")
        self.TLabel3_encode.configure(foreground="#000000")
        self.TLabel3_encode.configure(relief="flat")
        self.TLabel3_encode.configure(anchor='w')
        self.TLabel3_encode.configure(justify='left')
        self.TLabel3_encode.configure(text='''Message''')

        self.TEntry1_encode = ttk.Entry(self.TFrame1_encode)
        self.TEntry1_encode.place(relx=0.222, rely=0.023,
                           relheight=0.048, relwidth=0.691)
        self.TEntry1_encode.configure(takefocus="")
        self.TEntry1_encode.configure(cursor="xterm")

        self.TEntry2_encode = ttk.Entry(self.TFrame1_encode)
        self.TEntry2_encode.place(relx=0.222, rely=0.083,
                           relheight=0.048, relwidth=0.691)
        self.TEntry2_encode.configure(takefocus="")
        self.TEntry2_encode.configure(cursor="xterm")

        self.TEntry3_encode = ttk.Entry(self.TFrame1_encode)
        self.TEntry3_encode.place(relx=0.222, rely=0.145,
                           relheight=0.048, relwidth=0.691)
        self.TEntry3_encode.configure(takefocus="")
        self.TEntry3_encode.configure(cursor="xterm")

        self.TButton1_encode = ttk.Button(self.TFrame1_encode)
        self.TButton1_encode.place(relx=0.923, rely=0.023, height=30, width=33)
        self.TButton1_encode.configure(command=lambda: UploadAction(
            self.TEntry1_encode, self.TEntry2_encode, self.TLabel5_encode, askopenfilename(parent=root_encode)))
        self.TButton1_encode.configure(takefocus="")
        self.TButton1_encode.configure(text='''...''')

        self.TButton2_encode = ttk.Button(self.TFrame1_encode)
        self.TButton2_encode.place(relx=0.427, rely=0.911, height=30, width=83)
        self.TButton2_encode.configure(command=lambda: encode_gui(
            self.TEntry1_encode, self.TEntry2_encode, self.TEntry3_encode, self.TEntry4_encode))
        self.TButton2_encode.configure(takefocus="")
        self.TButton2_encode.configure(text='''Encode''')

        self.TLabel5_encode = ttk.Label(self.TFrame1_encode)
        self.TLabel5_encode.place(relx=0.017, rely=0.269, height=301, width=558)
        self.TLabel5_encode.configure(background="#d9d9d9")
        self.TLabel5_encode.configure(foreground="#000000")
        self.TLabel5_encode.configure(relief="flat")
        self.TLabel5_encode.configure(anchor='w')
        self.TLabel5_encode.configure(justify='left')

        self.TLabel4_encode = ttk.Label(self.TFrame1_encode)
        self.TLabel4_encode.place(relx=0.159, rely=0.207, height=21, width=28)
        self.TLabel4_encode.configure(background="#d9d9d9")
        self.TLabel4_encode.configure(foreground="#000000")
        self.TLabel4_encode.configure(relief="flat")
        self.TLabel4_encode.configure(anchor='w')
        self.TLabel4_encode.configure(justify='right')
        self.TLabel4_encode.configure(text='''Key''')

        self.TEntry4_encode = ttk.Entry(self.TFrame1_encode)
        self.TEntry4_encode.place(relx=0.222, rely=0.207,
                           relheight=0.048, relwidth=0.691)
        self.TEntry4_encode.configure(takefocus="")
        self.TEntry4_encode.configure(cursor="xterm")


class Toplevel_decode:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("600x461+383+167")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("Decode Image")

        self.TFrame1_decode = ttk.Frame(top)
        self.TFrame1_decode.place(relx=0.017, rely=0.022,
                           relheight=0.967, relwidth=0.975)
        self.TFrame1_decode.configure(relief='groove')
        self.TFrame1_decode.configure(borderwidth="2")
        self.TFrame1_decode.configure(relief="groove")

        self.TEntry1_decode = ttk.Entry(self.TFrame1_decode)
        self.TEntry1_decode.place(relx=0.205, rely=0.022,
                           relheight=0.052, relwidth=0.708)
        self.TEntry1_decode.configure(takefocus="")
        self.TEntry1_decode.configure(cursor="xterm")

        self.TEntry2_decode = ttk.Entry(self.TFrame1_decode)
        self.TEntry2_decode.place(relx=0.205, rely=0.09,
                           relheight=0.052, relwidth=0.708)
        self.TEntry2_decode.configure(takefocus="")
        self.TEntry2_decode.configure(cursor="xterm")

        self.TLabel1_decode = ttk.Label(self.TFrame1_decode)
        self.TLabel1_decode.place(relx=0.017, rely=0.022, height=21, width=108)
        self.TLabel1_decode.configure(background="#d9d9d9")
        self.TLabel1_decode.configure(foreground="#000000")
        self.TLabel1_decode.configure(font="TkDefaultFont")
        self.TLabel1_decode.configure(relief="flat")
        self.TLabel1_decode.configure(anchor='w')
        self.TLabel1_decode.configure(justify='left')
        self.TLabel1_decode.configure(text='''Input File Name''')

        self.TLabel2_decode = ttk.Label(self.TFrame1_decode)
        self.TLabel2_decode.place(relx=0.137, rely=0.09, height=21, width=28)
        self.TLabel2_decode.configure(background="#d9d9d9")
        self.TLabel2_decode.configure(foreground="#000000")
        self.TLabel2_decode.configure(font="TkDefaultFont")
        self.TLabel2_decode.configure(relief="flat")
        self.TLabel2_decode.configure(anchor='w')
        self.TLabel2_decode.configure(justify='left')
        self.TLabel2_decode.configure(text='''Key''')

        self.TButton1_decode = ttk.Button(self.TFrame1_decode)
        self.TButton1_decode.place(relx=0.923, rely=0.022, height=30, width=33)
        self.TButton1_decode.configure(command=lambda: UploadAction2(
            self.TEntry1_decode, self.TLabel3_decode, askopenfilename(parent=root_decode)))
        self.TButton1_decode.configure(takefocus="")
        self.TButton1_decode.configure(text='''...''')

        self.TLabel3_decode = ttk.Label(self.TFrame1_decode)
        self.TLabel3_decode.place(relx=0.017, rely=0.157, height=311, width=558)
        self.TLabel3_decode.configure(background="#d9d9d9")
        self.TLabel3_decode.configure(foreground="#000000")
        self.TLabel3_decode.configure(font="TkDefaultFont")
        self.TLabel3_decode.configure(relief="flat")
        self.TLabel3_decode.configure(anchor='w')
        self.TLabel3_decode.configure(justify='left')
        self.TLabel3_decode.configure(text='''''')

        self.TButton2_decode = ttk.Button(self.TFrame1_decode)
        self.TButton2_decode.place(relx=0.427, rely=0.919, height=30, width=83)
        self.TButton2_decode.configure(command=lambda: decode_gui(
            self.TEntry1_decode, self.TEntry2_decode))
        self.TButton2_decode.configure(takefocus="")
        self.TButton2_decode.configure(text='''Decode''')


def start_gui():
    '''Starting point when module is the main routine.'''
    global val_main, w_main, root_main
    root_main = tk.Tk()
    top_main = Toplevel_main(root_main)
    init(root_main, top_main)
    root_main.mainloop()

def start_gui_encode():
    '''Starting point when module is the main routine.'''
    global val_encode, w_encode, root_encode
    root_encode = tk.Toplevel(root_main)
    top_encode = Toplevel_encode(root_encode)
    init(root_encode, top_encode)
    root_encode.mainloop()
    
def start_gui_decode():
    '''Starting point when module is the main routine.'''
    global val_decode, w_decode, root_decode
    root_decode = tk.Toplevel(root_main)
    top_decode = Toplevel_decode(root_decode)
    init(root_decode, top_decode)
    root_decode.mainloop()

def main():
    start_gui()

