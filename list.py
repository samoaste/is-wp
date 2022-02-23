import requests
list = ['https://incuca.net','https://play.incuca.net']
#Loop through the whole list of domains 
for f in list:
    counter = 0
    source = requests.get(f).text
    if "wp-include" in source:
        results = 'WordPress'
    else:
        results = 'Não é WordPress'
    counter = counter+1
    print(f, results)