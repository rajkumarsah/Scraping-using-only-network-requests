import requests
import json

payload={}
headers = {}
pageNo=1

try:
    response = requests.request("GET", "https://bg.annapurnapost.com/api/news/list?page={}&category_alias=bharkharai&per_page=30".format(pageNo), headers=headers, data=payload)
except Exception as e:
    pageNo+=1
    response = requests.request("GET", "https://bg.annapurnapost.com/api/news/list?page={}&category_alias=bharkharai&per_page=30".format(pageNo), headers=headers, data=payload)
    


jsonData = json.loads(response.text)

data = {}
i=1
for article in jsonData['data']:
    articleId = article['id']
    articleTitle = article['title']
    articlePublishOn = article['publishOn']
    oneData={}
    oneData['id']=articleId
    oneData['title'] = articleTitle
    oneData['publishOn'] = articlePublishOn
    data['article'+str(i)] = oneData
    i+=1

print(data)

with open('30_article.json', 'w') as fp:
    json.dump(data, fp, indent=4)