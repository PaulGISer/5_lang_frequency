import collections,string,argparse,sys

def loadData(filepath):
    file=open(filepath,'r')
    return file

def getMostFrequentWords(text):
    # симлволы, которые необходимо исключать из слов
    strip_string_chars=string.whitespace+string.punctuation+string.digits
    # символы, которые программа может воспринять как слова
    bad_chars='–—'
    collection=collections.Counter()
    for line in text:
        for word in line.lower().split():
            if not word in bad_chars:
                collection[word.strip(strip_string_chars)]+=1
    return collection.most_common(10)

def printRezult(rezult):
    for pair in rezult:
        print (pair[0],pair[1])

def createParser():
    parser=argparse.ArgumentParser(prog='words counter',description="""
    Эта программа возвращает 10 наиболе популярных слов в текстовом
    файле. В качестве параметра file необходимо передавать путь к файлу""")
    parser.add_argument('file')
    return parser

if __name__ == '__main__':
    parser=createParser()
    txt_file=parser.parse_args()
    text=loadData(txt_file.file)
    rezult=getMostFrequentWords(text)
    print("Итак, 10 наиболее порулярных слов в файле",txt_file.file+':')
    printRezult(rezult)
