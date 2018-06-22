import requests


def doit(url):
    flag = False
    responseurl = requests.get(url)
    reurljson = responseurl.json()
    if responseurl.status_code == 200:
        it = reurljson['_embedded']['inspections']
        c =len (it)
        if c != 0:
            for i in range(0，c):
                print(it[i])
        else:
            flag = True
    else:
        flag = True
    return flag


f = open('scrproject.txt')
for line in f:
    project = line.strip()[28:]

    startpoint = 'https://scrutinizer-ci.com/api/repositories/g'
    token = 'access_token=aae438c3981964239614d6213616bebb31e61f0f788f2b5622632a6e31e4e243'

    for i in range(1,5000):
        url = startpoint + project + '/inspections?page=%s&per_page=50 ' %i +token
        itflag = doit(url)
        if itflag:
            break


