# _*_ coding: cp866 _*_
import string,sys
if sys.argv[1]=="--help":
    print("""Эта программа выводит 10 наиболее часто встречающихся слов в текстовом файле.
В качестве параметра командной строки необходимо передать путь к файлу""")
else:
    strp=string.whitespace+string.punctuation+string.digits+"\"'"+'\u2013'
    f=open(sys.argv[1],'r')
    dic={}
    for line in f:
        for word in line.lower().split():
            word=word.strip(strp)
            if word:
                dic[word]=dic.get(word,0)+1
    f.close()
    print("Итак, 10 наиболее популярных слов в файле ",sys.argv[1],':')
    for i in sorted(list(dic.items()),key=lambda x: x[1],reverse=True)[:10]:
        print (i[0]+' '+str(i[1]))
