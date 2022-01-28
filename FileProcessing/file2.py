import time
import os
import pandas

while True:
    if os.path.exists("FileProcessing/files/temps_today.csv"):
        data = pandas.read_csv("FileProcessing/files/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File not found")
    time.sleep(10)
    