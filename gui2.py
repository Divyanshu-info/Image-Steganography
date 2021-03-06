from tkinter.filedialog import *
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui2_support
import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel2 (root)
    gui2_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel2(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel2(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel2 (w)
    gui2_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel2():
    global w
    w.destroy()
    w = None

class Toplevel2:
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

        top.geometry("600x461+383+167")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("New Toplevel")

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.017, rely=0.022, relheight=0.967
                , relwidth=0.975)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TEntry1 = ttk.Entry(self.TFrame1)
        self.TEntry1.place(relx=0.205, rely=0.022, relheight=0.052
                , relwidth=0.708)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="xterm")

        self.TEntry2 = ttk.Entry(self.TFrame1)
        self.TEntry2.place(relx=0.205, rely=0.09, relheight=0.052
                , relwidth=0.708)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="xterm")

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.017, rely=0.022, height=21, width=108)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Input File Name''')

        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.137, rely=0.09, height=21, width=28)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Key''')

        self.TButton1 = ttk.Button(self.TFrame1)
        self.TButton1.place(relx=0.923, rely=0.022, height=30, width=33)
        self.TButton1.configure(command=lambda: gui_support.UploadAction2(
            self.TEntry1,self.TLabel3, askopenfilename()))
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''...''')

        self.TLabel3 = ttk.Label(self.TFrame1)
        self.TLabel3.place(relx=0.017, rely=0.157, height=311, width=558)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Tlabel''')

        self.TButton2 = ttk.Button(self.TFrame1)
        self.TButton2.place(relx=0.427, rely=0.919, height=30, width=83)
        self.TButton2.configure(command=lambda: gui_support.decode_gui(
            self.TEntry1, self.TEntry2))
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Decode''')

if __name__ == '__main__':
    vp_start_gui()





