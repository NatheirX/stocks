import tkinter 
import matplotlib.pyplot as plt
import matplotlib
import csv
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from buystock import money, going_down, going_up, stock

#defining tkinter functions
def stockchange():
    f = open("stockname.py","w+")
    f.write("Stockname = " + str(stocknameentry.get()))
    

time_data = going_up
time_loss = going_down

data = pd.read_csv(stock)
data = data[["counter", "middle_band"]]
time = []

for i in data["counter"]:
    time.append(i)
position = []
for i in data["middle_band"]:
    position.append(i)

#print(len(time), len(position))

matplotlib.use("TkAgg")
root = tkinter.Tk()
root.title("Stock Market Visualizer")
root.geometry("500x750")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

#graphing graph data
a.plot(time, position, color="blue")

#putting buy/sell 
for i in time_data:
    a.plot(i[0], i[1], color="green", marker=".", markersize=10)
for i in time_loss:
    a.plot(i[0], i[1], color="red", marker=".", markersize=10)
#graphing matplotlib to tkinter
graph_frame = tkinter.LabelFrame(root)
graph_frame.grid(row=0, column=0, columnspan=5)
canvas = FigureCanvasTkAgg(f, graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, graph_frame)
toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

#making layout to tkinter
stocknameentry = tkinter.Entry(root, text="Stockfile Path",bg="light blue")
stocknameentry.grid(row=1,column=1,sticky="W")
stocknamelabel = tkinter.Label(root,text="Stockfile path: ")
stocknamelabel.grid(row=1,column=0, sticky="e")
stocknamebutton = tkinter.Button(root, text="Submit", command=stockchange)
stocknamebutton.grid(row=1, column=2, sticky="W")
stocknamemoney = tkinter.Label(root, text="Money: " +str(money))
stocknamemoney.grid(row=1,column=3, sticky= "E")



root.mainloop()