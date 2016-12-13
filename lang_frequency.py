# _*_ coding: cp866 _*_
import string,sys
strp=string.whitespace+string.punctuation+string.digits+"\"'"+'\u2013'
f=open(sys.argv[1],'r')
dic={}
for line in f:
    for word in line.lower().split():
        word=word.strip(strp)
        if word:
            dic[word]=dic.get(word,0)+1
f.close()

for i in sorted(list(dic.items()),key=lambda x: x[1],reverse=True)[:10]:
    print (i[0]+' '+str(i[1]))
