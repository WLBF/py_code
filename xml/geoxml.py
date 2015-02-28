import urllib
import xml.etree.ElementTree as ET




url = raw_input('Enter location: ')
 
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)


results = tree.findall('.//count')

print 'Count:',len(results)

ans = 0
for result in results:
    ans += int(result.text)

print 'Sum', ans

