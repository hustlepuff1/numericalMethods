import requests

url = 'https://homepage.cnu.ac.kr/cic/data/offer.do?mode=view&articleNo=324650&article.offset=0&articleLimit=10'
params = {'serviceKey': '서비스키', 'type': 'json',
          'numOfRows': '10', 'pageNo': '1'}

response = requests.get(url, params=params)
print(response.content)
