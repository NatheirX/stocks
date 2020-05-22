import requests
import csv
from time import sleep

stock_names = ["SURF"]


for stock in stock_names:
    lst_data = []
    url = "https://twelvedata.p.rapidapi.com/bbands"
    querystring = {"start_date":"2020-03-15","sd":"2","end_date":"2020-05-18","outputsize":"5000","series_type":"close","ma_type":"SMA","time_period":"20","symbol":stock,"interval":"1min","apikey":"59425131999148a7be6eb17b7d19fd61"}

    headers = {
    'x-rapidapi-host': "twelvedata.p.rapidapi.com",
    'x-rapidapi-key': "fe4c7feda4msh612b76ef8e665fcp1a798ajsne8b70b6f0b4a"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.text

    countee = 0
    for i in eval(data)["values"]:
        
        lst_data.append(i)

    csv_columns = ["datetime", "counter", "upper_band", "middle_band", "lower_band", "countee"]

    csv_file = "StockTestwithgaps-" + stock + ".csv"
    lst_data = lst_data[::-1]


    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        counter = 0
        for data in lst_data:
            data["counter"],data["countee"] = counter, 0
            
            writer.writerow(data)
            counter += 1


