import sys
import tkinter as tk
import tkinter.ttk as ttk

import gui3_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui3_support.init(root, top)
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
    gui3_support.init(w, top, *args, **kwargs)
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

        top.geometry("600x450+368+166")
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

        self.TButton1 = ttk.Button(self.TFrame1)
        self.TButton1.place(relx=0.325, rely=0.023, height=120, width=203)
        self.TButton1.configure(command=lambda: gui3_support.encode_window())
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Encode Image''')

        self.TButton2 = ttk.Button(self.TFrame1)
        self.TButton2.place(relx=0.325, rely=0.322, height=120, width=203)
        self.TButton2.configure(command=lambda: gui3_support.decode_window())
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Decode Image''')

if __name__ == '__main__':
    vp_start_gui()





