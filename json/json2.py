import json
import urllib

url = raw_input('Enter URL: ')
uh = urllib.urlopen(url)
data = uh.read()


info = json.loads(data)

ans = 0
for item in info['comments']:
    ans += int(item['count'])

print ans
