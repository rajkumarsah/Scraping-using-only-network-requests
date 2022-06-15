import requests
import json

payload={}
headers = {}

errorChecking = requests.request("GET", "https://bg.annapurnapost.com/api/news/list?page=1&category_alias=bharkharai&per_page=30", headers=headers, data=payload)    

print(errorChecking.status_code)

def pagination(pageNo):
        
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

    #Storing scraped data in json file!!

    with open('30_article.json', 'w') as fp:
        json.dump(data, fp, indent=4)

#Scrapping from second page if error occured!!

if errorChecking.status_code==200:
    pagination(1)
else:
    pagination(2)
