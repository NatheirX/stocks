import matplotlib.pyplot as plt
import csv
import pandas as pd


data = pd.read_csv("graph\Stockday05-19AAPL.csv")
data = data[["counter", "middle_band"]]
print(data)
time = []

for i in data["counter"]:
    time.append(i)
position = []
for i in data["middle_band"]:
    position.append(i)


plt.plot(time, position)
plt.show()