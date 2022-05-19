import requests
import keys
import pandas as pd
from time  import sleep

#seguir este video para cria rum alert de crypto e receber no email
# https://www.youtube.com/watch?v=0ZJwW395viQ
def get_crypto_rates(base_currency='EUR', assets='SOL,ETH,XRP,BTC'):
    url = 'https://api.nomics.com/v1/currencies/ticker'
    
    
    payload = {'key ': keys.nomics_api_key, 'convert':base_currency, 'ids': assets, 'interval':'id'}
    response = requests.get(url, params=payload)
    data = response.json()
     
    crypto_currency,  crypto_price, crypto_timestamp = [],[],[]
    
    print(data)
    for asset in data:
        crypto_currency.append(asset['currency']) 
        crypto_price.append(asset['price'])
        crypto_timestamp.append(asset['price_timestamp'])
        
    raw_data = {
        'assets' : crypto_currency,
        'rates' : crypto_price,
        'timestamp' : crypto_timestamp
    }
    
    df =  pd.DataFrame(raw_data)
    print(df)
    return df

get_crypto_rates()