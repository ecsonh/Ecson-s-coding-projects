import tkinter as tk
from tkinter import ttk, filedialog
from Profile import Profile, Post
#from NaClProfile import NaClProfile
def close():
    window.destory()

def open_profile():
    filename = tk.filedialog.askopenfile(filetypes=[('Distributed Social Profile','*.dsu')])

def new_profile():
    filename = tk.filedialog.asksaveasfile(filetypes=[('Distributed Social Profile','*.dsu')])

window = tk.Tk()
window.title('ISC 32 Distributed Social Demo')
window.geometry('720x480')


menu_bar = tk.Menu(window)
window['menu'] = menu_bar
menufile = tk.Menu(menu_bar)
body_frame = tk.Frame(master = window, bg = "blue")
body_frame.pack(fill = tk.BOTH, side = tk.LEFT)

posts_frame = tk.Frame(master = body_frame, width = 250, bg = "white")
posts_frame.pack(fill = tk.BOTH, side = tk.LEFT)

posts_frame = tk.Frame(master = body_frame, width = 250, bg = "yellow")
posts_frame.pack(fill = tk.BOTH, side = tk.TOP, expand=True)

posts_frame = tk.Frame(master = body_frame, bg = "red")
posts_frame.pack(fill = tk.BOTH, side = tk.BOTTOM)

menu_bar.add_cascade(menu=menufile, label = 'File')
menufile.add_command(label = 'New', command = new_profile)
menufile.add_command(label = 'Open', command = open_profile)
window.update()
window.mainloop()
