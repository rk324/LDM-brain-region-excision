import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import skimage as ski

'''
Image class for displaying target images

### fields ###
frame: the frame containing image, button, etc

__img: img data

load_file_btn: button for loading image data, is hidden 
after image chosen

### functions ###
__init__: creates frame to hold everything, load & display image
if filename provided

load: loads image data from file selected via file dialog

display: displays image data
'''
class Image: 

    '''
    Initialize with master frame and optional filename of image.
    Create button to load image data
    Will load and display image and if filename is provided
    '''
    def __init__(self, master, filename=None):
        self.frame = ttk.Frame(master=master)
        self.frame.pack()

        self.load_file_btn = ttk.Button(master=self.frame, text="Load data", command=self.load)
        self.load_file_btn.pack()
        
        if filename is not None: self.load(filename)
        
    '''
    Load image data using a file dialog, then call display()
    if file is chosen and hide file load button.
    Takes optional filename parameter.
    Returns True if successful image load, false is no valid image file chosen.
    '''
    def load(self, filename=None):
        
        if filename is None:
            file = tk.filedialog.askopenfile() # TODO: make it only allow image files, handle errors by bad file load
            if file is None:
                return False
            filename = file.name
        
        self.__img = ski.io.imread(filename)
        self.display()
        self.load_file_btn.pack_forget()

        return True
  
    '''
    Display image data using matplotlib
    '''
    def display(self):
        fig = Figure()
        fig.add_subplot(111).imshow(self.__img)
        canvas = FigureCanvasTkAgg(fig,master=self.frame)
        canvas.draw()
        
        # add mpl toolbar to allow zoom, translation
        toolbar = NavigationToolbar2Tk(canvas, self.frame) 
        toolbar.update() 

        canvas.get_tk_widget().pack()
    
        