import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from numpy import linspace, sinh, cosh, sqrt
from math import pi

from Tkinter import *


class plotApp:

    def __init__(self, master):

        self.master = master

        labelsFrame = self.makeLabels()
        boxesFrame  = self.makeEntryBoxes()
        plotFrame   = self.makePlotArea()

        plotButton = Button(self.master, text='PLOT!', command=self.make_plot)

        self.boxesFrame = boxesFrame

        labelsFrame.grid(column=0, row=0)
        boxesFrame.grid(column=1, row=0)
        plotFrame.grid(column=2, row=0, rowspan=2)
        plotButton.grid(column=0, row=1, columnspan=2)


    def makeLabels(self):

        # make a frame for the labels
        frame = Frame(self.master)
        
        # the names of labels in order:d
        names = ['L', 'D', 'H', 'Gamma', 'mu', 'Q_0', 'P_0', 'P_infty', 'C_0', 'eta_g']

        # now, make a label for each name:
        self.labels = []
        for i in range(10):
            self.labels.append(Label(frame, text=names[i]))
            self.labels[i].pack()

        return frame

    def makeEntryBoxes(self):

        # make a frame for the entry boxes:
        frame = Frame(self.master)

        self.boxes = []
        for i in range(10):
            self.boxes.append(Entry(frame, width = 6))
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
        L = float(self.boxes[0].get())
        D = float(self.boxes[1].get())
        H = float(self.boxes[2].get())
        Gamma = float(self.boxes[3].get())
        mu = float(self.boxes[4].get())
        Q_0 = float(self.boxes[5].get())
        P_0 = float(self.boxes[6].get())
        P_infty = float(self.boxes[7].get())
        C_0 = float(self.boxes[8].get())
        eta_g = float(self.boxes[9].get())

        x = linspace(0, L, 100)
        lambda_C = sqrt(D**3*H/128/Gamma)
        Q_ref = pi*D**4/(128*mu*lambda_C)*(P_0-P_infty)
        print Q_ref
        a = self.f.add_subplot(111)
        a.plot(x, -Q_ref*sinh(x/lambda_C)+Q_0*cosh(x/lambda_C))
        self.canvas.show()

root = Tk()
plotApp(root)
root.mainloop()