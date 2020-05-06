import json

json_data = {'abc':0,'cc':[1,2,3,4,5]}
json_str = json.dumps(json_data)

#print(json_data)
#print(json_str)

fp = open('豆瓣电影json.txt', encoding='utf-8')
json_str1 = fp.read()

json_data1 = json.loads(json_str1)
#print(json_data1)
#print(json_data1[1]['title'])


result = ''

for i in range(20):
    #result += json_data1[i]['title']+ '\n'
    print(str(i+1) + '. ' + json_data1[i]['title'])
