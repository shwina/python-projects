import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from numpy import linspace, sin
from Tkinter import *


class plotApp:

    def __init__(self, master):

        self.master = master

        labelsFrame = self.makeLabels()
        boxesFrame  = self.makeEntryBoxes()
        plotFrame   = self.makePlotArea()
        plotButton = Button(self.master, text='PLOT!', command=self.make_plot, padx=2)

        labelsFrame.grid(column=0, row=0)
        boxesFrame.grid(column=1, row=0)
        plotFrame.grid(column=2, row=0, rowspan=2)
        plotButton.grid(column=0, row=1, columnspan=2)


    def makeLabels(self):

        # make a frame for the labels
        frame = Frame(self.master)
        
        # the names of labels in order:d
        names = ['A', 'B', 'C']

        # now, make a label for each name:
        self.labels = []
        for i in range(3):
            self.labels.append(Label(frame, text=names[i]))
            self.labels[i].pack()

        return frame

    def makeEntryBoxes(self):

        # make a frame for the entry boxes:
        frame = Frame(self.master)

        self.boxes = []
        for i in range(3):
            self.boxes.append(Entry(frame, width = 4))
            self.boxes[i].pack()

        return frame


    def makePlotArea(self):

        frame = Frame(self.master)

        self.f = Figure(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.f, frame)
        self.canvas.show()
        toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        return frame

    def make_plot(self):

        # get the parameters:
        A = float(self.boxes[0].get())
        B = float(self.boxes[1].get())
        C = float(self.boxes[2].get())

        x = linspace(0, 1, 100)
        a = self.f.add_subplot(211)
        a.plot(x, A*sin(B*(x + C)))
        b.plot(x, A*sin(x))
        self.canvas.show()

root = Tk()
plotApp(root)
root.mainloop()