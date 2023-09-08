from urllib import request

data = b'{"HEB": "test1", "parameter2": "test2"}'
req = request.Request("https://whois.arin.net/ui/query.do", data)
resp = request.urlopen(req).read().decode('utf-8')
print(resp)
