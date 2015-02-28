import urllib2

def proxy_get(url):

    proxies = {'http': '127.0.0.1:8087',
               'https': '127.0.0.1:8087'}
    proxy_handler = urllib2.ProxyHandler(proxies)

    opener = urllib2.build_opener(proxy_handler)


    
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    req = urllib2.Request(url,headers = header)
    load = opener.open(url)
    content = load.read()
    print content

proxy_get("http://www.t66y.com/index.php")
