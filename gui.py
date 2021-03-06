from tkinter.filedialog import *

import sys
import tkinter as tk
import tkinter.ttk as ttk

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x499+383+106")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.017, rely=0.022, relheight=0.968
                , relwidth=0.975)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.034, rely=0.023, height=23, width=108)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Input File Name''')

        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.017, rely=0.083, height=23, width=118)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Output File Name''')

        self.TLabel3 = ttk.Label(self.TFrame1)
        self.TLabel3.place(relx=0.108, rely=0.135, height=34, width=58)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Message''')

        self.TEntry1 = ttk.Entry(self.TFrame1)
        self.TEntry1.place(relx=0.222, rely=0.023, relheight=0.048
                , relwidth=0.691)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="xterm")

        self.TEntry2 = ttk.Entry(self.TFrame1)
        self.TEntry2.place(relx=0.222, rely=0.083, relheight=0.048
                , relwidth=0.691)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="xterm")

        self.TEntry3 = ttk.Entry(self.TFrame1)
        self.TEntry3.place(relx=0.222, rely=0.145, relheight=0.048
                , relwidth=0.691)
        self.TEntry3.configure(takefocus="")
        self.TEntry3.configure(cursor="xterm")

        self.TButton1 = ttk.Button(self.TFrame1)
        self.TButton1.place(relx=0.923, rely=0.023, height=30, width=33)
        self.TButton1.configure(command=lambda: gui_support.UploadAction(
            self.TEntry1, self.TEntry2, self.TLabel5, askopenfilename()))
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''...''')

        self.TButton2 = ttk.Button(self.TFrame1)
        self.TButton2.place(relx=0.427, rely=0.911, height=30, width=83)
        self.TButton2.configure(command=lambda: gui_support.encode_gui(self.TEntry1, self.TEntry2, self.TEntry3, self.TEntry4))
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Encode''')

        self.TLabel5 = ttk.Label(self.TFrame1)
        self.TLabel5.place(relx=0.017, rely=0.269, height=301, width=558)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')

        self.TLabel4 = ttk.Label(self.TFrame1)
        self.TLabel4.place(relx=0.159, rely=0.207, height=21, width=28)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='right')
        self.TLabel4.configure(text='''Key''')

        self.TEntry4 = ttk.Entry(self.TFrame1)
        self.TEntry4.place(relx=0.222, rely=0.207, relheight=0.048
                , relwidth=0.691)
        self.TEntry4.configure(takefocus="")
        self.TEntry4.configure(cursor="xterm")

if __name__ == '__main__':
    vp_start_gui()





