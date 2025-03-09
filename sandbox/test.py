import yfinance as yf
from datetime import datetime


dat = yf.Ticker("BMW.DE")

heute = datetime.now().date()
print(" ")

preis = dat.history(period="3d")
for k,v in preis.items():
    print(f"k={k}: v={v}")
    print(" ")




    
