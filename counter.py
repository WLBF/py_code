import os
import re
import sys

LINES = 0
types = ["py", "scm", "cpp", "c"]



def valid(line):
        global parts
        if re.match(r"^[\s]*$|^\s*[/\*#]", line)!=None:
                return False

        return True




def countLines(location):
        global LINES
        f = open(location)
        for line in f:
                #print line
                if valid(line):
                        LINES += 1
                        #sys.stdout.write(line)
        f.close()



def counter(rootDir):
        global types
        temp = os.walk(rootDir)
        for root, dirs, files in temp:
                for f in files:
                        matchObj = re.match(r".*\.(.*)", f)
                        if matchObj != None and (matchObj.groups()[0] in types):
                                #print os.path.join(root, f)
                                countLines(os.path.join(root, f))
                                
                                


if __name__ == "__main__":
        rootDir = raw_input("Root:")
        #rootDir = "C:\Users\Bofan\Documents\RK4"
        counter(rootDir)
        print "LinesNum:",LINES
