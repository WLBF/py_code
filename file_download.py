import urllib2
import re


#url = "https://d3c33hcgiwev3.cloudfront.net/1-1%20%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B3%BB%E7%BB%9F%E6%A6%82%E5%BF%B5.47c984a0251811e5b4a44351e72baad6/full/360p/index.mp4?Expires=1453766400&Signature=TsOu7R4VQrKGWO1-SOys3IZW8U37Y-T4ddDob4Zet2jiNYodND4sCMXgh-zg12NZR~ww2DwZPh4NTEaN8GNJMXffKmhqjHzR9rcDDMvR4wkfKP3LavEUn2zD6RhaTUUIdKHe2lJekQSFkQAglobh5clEELcQe-lFoeP4TpywXr0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
#file_name = url.split('/')[-1]
#file_name = "test.mp4"
def file_downloader(url, file_name):
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = "\r%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    print status,

	f.close()



if __name__ == "__main__":
	f = open("download_list.txt")
	counter = 6
	for line in f:
		#print line
		#tmp = re.search("\.net/([0-9]*-[0-9]*)", line)
		#file_name = tmp.group(1)+r".mp4"
		file_name = str(counter)+r".mp4"
		file_downloader(line, file_name)
		print "\nFile ---{0}--- is done.".format(file_name)
		counter += 1

	f.close()