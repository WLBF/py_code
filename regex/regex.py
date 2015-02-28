import re


f = open("regex_sum_204411.txt")
#f = open("regex_sum_42.txt")

ans = 0

for line in f:
    lst = re.findall('[0-9]+', line)
    if lst!=[]:
        for strnum in lst:
            ans += int(strnum)

f.close()

print ans
