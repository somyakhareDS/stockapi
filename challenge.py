x=5456

start = 0
end = 500
while end>x:
    print(start,end)
    start = end
    end+= 500
start = end -500
end = x
print(start,end)


# Stock Screener

from keys import ameritrade
import requests


url= "https://api.tdameritrade.com/v1/instruments"
payload = {
        'apikey': ameritrade,
        'symbol':'GOOG',
        'projection': 'fundamental'
}

results = requests.get(url, params=payload)
