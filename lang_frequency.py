import collections,string,argparse,sys

def load_data(filepath):
    txtfile=open(filepath,'r')
    return txtfile

def get_most_frequent_words(text):
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

def print_result(result):
    for word_and_number in result:
        print (word_and_number[0],word_and_number[1])

def create_parser():
    parser=argparse.ArgumentParser(prog='words counter',description="""
    Эта программа возвращает 10 наиболе популярных слов в текстовом
    файле. В качестве параметра file необходимо передавать путь к файлу""")
    parser.add_argument('textfile')
    return parser

if __name__ == '__main__':
    parser=create_parser()
    arguments=parser.parse_args()
    text=load_data(arguments.textfile)
    result=get_most_frequent_words(text)
    print("Итак, 10 наиболее порулярных слов в файле",arguments.textfile+':')
    print_result(result)
