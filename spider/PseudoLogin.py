import urllib
import urllib2
import cookielib
import re


LoginUrl = "http://XXXXXXXXXXXX/login"
Username = "XXXX"
Password = "XXXX"
Lt = ""
Cookie = cookielib.CookieJar()
CookieHandler = urllib2.HTTPCookieProcessor(Cookie)
Opener = urllib2.build_opener(CookieHandler)


Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}
Data = {"username":Username,
        "password":Password,
        "lt":"",
        "execution":"e1s1",
        "_eventId":"submit",
        "submit":"%B5%C7%C2%BC",
        }


        


Load = Opener.open(LoginUrl)
Content = Load.read()
Reg = r'name="lt" value="(.*)" />'
Result = re.findall(Reg, Content)
if len(Result) == 0:
    print "Fail to find -- 'It'."
print Result[0]
Data["lt"] = Result[0]

#print Content

PostData = urllib.urlencode(Data)
print PostData 
Req = urllib2.Request(LoginUrl, PostData, Header)

#print Req

      
Response = Opener.open(Req)
Page = Response.read()
#print Page

if re.search(r'<div id="msg" class="errors">', Page):
    print "Wrong password!"
else:
    print "Success login!"
  
        

    
