import requests




valut = "USD"
date = "20240126"
url1 = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valut}&date={date}&json"
r = requests.get(url1)
if r.status_code == 200:
    data = r.json()
    print(data)
else:
    print("помилка")