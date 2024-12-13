import tkinter as tk
from tkinter import ttk
import os
#from Image import Image
#from Atlas import Atlas
from Pages import *
from abc import ABC

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.pages = [Starter(self.root)]
        self.curr_page_idx = 0
        
        self.pg_header = tk.StringVar()
        pg_header_label = ttk.Label(self.root,textvariable=self.pg_header)

        btns_frame = ttk.Frame(self.root)
        self.prev_txt = tk.StringVar(value='Previous')
        self.nxt_txt = tk.StringVar(value='Next')
        self.prev_btn = ttk.Button(btns_frame,textvariable=self.prev_txt, command=self.prev_pg)
        self.nxt_btn = ttk.Button(btns_frame,textvariable=self.nxt_txt, command=self.nxt_pg)

        pg_header_label.grid(row=0, column=0)
        btns_frame.grid(row=2, column=0,sticky='we',padx=10, pady=5)
        self.prev_btn.pack(side=tk.LEFT)
        self.nxt_btn.pack(side=tk.RIGHT)

    def start(self):
        self.update()
        self.root.mainloop()
    
    def nxt_pg(self):
        nxt_pg = self.pages[self.curr_page_idx].next()
        if self.curr_page_idx == 4:
            self.root.destroy()
            return
        self.curr_page_idx += 1
        self.pages.append(nxt_pg)
        self.update()

    def prev_pg(self):

        if self.curr_page_idx == 0: 
            self.root.destroy()
            return

        self.pages[self.curr_page_idx].frame.destroy()
        self.pages.pop(self.curr_page_idx)
        self.curr_page_idx -= 1
        self.update()
    
    def update(self):
        # activate current page
        self.pages[self.curr_page_idx].activate()
        
        # show page header for current page
        self.pg_header.set(self.pages[self.curr_page_idx].header)

        # logic for showing next and previous buttons
        self.prev_txt.set('Previous')
        self.nxt_txt.set('Next')
        if self.curr_page_idx == 0:
            self.prev_txt.set('Exit')
        elif self.curr_page_idx == 4:
            self.nxt_txt.set('Finish')


# Actually run the app
app = App()
app.start()
