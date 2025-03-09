import yfinance as yf

dat = yf.Ticker("BMW.DE")




for k,v in dat.info.items():
    print(f"{k}:{v}")