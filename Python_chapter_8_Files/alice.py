def count_words(filenames):
    '''Подсчет слов в книге'''
    try:
        with open (filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f'Sorry file {filename} not found')
    else:
        words = content.split()
        num_words = len(words)
        print (f'The file {filename} has about {num_words} worlds.')

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_woman']
for filename in filenames:
    count_words(filename)

